def choices():
    print("Please note that this isn't anything like the mobile game of the same name.\n Created by Lol Guy for the sparrow assistant by pivinx1\n")
    print("\nChoices a text game by Lol Guy")
    cmd = input("Press any key to continue\n")

    print("Good morning")
    print("You are Dan, he lives alone in a house near a major intersection. He uses a car to get to most places, and he works a 9-5 job.")
    print("Your alarm clock goes off, it's 6:30 am. You get out of bed,")
    cmd = input("Do you eat breakfast or go straight to work?\n")
    if cmd == "Go straight to work":
        print("I'm going to have breakfast, I'd rather eat something than be starving.")
    #no matter what you'll eat breakfast because that's how the game is coded lol
    print("You go to the kitchen and make a breakfast and coffee because Dan has a fixed schedule.")
    print("if you're Dan's schedule is\n -Wake up at 6:30\n -Eat breakfast\n -Go to work\n -Eat lunch at work\n -Finish work and go back home\n -Make dinner\n -Cry yourself to sleep")
    print("After you're done eating you go to the garage,")
    #You are going to have to use your car because you live in a car-centric city
    cmd = input("Do you use your car or ride your bike to work?\n")
    if cmd == "Ride bike to work":
        print("I'm not going to risk getting myself killed.")
    print("Well sorry but you're going to have to use your car because you live in a car-centric city.\n Anyways 50 minutes later you arrive at work because traffic.")
    print("The time is now 9 am, time to get to work")
    sleep(4)
    print("It is now noon")
    cmd = input("Do you go to [insert fast-food restaurant] or eat your own lunch?\n")
    if cmd == "[fast food restaurant]":
        print("I packed my own f**king sandwich")
    #You eat your own lunch, the sandvich you made at your house
    print("Well you packed your own lunch, a nice 'healthy' (bread and meat, yummy) sandvich")
    print("Now it's 12:30 pm, back to work")
    sleep(4)
    print("4 hours and 30 minutes pass, the time is now 5 pm")
    #You're not gonna work overtime, Dan's done all his work
    cmd = input("Do you work overtime or go home?\n")
    if cmd == "overtime":
        print("I'M DONE ALL MY F**KING WORK! \nDan, are you okay? \nI'm not f**king okay, there's a voice in my head that keeps pestering me. \nTake a day off for your mental health, maybe that'll help. \nI'm going to my car.")
    print("You leave your cubicle, go to the underground garage, get in your car, then head home")
    print("Once you arrive home you eat dinner then cry yourself to sleep")
    print("The end")
    #pivin, if you need to fix any code you can :)
