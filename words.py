#1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a 
#word to uppercase? Ask Python for help on what you can do with strings!

foods = ['corn', 'sode', 'egg', 'bread']

for food in ['corn', 'sode', 'egg', 'bread']:
    print(food.upper())

#2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(foods):
    """ Makes a list of words uppercase"""
    
    for food in foods:
      print(food.upper())
      


#3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

foods = ['corn', 'sode', 'egg', 'bread']

def only_words_with_this_letter(foods):
    """ Prints words that start with the letter E upper case or lower case into lower case words."""
    
    for food in foods:
        if food.startswith('e') or food.startswith('E'):
            print(food.upper())
                

#4.Make your function more general: you should be able to pass in a set of letters, 
#and it only prints words that start with one of those letters.
foods = ['corn', 'sode', 'egg', 'bread']
letters = ['b', 'c', 's']
def general_letter(foods,letters):

    """ Prints words that start with the any letter declared in the function."""
    for food in foods:
        for letter in letters:
            if food.startswith(letter):
                print(food.upper())
                