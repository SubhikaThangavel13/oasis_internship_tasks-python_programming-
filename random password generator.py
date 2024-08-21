import random
import string
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("You need to include at least one type of character (letters, numbers, or symbols).")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("How long should your password be? "))
        if length <= 0:
            raise ValueError("Password length must be a positive number.")
        use_letters = input("Do you want to include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nHere is your password: {password}")
    
    except ValueError as e:
        print(f"Oops! {e}")
if __name__ == "__main__":
    main()
