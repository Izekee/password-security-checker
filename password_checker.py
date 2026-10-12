import hashlib
import string
from getpass import getpass

import requests


# Common passwords that are easy to guess
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "monkey",
    "football",
    "dragon",
    "abc123",
    "000000",
}


# Simple sequences that are commonly used in passwords
COMMON_SEQUENCES = {
    "1234",
    "2345",
    "3456",
    "4567",
    "5678",
    "6789",
    "abcd",
    "bcde",
    "cdef",
    "qwer",
    "wert",
    "asdf",
    "zxcv",
}


def check_repeated_characters(password):
    """Check for the same character repeated 3 or more times."""
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False


def check_sequences(password):
    """Check for simple sequences commonly used in passwords."""
    password_lower = password.lower()

    for sequence in COMMON_SEQUENCES:
        if sequence in password_lower:
            return True

    return False


def check_breached(password):
    """Return how many times the password appears in known data breaches.

    Uses the Have I Been Pwned "Pwned Passwords" API with k-anonymity:
    only the first 5 characters of the password's SHA-1 hash are sent.
    The password itself never leaves this computer.

    Returns None if the check could not be completed (offline, API down).
    """
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={"Add-Padding": "true"},
            timeout=5,
        )
        response.raise_for_status()
    except requests.RequestException:
        return None

    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0


def check_password(password):
    score = 0
    feedback = []

    # -----------------------------
    # 1. Check password length
    # -----------------------------
    if len(password) >= 12:
        score += 1
        length_check = "PASS"
    else:
        feedback.append("Use at least 12 characters.")
        length_check = "FAIL"

    # -----------------------------
    # 2. Check uppercase letters
    # -----------------------------
    if any(character.isupper() for character in password):
        score += 1
        uppercase_check = "PASS"
    else:
        feedback.append("Add at least one uppercase letter.")
        uppercase_check = "FAIL"

    # -----------------------------
    # 3. Check lowercase letters
    # -----------------------------
    if any(character.islower() for character in password):
        score += 1
        lowercase_check = "PASS"
    else:
        feedback.append("Add at least one lowercase letter.")
        lowercase_check = "FAIL"

    # -----------------------------
    # 4. Check numbers
    # -----------------------------
    if any(character.isdigit() for character in password):
        score += 1
        number_check = "PASS"
    else:
        feedback.append("Add at least one number.")
        number_check = "FAIL"

    # -----------------------------
    # 5. Check special characters
    # -----------------------------
    if any(character in string.punctuation for character in password):
        score += 1
        special_check = "PASS"
    else:
        feedback.append("Add at least one special character.")
        special_check = "FAIL"

    # -----------------------------
    # 6. Check common password
    # -----------------------------
    if password.lower() in COMMON_PASSWORDS:
        common_password = True
        feedback.append(
            "This password is commonly used and may be easy to guess."
        )
    else:
        common_password = False

    # -----------------------------
    # 7. Check repeated characters
    # -----------------------------
    repeated_characters = check_repeated_characters(password)

    if repeated_characters:
        feedback.append(
            "Avoid repeating the same character three or more times."
        )

    # -----------------------------
    # 8. Check simple sequences
    # -----------------------------
    sequence_found = check_sequences(password)

    if sequence_found:
        feedback.append(
            "Avoid simple sequences such as 1234, abcd, qwer, or asdf."
        )

    # -----------------------------
    # Determine password strength
    # -----------------------------
    if common_password:
        strength = "VERY WEAK"
    elif score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    elif repeated_characters or sequence_found:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return (
        score,
        strength,
        feedback,
        common_password,
        repeated_characters,
        sequence_found,
        length_check,
        uppercase_check,
        lowercase_check,
        number_check,
        special_check,
    )


# ==========================================
# PROGRAM TITLE
# ==========================================

print("=" * 55)
print("             PASSWORD SECURITY CHECKER")
print("=" * 55)
print("Educational cybersecurity tool")
print("Use fake/test passwords only.")
print("=" * 55)

# Get password from user (typing is hidden on screen)
password = getpass("\nEnter a test password: ")

# Check for empty input
if not password:
    print("\n⚠ ERROR: You did not enter a password.")
    print("Please run the program again and enter a test password.")

else:
    # Analyze password
    (
        score,
        strength,
        feedback,
        common_password,
        repeated_characters,
        sequence_found,
        length_check,
        uppercase_check,
        lowercase_check,
        number_check,
        special_check,
    ) = check_password(password)

    # ==========================================
    # BREACH CHECK (Have I Been Pwned)
    # ==========================================

    breach_count = None

    # Skip the network call if it's already a known common password
    if not common_password:
        print("\nChecking breach database...")
        breach_count = check_breached(password)

    if breach_count:
        strength = "VERY WEAK"
        feedback.append(
            f"This password appeared in {breach_count:,} known data breaches."
        )

    # ==========================================
    # RESULTS
    # ==========================================

    print("\n" + "=" * 55)
    print("                    RESULTS")
    print("=" * 55)

    print(f"\nPassword length: {len(password)} characters")
    print(f"Security score: {score}/5")
    print(f"Overall strength: {strength}")

    # ==========================================
    # SECURITY CHECKS
    # ==========================================

    print("\nSecurity Checks")
    print("-" * 55)

    print(f"Length:              {length_check}")
    print(f"Uppercase letter:    {uppercase_check}")
    print(f"Lowercase letter:    {lowercase_check}")
    print(f"Number:              {number_check}")
    print(f"Special character:   {special_check}")

    # Common password check
    if common_password:
        print("Common password:     YES")
    else:
        print("Common password:     NO")

    # Repeated character check
    if repeated_characters:
        print("Repeated characters: YES")
    else:
        print("Repeated characters: NO")

    # Sequence check
    if sequence_found:
        print("Simple sequence:     YES")
    else:
        print("Simple sequence:     NO")

    # Breach database check
    if common_password:
        print("Breach database:     SKIPPED (already a common password)")
    elif breach_count is None:
        print("Breach database:     COULD NOT CHECK (offline?)")
    elif breach_count > 0:
        print(f"Breach database:     FOUND ({breach_count:,} times)")
    else:
        print("Breach database:     NOT FOUND")

    # ==========================================
    # RECOMMENDATIONS
    # ==========================================

    print("\nRecommendations")
    print("-" * 55)

    if feedback:
        for item in feedback:
            print(f"- {item}")
    else:
        print("✓ No basic security problems were detected.")

    # ==========================================
    # FINAL MESSAGE
    # ==========================================

    print("\n" + "=" * 55)

    if strength == "VERY WEAK":
        print("⚠ This password has significant weaknesses.")
    elif strength == "WEAK":
        print("⚠ This password could be improved.")
    elif strength == "MODERATE":
        print("! This password has some good characteristics.")
    else:
        print("✓ This password passes the basic security checks.")

    print("=" * 55)
    print("\nNote: This tool provides a basic educational assessment.")
    print("It does not guarantee that a password is uncrackable.")