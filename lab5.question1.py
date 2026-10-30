
#Generate a Python script that collects and stores user data including name, email, and password in a file. First, provide a basic version that stores the data, then analyze the script for privacy and security risks. Specifically check whether the password or other sensitive information is stored in plain text, whether the file is properly protected, and identify any other security vulnerabilities. Finally, provide a revised and more secure version of the Python script that uses password hashing (such as bcrypt or hashlib with a secure salt) instead of storing passwords in plain text. Explain the security improvements made in the revised version.


import getpass
import hashlib
import json
import os
import secrets


# BASIC VERSION (DO NOT USE IN PRODUCTION):
# The password and other data are written directly to disk in plain text.
def store_basic_user():
	user = {
		"name": input("Name: "),
		"email": input("Email: "),
		"password": getpass.getpass("Password: "),
	}
	with open("users_basic.jsonl", "a", encoding="utf-8") as file:
		file.write(json.dumps(user) + "\n")


# Risks in the basic version:
# - Passwords are plain text, so anyone reading the file can use them.
# - The file may be readable by other users or exposed by backups/cloud sync.
# - There is no validation, authentication, access control, encryption, or
#   protection against duplicate accounts and malformed input.


SECURE_FILE = "users_secure.jsonl"
ITERATIONS = 600_000


def hash_password(password, salt):
	"""Hash a password with a unique salt using PBKDF2-HMAC-SHA256."""
	return hashlib.pbkdf2_hmac(
		"sha256", password.encode("utf-8"), salt, ITERATIONS
	).hex()


def store_secure_user():
	name = input("Name: ").strip()
	email = input("Email: ").strip().lower()
	password = getpass.getpass("Password: ")

	if not name or not email or not password:
		raise ValueError("Name, email, and password are required")

	salt = secrets.token_bytes(16)
	user = {
		"name": name,
		"email": email,
		"salt": salt.hex(),
		"password_hash": hash_password(password, salt),
	}

	# Restrict the file where supported; never store the password itself.
	file_exists = os.path.exists(SECURE_FILE)
	with open(SECURE_FILE, "a", encoding="utf-8") as file:
		if not file_exists:
			try:
				os.chmod(SECURE_FILE, 0o600)
			except OSError:
				pass  # Windows permissions must be configured separately.
		file.write(json.dumps(user) + "\n")


if __name__ == "__main__":
	store_secure_user()




