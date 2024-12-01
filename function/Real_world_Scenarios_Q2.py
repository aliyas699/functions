import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."
    
    # Define the characters available for the password
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password