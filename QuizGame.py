from tkinter.messagebox import YES


print("Welcome to my computer game")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay let's play: )")
score = 0

def main():

    question = input("what does CPU stand for? ")
    if question.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("incorrect!")
    question = input("what does GPU stand for? ")
    if question.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("incorrect!")
    question = input("what does RAM stand for? ")
    if question.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("incorrect!")
    question = input("what does PSU stand for? ")
    if question.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("incorrect!")
    question = input("what does SaHeCo stand for? ")
    if question.lower() == "sacred heart college":
        print("Correct!")
        score += 1 
    else:
        print("incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " +str((score/5)*100) + "%")

    continu = input("do you want to have another try?")
    if continu.lower() == "yes":
        main()
    else:
        print("bye :)")
        quit()



