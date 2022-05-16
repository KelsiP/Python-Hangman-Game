#because we will be picking a random word from a list, we need to import random
import random

#holds all the superheros in a list
superheros=['spiderman','ironman','hulk','antman','thor','captainamerica','blackwidow']

#stores all the random words that are going to be used in this game
word=['school','work','shopping','vehicle','television','mirror','painting','lamp']

#rules of the game
print('RULES: This is a guessing game. You have 15 tries to guess the word or superhero. There are no spaces in the word/superhero.  \n')

#more rules 
print('IMPORTANT: When you are ready to guess the word, please type "stop" in the guess and you will be prompted to guess the word. Enter your guess of the superhero as a whole, without any spaces. Enter "hint" to get a hint. \n')


#asks user how many times they would like to play
play=int(input('How many times do you want to play? '))

#user choses if they want to guess superheros or random words
category=input('\n Choose between superheros and words. Enter "S" for superheros or "W" for words: ',)
category=category.upper()  #allows code to not be case sensitive 


def category_superheros():
  count=0 #counts how many times the user guesses 
  won=False  #intial win is false as the user has not played yet
  srandom=random.choice(superheros)  #selects a random superhero from the list
  letter_placement = ((len(srandom))*('_')) #blank spaces for the amount of letters in the word
  print('\n The superhero has',letter_placement,'letters')  #prints blank spaces for the amount of letters in the word
  while count<15:  #user gets 15 tries, the loop runs for the 15 tries the user gets
    guess=input('\n Enter letter: ')  #user guesses the letter
    guess=guess.lower()  #allows code to not be case sensitive 
    count+=1 #count increases for each letter the user guesses
    print('You have', 15-count,'tries left')  #prints how many tries the user has left
    for i in range(len(srandom)):  #loop runs for the length of the letters in superhero
      if guess==srandom[i]:  #if the guess is at the index of the superhero
        letter_placement = letter_placement[:i] + guess + letter_placement[i+1:]  #replaces the blank if the user guess that letter 
    print(letter_placement) #the letter replaces the correct blank space in the word    
    if "_" not in letter_placement:  #if user guess all the letters, and there are no more blanks, they win
      won=True #won is true
      break
    if (guess.upper())=='STOP': #ensures code is not case sensitive, user inpute stop
      scramble=input('\n Guess the superhero: ') #if user enters stop, they can guess the word
      if (scramble.lower())==srandom: #if user guesses correct:
        won=True  #won will become true as they win
        break
      else:  #else win stays false as they lost
        won=False
        break
    if (guess.upper())=='HINT':  #user enters hint to get a hint
      print('\n Hint is: ',srandom)  #provides user a hint
  if won==True:  #if win is true, it prints that the user has won
    print('\n You Won')
  else:  #if win is false, it prints that the user has lost
    print('\n You Lost')


#this code is same to the code for def category_word(). 
def category_word():
  count=0  #counts how many times the user guesses 
  won=False  #intial win is false as the user has not played yet
  wrandom=random.choice(word)  #selects a random superhero from the list
  letter_placement = ((len(wrandom))*('_'))  #blank spaces for the amount of letters in the word
  print('\n The word has',letter_placement,'letters')  #prints blank spaces for the amount of letters in the word
  while count<15:  #user gets 15 tries, the loop runs for the 15 tries the user gets
    guess=input('\n Enter letter: ')  #user guesses a letter
    guess=guess.lower()  #allows code to not be case sensitive 
    count+=1  #count increases for each letter the user guesses
    print('You have', 15-count,'tries left')  #prints how many tries the user has left
    for i in range(len(wrandom)):  #loop runs for the length of the letters in the word
      if guess==wrandom[i]:   #if the guess is at the index of the superhero
        letter_placement = letter_placement[:i] + guess +letter_placement[i+1:]  #replaces the blank if the user guess that letter 
    print(letter_placement)  #the letter replaces the correct blank space in the word    
    if "_" not in letter_placement:  #if user guess all the letters, and there are no more blanks, they win
      won=True  #won is true
      break     
    if (guess.upper())=='STOP':   #ensures code is not case sensitive, user inpute stop
      scramble=input('\n Guess the word: ')  #if user enters stop, they can guess the word
      if (scramble.lower())==wrandom:  #if user guesses correct:
        won=True  #won will become true as they win
        break
      else:   #else win stays false as they lost
        won=False
        break
    if (guess.upper())=='HINT':  #user enters hint to get a hint
      print('\n Hint is: ',wrandom)  #provides user a hint
  if won==True:  #if win is true, it prints that the user has won
    print('\n You Won')
  else:  #if win is false, it prints that the user has lost
    print('\n You Lost')



if (category!='S') and (category!='W'):
 print('You did not choose a category. Please rerun the code and enter "S" for superheros or "W" for words.')#if user doesn't enter S or W, this message will pop up. 
else:  #is the user enter s or w, the code will run
  for playing in range(0,play):  #the user will play how many times they want to
    print('\n Round',playing+1)
    if (category.upper())=='S':  #ensures the code will work for both upper and lower case inputs. if user enter s, they want to play superheros
      category_superheros()  #runs the superheros function
    else:  #if user enter w, they want to play words
      category_word()  #runs the words function
