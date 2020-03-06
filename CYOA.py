def intro():
    print("Welcome to Choose Your Own Adventure. The choices you make will affect the story. Choose wisely.")
    name = input("What is your name? ")



def choice1():
    print("You stay on the plane. As the plane takes off, you notice some strange sounds. You convince yourself that everything is okay. You fall asleep on the plane.")
    print("You wake up to the feeling of extreme turbulence. The plane is going down. Do you buckle your seat belt and pray or attempt to hijack the plane and save everyone")
    planeChoice = input("Choose 1 for seatbelt and 2 to hijack the plane: ")
    if (planeChoice == "1") :
        print("The plane continues to go down and the plane crashes. GAME OVER.")
    elif (planeChoice == "2"):
        print ("You run through the aisle and whip open the cock pit door. You find the pilots are both alseep with blow darts in their neck. It was the Russians. You grab the controls and try to figure things out. Somehow the plane starts the pull up. You are going to be okay.")
        print ("Then the flight marshall tackles you and arrests you. The plane crashes. GAME OVER.")  
            
        
def choice2():
   print("You get off the plane and go to get your ticket. Your ticket is a round trip ticket to ANTARCTICA. You get your $5000 and board your plane as the real adventure begins.")
   print("The flight goes smoothly and you land in ANTARCTICA. Once you land there, you are given a choice of where to stay. In an Igloo with eskimos for $500 total or a research facility for $3000.")
   igloo = input("Choose 1 for the igloo and 2 for the research facility: ")
   if (igloo == "1"):
        iggy1()
   elif(igloo =="2"):
        iggy2()
   else:
        print("invalid")
    


def setup():
    print("You are headed to the airport for your dream vacation. A riverrafting trip through the Amazon River over the course of two weeks.")
    print("You go through security and are baording the plane and get to your seat. As you wait for the plane to leave, the flight attendant comes over the PA and announces that the flight is overbooked and that they are offering a free round trip ticket to a mystery location and $5000.")
    flightChoice = input("Choose 1 to stay or 2 to take the ticket: ")
    if (flightChoice == "1"):
        choice1()
    elif (flightChoice == "2"):
        choice2()
    else:
        print("invalid answer")
        

def iggy1():
    print("When you arrive at the igloo, you are greeted with hugs and smiles. The eskimos welcome you into their home and treat you like family. You are given a fur coat and a seat by the fire.")
    print("You get in your sleeping bag for the night and get ready for bed. You fall asleep.")
    print("You are woken up in the middle of the night to a loud noise. The fire is dwindling and no one else is awake. Do you investigate the noise or not? ")
    ab = input("Choose 1 for Yes and 2 for No: ")
    if (ab == "1"):
          a1()
    elif(ab == "2"):
          a2()
    else:
        print("invalid")

def iggy2():
    print("The research facility you stay in is a hub of intelligence and technology. Some of the brightest minds in the World are working here. You aren't sure what they're studying but youre impressed nonetheless.")
    print("You are given the oppurtunity to learn and somewhat participate in what the researchers are studying but it'll cost an extra $1500. Do you Agree? ")
    cd = input("Choose 1 for Yes and 2 for No: ")
    if (cd == "1"):
          r1()
    elif(cd == "2"):
          r2()
    else:
        print("invalid")
            
def r1():
    print("You discover that the research facility is actually a secret international coaltion. The real reason they are researching isn't because of the ice caps.")
    print("The real reason they are there is because there is an alien colony deep underneath the ice. You discover that these aliens have been the source of the recent surge of technological innovation.")

def r2():
    print("You learn nothing and spend the rest of the trip being bored. GAME OVER.")
              
def a1():
    print("You go outside and see a 15 foot tall polar bear. You decide to run as fast as you can to the nearby research facility. The polar bear begins to chase you.")
    print("As you are running away, the polar bear begins to gain on you. It gets you and you die. GAME OVER")

def a2():
    print("You go back to bed and get attacked by a polar bear. GAME OVER.")

intro()
setup()
