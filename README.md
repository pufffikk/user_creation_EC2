# 🧪 Task: Automate User Creation with Python on EC2 (Amazon Linux 2)

## 📘 Objective

Write a Python script that connects to a running EC2 instance and:

1. Creates a **new Linux user** with a name you choose.
2. Creates a **home directory** for that user (if it's not automatically created).
3. Ensures the new user owns their home directory.

---

## 🧰 What You Need to Do

1. **SSH into your EC2 instance** manually to verify it's running and reachable.

2. Create a Python script on your **local machine** or **directly on the EC2 instance** that:
   - Uses the `subprocess` module (or similar) to run Linux commands.
   - Checks if the user already exists, and if not, creates it.
   - Ensures the user has a home directory (`/home/username`).
   - Sets correct ownership and permissions for the home directory.

3. **Test your script**:
   - Run it on the EC2 instance.
   - Use `ls`, `cat /etc/passwd`, and `ls -ld /home/username` to confirm that everything worked.

---

## 🧠 Hints

- Think about which Linux command adds a new user.
- Think about what happens automatically when using `useradd` with and without certain flags.
- Think about how to run those commands from inside Python.
- Look up the permissions and ownership using `ls -ld`.

---
