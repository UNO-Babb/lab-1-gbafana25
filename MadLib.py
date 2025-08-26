#MadLib.py
#Name: Gareth Moodley
#Date: 8-25-2025
#Assignment: MadLib
#Purpose: Create a mad libs style game that accepts user input and outputs as a story

#Source(s): https://www.thepaintedturtle.org/sites/main/files/file-attachments/mad_libs.pdf, My Stay at the Hospital

def main():
  print("Madlib")
  print("Type a word that falls into the prompted category (noun, adjective, number, etc.)")
  #Ask user for words
  num1 = input("Number: ")
  time1 = input("Measure of time: ")
  transport1 = input("Mode of transport: ")
  adj1 = input("Adjective: ")
  adj2 = input("Adjective: ")
  noun1 = input("Noun (plural): ")
  color1 = input("Color: ")
  bodypart1 = input("Body part: ")
  verb = input("Verb (3rd person sing.): ")
  num2 = input("Number: ")
  noun2 = input("Noun (sing./plural depending on last number): ")
  noun3 = input("Noun (plural): ")
  bodypart2 = input("Body part (plural): ")
  verb2 = input("Verb: ")
  noun4 = input("Noun: ")

  #Print the story with the user supplied words.
  print("It was about", num1, time1, "ago when I came to the hospital in a",transport1+".")
  print("The hospital is a/an", adj1, "place and there are a lot of", adj2, noun1,"here.")
  print("There are nurses who have",color1,bodypart1+".")
  print("If someone wants to come into my room they have to",verb,"first.")
  print("I have decorated my room with",num2,noun2+".")
  print("Today a doctor came into my room and they were wearing",noun3,"on their",bodypart2+".")
  print("I heard that all the doctors",verb2,noun4,"for breakfast.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
