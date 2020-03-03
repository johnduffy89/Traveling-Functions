def intro():
    print("Welcome to Choose Your Own Adventure. The choices you make will affect the story. Choose wisely.")
    name = input("What is your name?")


def choice1():
    print("You stay on the plane. As the plane takes off, you notice some strange sounds. You convince yourself that everything is okay. You fall asleep on the plane.")
    print("You wake up to the feeling of extreme turbulence. The plane is going down. Do you buckle your seat belt and pray or attempt to hijack the plane and save everyone")
    planeChoice = input("Choose 1 for seatbelt and 2 to hijack the plane")
    if(planeChoice == 1)
            print("The plane continues to go down and the plane crashes. GAME OVER.")
            print ("You run through the aisle and whip open the cock pit door. You find the pilots are both alseep with blow darts in their neck. It was the Russians. You grab the controls and try to figure things out. Somehow the plane starts the pull up. You are going to be okay.")
            print ("Then the flight marshall tackles you and arrests you. The plane crashes. GAME OVER.
        



def setup():
    print("You are headed to the airport for your dream vacation. A riverrafting trip through the Amazon River over the course of two weeks.")
    print("You go through security and are baording the plane and get to your seat. As you wait for the plane to leave, the flight attendant comes over the PA and announces that the flight is overbooked and htat they are offering a free round trip ticket to a mystery location and $5000.")
    flightChoice = input("Choose 1 to stay or 2 to take the ticket")
    if(flightChoice == 1)
        choice1()
    elif(flightChoice == 2)
        choice2()
    else
        print("invalid answer")
        
        

intro()
setup()
