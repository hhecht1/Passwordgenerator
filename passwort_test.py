import random
import string


def passwort_generator(length):
    character= string.ascii_letters + string.digits + string.punctuation
    passwort=''.join(random.choice(character) for i in range (length))
    return passwort

print(passwort_generator(12))