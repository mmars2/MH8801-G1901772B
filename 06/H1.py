from generatePassword import genPassword

length=int(input('What length of password would you like to generate? Do note the password will be of a minmium length of 4.'))
print(genPassword(length))