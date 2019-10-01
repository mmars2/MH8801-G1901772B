print('Hello, I am new to python and I would like to share with you 3 things that I have learnt and created so far :') 
print('1. The first shoutout everyone new to python will usually use')
print('2. My personalised greeting to you')
print('3. This program helps you convert celsius to farenheit\n')
print('Which program would you like to explore?')
def programme() :
    while True:    
        chosen = input('Please type 1, 2, 3 or q to quit :')
        if chosen == '1':
            print('Hello, world!\n')
        elif chosen == '2':
            nam = input('May I know what is your name?')
            print('Hi,', nam,', wishing you a great year ahead!\n')
        elif chosen == '3':
            celsiusTemp = input('Please enter temperature in celsius:') 
            fahrenheitTemp = float(celsiusTemp)* 1.8 + 32
            print(celsiusTemp,'degree celsius in fahrenheit is:',round(fahrenheitTemp,1),'\n')
        elif chosen == 'q':
            quit('Thanks for trying and have a nice day!')
        else:
            print('Sorry, the option you have entered is not available.\n')
        print('What other programs would you like to try? The options are as follows:')
        print('1. The first shoutout everyone new to python will usually use')
        print('2. My personalised greeting to you')
        print('3. This program helps you convert celsius to farenheit\n')

programme()