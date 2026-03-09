import re


def is_valid_email(email):
    """
    Validates whether a given string is a valid email address.
    
    Checks for:
    - Presence of @ symbol
    - Valid format before @ (username)
    - Valid format after @ (domain name)
    - Presence of a dot (.) in domain
    - Valid domain extension
    
    Args:
        email: The email string to validate
    
    Returns:
        True if email is valid, False otherwise
    """
    
    # Basic checks
    if email is None or email == "":
        return False
    
    if email.count('@') != 1:
        return False
    
    # Split email into username and domain
    username, domain = email.split('@')
    
    # Check if username is not empty
    if not username or len(username) > 64:
        return False
    
    # Check if domain is not empty
    if not domain or len(domain) > 255:
        return False
    
    # Check if domain contains at least one dot
    if '.' not in domain:
        return False
    
    # Username pattern: alphanumeric, dots, hyphens, underscores
    username_pattern = r'^[a-zA-Z0-9._-]+$'
    if not re.match(username_pattern, username):
        return False
    
    # Domain pattern: alphanumeric, hyphens, dots
    domain_pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(domain_pattern, domain):
        return False
    
    # Check if domain starts or ends with a dot or hyphen
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    if domain.startswith('-') or domain.endswith('-'):
        return False
    
    # Check domain extension (TLD - Top Level Domain)
    domain_parts = domain.split('.')
    tld = domain_parts[-1]
    
    # TLD should be at least 2 characters and contain only letters
    if len(tld) < 2 or not tld.isalpha():
        return False
    
    # Check if consecutive dots exist
    if '..' in domain:
        return False
    
    return True


def email_validator_interactive():
    """
    Interactive email validation program.
    Allows user to validate multiple email addresses.
    """
    print("=" * 60)
    print("EMAIL VALIDATOR PROGRAM")
    print("=" * 60)
    print()
    print("This program validates email addresses.")
    print("Checks for: @ symbol, valid username, domain name, and TLD")
    print()
    
    while True:
        email = input("Enter an email address (or type 'exit' to quit): ").strip()
        
        if email.lower() == 'exit':
            print("Thank you for using Email Validator Program!")
            break
        
        if not email:
            print("Error: Email cannot be empty!")
            print()
            continue
        
        is_valid = is_valid_email(email)
        
        print("-" * 60)
        if is_valid:
            print("Result: VALID EMAIL")
        else:
            print("Result: INVALID EMAIL")
        print("-" * 60)
        print()


# Test cases for verification
if __name__ == "__main__":
    # Run the interactive program
    email_validator_interactive()
    
    # Or test with specific examples:
    """
    print("TEST CASES:")
    print()
    
    test_emails = [
        # Valid emails
        ("john@example.com", True),
        ("user.name@domain.co.uk", True),
        ("test_email@test-domain.org", True),
        ("a@b.com", True),
        ("user123@email.com", True),
        
        # Invalid emails
        ("invalid.email", False),
        ("@example.com", False),
        ("user@", False),
        ("user name@example.com", False),
        ("user@domain", False),
        ("user@.com", False),
        ("user@@example.com", False),
        ("user@example..com", False),
        ("user@-example.com", False),
        ("", False),
        ("user@example.c", False),
    ]
    
    for email, expected in test_emails:
        result = is_valid_email(email)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{email}' -> {result}")
    """