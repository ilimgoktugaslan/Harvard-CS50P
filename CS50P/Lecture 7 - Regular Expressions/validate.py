import re

email=input("What's your email?").strip()

"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""
"""
username,domain=email.split("@")

if username and "." in domain:
    print("Valid")

if username and domain.endswith(".edu"):
    print("Valid")
else :
    print("Invalid")
"""

"""
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("Valid")
"""
if re.search(r"^\w+@(\w\.)?\w+\.(com|edu|gov|tr|net|org)$",email, re.IGNORECASE):
    print("Valid")

else :
    print("Invalid")

