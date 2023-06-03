import secrets, string

def token_generator(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == '__main__':
    print(token_generator(64))