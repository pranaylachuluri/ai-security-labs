# Lab 2 — SQL injection

Environment: SEED Labs Docker containers (Apache + PHP web app, MySQL `sqllab_users` database).

## Attacks

| Task | Target | Payload idea | Result |
|------|--------|--------------|--------|
| 2.1 | Login form (`SELECT ... WHERE name='$u' AND Password='$p'`) | `admin' #` in the username comments out the password check | Logged in as Admin with any password |
| 2.2 | Same, from the command line | `curl` with the URL-encoded payload `admin%27%23` | Server returned every employee record |
| 2.3 | Stacked queries | Appending `; UPDATE ...` | Blocked: PHP's `mysqli::query` runs one statement only |
| 3.1 | Edit-profile form (`UPDATE ... SET nickname='$n', ...`) | `', salary=80000 WHERE ID=1;#` | Raised my own salary |
| 3.2 | Same | `', salary=1 WHERE ID=2;#` | Changed another employee's salary |
| 3.3 | Same | Overwrote another user's password with the hash of a password I chose | Logged in as that user |

## Defense — prepared statements

Rewrote the vulnerable login query in `unsafe.php` to use `mysqli` prepared statements
(`prepare` → `bind_param` → `execute`), so user input is sent as data and never parsed as SQL.
All Task 2 payloads stopped working, while legitimate logins still returned the right record.

## Takeaways
String-built SQL is exploitable on both reads and writes; parameterized queries fix the
root cause, while single-statement execution only limits one technique.
