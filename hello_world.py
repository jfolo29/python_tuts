



import math

print("Welcome to my small calculator")

playing = input("Do you want to play? ") 
if playing.lower() != "yes":
  quit()

print("Okay let's play :)")

def main():
  FirstNum = input("What is your first number? ")
  SecondNum = input("what is your second number? ")
  sum = int(FirstNum) + int(SecondNum)

  Calculator = input("Do you want to to get the sum of both numbers? ")
  if Calculator.lower() == "yes":
    print("The sum is: ", sum)

  Continue = input("Do you want another try? ") 
  if Continue.lower() == "yes":
    main()
  else:
    print("bye :)")
    quit()

main()



