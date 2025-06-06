import subprocess
import sys
import os

username = "test_user"


def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    return process.returncode, process.stdout.strip(), process.stderr.strip()


code, _, _ = run_command(f"id -u {username}")
if code == 0:
    print(f"User '{username}' already exists.")
else:
    print(f"Creating user '{username}'...")
    code, out, err = run_command(f"useradd -m {username}")
    if code != 0:
        print(f"Failed to create user: {err}")
        sys.exit(1)
    print(f"User '{username}' created with home directory.")

home_dir = f"/home/{username}"
if not os.path.isdir(home_dir):
    print(f"Home directory not found. Creating manually...")
    code, _, err = run_command(f"mkdir -p {home_dir}")
    if code != 0:
        print(f"Failed to create home directory: {err}")
        sys.exit(1)


print(f"Setting ownership of {home_dir} to {username}:{username}...")
code, _, err = run_command(f"chown {username}:{username} {home_dir}")
if code != 0:
    print(f"Failed to set ownership: {err}")
    sys.exit(1)

print(f"Done! You can verify with:\n  cat /etc/passwd\n  ls -ld {home_dir}")
