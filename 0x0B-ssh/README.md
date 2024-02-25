# 0x0B. SSH

## Task 0:

0. Use a private key

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

### Requirements:

- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase

### Solution

```bash
ssh [username]@[server IP]


## Task 1:

1. Create an SSH key pair

Write a Bash script that creates an RSA key pair.

### Requirements:

- Name of the created private key must be school
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty

### Solution

```bash
ssh-keygen -b [number of bits] -P [paraphrase] -f [name of private key]
