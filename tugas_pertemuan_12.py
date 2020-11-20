words = ['zero ', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ' , 'ten ' , 'eleven ' , 'twelve ' , 
        'thirteen ' ,'fourteen ' , 'fifteen ' , 'sixteen ' , 'seventeen ' , 'eighteen ' , 'nineteen ']

def said(n):
    if n < 20:
        return words[n]
    elif n >= 1_000_000_000:
        return said(n // 1_000_000_000) + 'billion ' + (said(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return said(n // 1_000_000) + 'million ' + (said(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        return said(n // 1_000) + 'thousand ' + (said(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        return said(n // 100) + 'hundred ' + (said(n % 100) if n % 100 != 0 else '')
    elif n < 30:
        return "twenty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 40:
        return "thirty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 50:
        return "forty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 60:
        return "fifty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 70:
        return "sixty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 80:
        return "seventy " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 90:
        return "eighty " + (said(n % 10) if n % 10 != 0 else '')  
    elif n < 100:
        return "ninety " + (said(n % 10) if n % 10 != 0 else '')  

class RangeNotValid(Exception):
    def __init__(self, msg):
        self.args = msg

import os
while True:
    os.system('cls')
    try:
        print("Number to Words Conversion Program")
        n = int(input('Enter number (up to billions): '))
        if n >= 1_000_000_000_000:
                raise RangeNotValid('Sorry, you can only input up to billions.')
        no_error = True
    except RangeNotValid:
        no_error = False
        print('Sorry, you can only input up to billions.')
    except Exception as e :
        no_error = False
        print('Sorry, you can only input integer data type.')
    finally:
        if no_error:
            print(f'{n:,} = {said(n)}')

    while True:
        choice = input('Do you want to repeat [y/n] ? ').lower()
        if choice in ['y', 'n']:
            break
    
    if choice == 'n':
        print('Thank you for using our program :)')
        break