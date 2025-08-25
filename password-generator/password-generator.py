import secrets
import string

def generate_password(n_letters=0, n_numbers=0, n_symbols=0, total_length=0):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+"
    
    pass_chars = []

    if total_length > 0:
        # Generate a password with 40% letters, 30% numbers, and 30% symbols
        n_letters = round(total_length * 0.4)
        n_numbers = round(total_length * 0.3)
        n_symbols = total_length - n_letters - n_numbers
    
    # Add random letters
    for _ in range(n_letters):
        pass_chars.append(secrets.choice(letters))
    
    # Add random numbers
    for _ in range(n_numbers):
        pass_chars.append(secrets.choice(numbers))

    # Add random symbols   
    for _ in range(n_symbols):
        pass_chars.append(secrets.choice(symbols))
        
    # Shuffle the password character list
    secrets.SystemRandom().shuffle(pass_chars)
    
    # Convert the password character list to a string
    password = ''.join(pass_chars)

    return password


if __name__ == "__main__":
    print("Welcome to The Password Generator.")

    while True:
        print("There are 2 options:")
        print("1. Enter the total password length.")
        print("2. Specify the number of letters, numbers, and symbols separately.")

        choice = input("Do you want to enter a total length? (y/n) ")
            
        try:
            if choice == 'y':
                total_length = int(input("Enter total password length: "))
                password = generate_password(total_length=total_length)
            else:
                n_letters = int(input("How many letters would you like in your password? "))
                n_numbers = int(input("How many numbers would you like in your password? "))
                n_symbols = int(input("How many symbols would you like in your password? "))
                password = generate_password(n_letters, n_numbers, n_symbols)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        else:
            print("Your password is:", password)

        again = input("Do you want to generate another password? (y/n) ")
        if again == 'n':
            break