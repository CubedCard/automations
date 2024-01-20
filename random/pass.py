import random
import string

def generate_password(length=20, uppercase=True, lowercase=True, numbers=True, symbols=True):
    character_types = {
        'uppercase': string.ascii_uppercase if uppercase else '',
        'lowercase': string.ascii_lowercase if lowercase else '',
        'numbers': string.digits if numbers else '',
        'symbols': string.punctuation if symbols else '',
    }

    if not any(character_types.values()):
        raise ValueError("At least one character type should be selected.")

    characters = ''.join(character_types.values())
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
generated_password = generate_password(length=length, uppercase=True, lowercase=True, numbers=True, symbols=True)
print(generated_password)
