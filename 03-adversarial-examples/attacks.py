"""White-box adversarial attacks used in CSE 565 Lab 3.

The target is a ResNet-50 image classifier with a two-layer fully connected head
(pretrained weights from emiliantolo/pytorch_nsfw_model, not redistributed here).
Inputs are ImageNet-normalized tensors, so adversarial images are clipped to the
normalized range [-3, 3] instead of [0, 1].
"""
import torch
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def fgsm_attack(model, images, labels, epsilon):
    """Fast Gradient Sign Method: one step of size epsilon along sign(grad_x loss)."""
    images = images.clone().detach().to(device)
    labels = labels.clone().detach().to(device)
    images.requires_grad = True
    model.zero_grad(set_to_none=True)
    outputs = model(images)
    loss = F.cross_entropy(outputs, labels)
    loss.backward()
    perturbation = epsilon * images.grad.data.sign()
    adv_images = images + perturbation
    adv_images = torch.clamp(adv_images, -3.0, 3.0)
    return adv_images.detach()


def pgd_attack(model, images, labels, epsilon, alpha, iters):
    """Projected Gradient Descent: repeated FGSM steps of size alpha,
    projected back into the L-infinity ball of radius epsilon around the input."""
    ori_images = images.clone().detach().to(device)
    labels = labels.clone().detach().to(device)
    adv = ori_images.clone().detach().to(device)
    for _ in range(iters):
        adv.requires_grad = True
        model.zero_grad(set_to_none=True)
        outputs = model(adv)
        loss = F.cross_entropy(outputs, labels)
        loss.backward()
        grad_sign = adv.grad.data.sign()
        adv = adv + alpha * grad_sign
        eta = torch.clamp(adv - ori_images, min=-epsilon, max=epsilon)
        adv = ori_images + eta
        adv = torch.clamp(adv.detach(), -3.0, 3.0)
    return adv


@torch.no_grad()
def accuracy(model, images, labels):
    preds = model(images.to(device)).argmax(dim=1)
    return (preds == labels.to(device)).float().mean().item()
