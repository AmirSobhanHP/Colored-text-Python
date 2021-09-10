# install required packages
# pip install termcolor2 
import termcolor2 # import package
word = input("Please enter your word : ") # get input from user
word_colored = termcolor2.colored(word,"cyan") # change your word's color (text or variable, color['red', 'green', 'yellow','blue', 'magenta', 'cyan', 'white'])
print(word_colored)
print("CC BY SA ! created by Amisobhan Hosseinpour")
input("PLease enter key to end... ")