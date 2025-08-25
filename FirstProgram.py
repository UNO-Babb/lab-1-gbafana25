#FirstProgram.py
#Name: Gareth Moodley
#Date: 8-25-2025
#Assignment: Lab1
#Purpose: ask a user for their name, calculate birth year

from datetime import datetime

def main():
  print("First Program")
  #Say hello
  print("Hello!")
  
  #Ask for the user's name
  name = input("Hello, what's your name? ")

  #Use the user's name in the program.
  print("Welcome to your first program,", name)


  #Ask the user for their age.
  age = int(input("How old are you? "))

  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  now = datetime.now()
  print("You were born in",str(now.year - age))


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
