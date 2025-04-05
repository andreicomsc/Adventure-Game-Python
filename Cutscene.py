import time, os

from gameparser import printslow


lecturers = {

    "Kirill":"Sorry this person cannot answer the phone write now, please try call someone else",

    "Jing": "Good Afternoon! Looks like you're running a little late today! Not to worry - head down to Lecture Hall as soon as you can, the students will be there working on their games"

    }
    

def image():

    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣶⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⣿⣾⠟⣛⣻⣿⣶⣤⣤⡴⢾⣿⡿⣿⣿⣟⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣭⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠉⠹⠟⠋⠛⠛⢻⡗⠀⢻⢮⠉⠀⠈⠉⠉⠉⠛⠉⠀⠀⠈⣿⣿⣿⠁⠈⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠋⠛⠆⢠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣀⣀⡰⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠛⠒⠛⠁⠁⠀⠀⠀⠀⢄⠀⠀⠀⠀⠀⠀⠀⢠⣶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⠒⠂⠐⠒⠒⠒⣒⣲⠄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠒⠃⠉⠉⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀⢸⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠉⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣶⢤⠤⠤⠴⢶⣾⡿⠟⠁⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠉⠛⠛⠛⠉⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡀⠀")
    print("⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")






def hall():

    time.sleep(6)
    print ("")
    print("QUICK! The students are waiting for you! Lets get in your car and drive there!")
    print ("")
    print ("...")
    time.sleep(4)
    print ("")
    print("Damn there's a lot of traffic!")
    print ("")
    print ("...")
    time.sleep(4)
    print ("")
    print("Whoaaa, well that was a crazy ride, You've reached! Let's get you in the lecture Hall...")
    print ("...")
    time.sleep(4)
    print("Ah, you bump into the security guard! They want to see some ID")
    print ("")
    time.sleep(1)
    input("press any key to show them your ID")
    print ("")
    
    image()

    print ("")
    print ("Perfect! Security has checked your ID and you're all good to go!")
    print ("")
    print ("Enjoy the rest of your day!")
    print ("")
    print ("THE END.")
    
    
           
           
def start():
    printslow("""You enter into what seems to be an office for a university professor.
The door is titled Kirill Sidorov. This is the evil professor, the one that 
preformed that insane experiement.\n\n""")
    waiter = input("\nPress enter to continue.")
    os.system("cls")

    printslow("""As you step inside you notice a mirror on the right hand wall.
You look into....
You are Kirill?
You are the professor? What?
But you remember nothing.
""")

    waiter = input("\nPress enter to continue.")
    os.system("cls")

    printslow("""You sit down at 'your' chair to think about what you have just found out.
But before you had time to analyse the evil things you have done, you here a knock at the door.
It's a group of students. They have some questions for you.""")


    waiter = input("\nPress enter to continue.")
    os.system("cls")

    printslow("""'Kiril, What's a compiler?""")
    printslow("""You reply, 'A compiler is....' You get cut off with another question.""")
    waiter = input("\nPress enter to continue.")
    os.system("cls")
    printslow("""'Kirill, How do you convert binary to denary?""")
    printslow("""You reply, 'its quite easy, you just have to....' They are too eager and cut you off again""")
    waiter = input("\nPress enter to continue.")
    os.system("cls")
    printslow("""'Kirill, Where is room 4.32?'""")
    printslow("""You begin to panic and break down, 'i[s *p 0n the 4#h f!0or.'""")
    waiter = input("\nPress enter to continue.")
    os.system("cls")
    printslow("""'Kirill, Kirill, Kirll'""")
    printslow("""Rage fills you and you resort to violence, you shout but its inaudidabile, 'S$£%*&£$ @:$£%@£%'""")
    printslow("""The students start screaming in fear""")
    
    waiter = input("\nPress enter to continue.")
    os.system("cls")

    printslow('You wake up.')
    time.sleep(1)
    end_cutscene()





def end_cutscene():

    printslow("RISE AND SHINE! You must of fell alseep in reception!...")
    printslow("...It's already 12pm - Let's have a look at your timetable...")
    waiter = input("\nPress enter to continue.")
    os.system("cls")
    printslow("\nYou had classes from 9-6! YOU'RE LATE")

    printslow("\nThank god it was all a dream. Or was it?")
    waiter = input("\nPress enter to continue.")
    os.system("cls")
    printslow("You lose :D, thanks for playing")
    waiter = input("\nPress enter to continue.")
    exit()
