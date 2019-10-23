def genPassword(n):
    import string
    import random
    symbol = random.choice(string.punctuation)
    lowercase = random.choice(string.ascii_lowercase) 
    uppercase = random.choice(string.ascii_uppercase) 
    digits = random.choice(string.digits)
    generatePassword = symbol + lowercase + uppercase + digits
    for i in range(n-4):
        total = random.choice(string.ascii_letters + string.digits + string.punctuation)
        generatePassword+= ''.join(random.choice(total))
    return generatePassword

if __name__ == "__main__" : 
    print(genPassword(12))