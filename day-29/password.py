import random

class Password:
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numbers = '0123456789'
        self.symbols = '!#$%&()*+'

    def generate(self, nr_letters=8, nr_symbols=2, nr_numbers=2):
        """Generates a random password with the specified number of letters, symbols, and numbers."""
        password_list = []

        # Add random letters
        password_list.extend(random.choices(self.letters, k=nr_letters))

        # Add random symbols
        password_list.extend(random.choices(self.symbols, k=nr_symbols))

        # Add random numbers
        password_list.extend(random.choices(self.numbers, k=nr_numbers))

        # Shuffle the password list
        random.shuffle(password_list)

        # Combine the list into a string
        return ''.join(password_list)

# Example usage
# password_generator = Password()
# password = password_generator.generate(nr_letters=random.randint(8, 10), nr_symbols=random.randint(2, 4), nr_numbers=random.randint(2, 4))
# print(f"Your password is: {password}")