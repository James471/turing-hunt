import re
from GameObjects import Location, Collectable, Pocket
from GameEngine import screen_clear, timed_print, close_game, opensite, im_show, copyFile
import random
import networkx as nx
import matplotlib.pyplot as plt

"""Build all the locations"""

Main_Gate = Location(
    "Main Gate",
    "A Nice Big Arch!\n"
    "Students are coming back from their friday night party at 12am...")
East_Gate = Location(
    "East Gate",
    "A train passes by...")
T_Point = Location(
    "T point",
    "Hunh, I can see something weird in this mirror, Oh thats just me...")
Admin = Location(
    "Admin",
    "You enter the lovely automatic sliding doors, a cool blast of AC...\n"
    "You see the IISER-M model and remember that 4 more hostels need to be built.\n"
    " But there's no funds...")
CAF = Location(
    "CAF",
    "Very sensitive machines which may be disturbed by students "
    "eating in the cafeteria\n"
    "You hear someone shouting at someone else in the distance, "
    "but do not record it, for it would be a violation of privacy")
Library = Location("Library", "So quiet...")
Computer_Centre = Location("Computer Centre",
                           "A few computers have not been turned off")
Health_Center = Location("Health Center", "A very dark and scary place...")

Outside_LHC = Location("Outside LHC", "The LHC may be locked at this time...")
LHC = Location("LHC", "Ah the good old LHC...")
LH1 = Location('LH1', "There's a BIG flowchart on the board!")
LH2 = Location('LH2', "There are so many computers.")
LH3 = Location(
    'LH3',
    "You can still hear the debates that happened here a few hours ago.")
LH4 = Location('LH4', "Nothing interesting")
LH5 = Location('LH5', "Someone has left their bottle outside.")
LH6 = Location(
    'LH6',
    'Someone forgot their umbrella. Some differential equations are written on the board')
LH7 = Location(
    'LH7',
    "The watchman shoos you away. The stage is too precious to even repair...")

Rotunda = Location(
    'Rotunda',
    'You see a gang of MS19 making a lot of noise...')
H5 = Location(
    'H5',
    'Caretaker\'s Office is locked. Why is it always locked? Hmm...\n'
    "It's dark outside, you may need a torch")
H5_SR = Location('H5 SR', "Back to the start...")
H6 = Location('H6', 'Hos... The rest of the banner is torn...\n'
              "It's dark outside, you may need a torch")
H6_SR = Location(
    'H6 SR',
    'You see a couple snogging. They see you. It\'s so awkward')
H7 = Location('H7', 'Someone is taking their clothes to wash...\n'
              "It's dark outside, you may need a torch")
H7_SR = Location(
    'H7 SR',
    'Those Dance Club people are still dancing in the Dance Room')
H8 = Location(
    'H8',
    'Some MS18 kids are loitering around...\n'
    "It's dark outside, you may need a torch")
H8_SR = Location(
    'H8 SR',
    'The ACs are off, its so hot...\nOh wait, they are on... '
    'Why is it so hot then? Oh the ACs aren\'t working')

Stadium = Location('Stadium', 'A lapwing shouts in the distance...')
BB_Court = Location('BB Court', 'Why the fuck do lapwings make so much noise?')
VH = Location(
    'VH',
    'Dollar building. The terrace may be locked')
VH_Terrace = Location(
    'VH Terrace',
    'Haaah! Nice and windy. You see a couple of friends talking about the'
    'struggles of life...')
Shopping_Complex = Location(
    'Shopping Complex',
    'It\'s so empty and quiet. Aunty must have gone home...')

AB1 = Location(
    'AB1',
    'You buy a nice coffee for 10rs, coz neither of you have change')
AB1_1F = Location('AB1 1F', 'People playing Badminton...')
AB1_2F = Location('AB1 2F', 'Eerily dark and quiet')
AB1_3F = Location(
    'AB1 3F',
    'One lone MS13 is studying there. Why haven\'t they graduated yet?')
AB1_4F = Location('AB1 4F', 'Eerily dark and quiet')
EBL_Lab = Location(
    'EBL',
    'So many dead flies in flasks.\n It\'s like a horror movie')
AB1_5F = Location(
    'AB1 5F',
    'Eerily dark and quiet, but there\'s some news article about '
    'Plastic Firecrackers...')
AB2 = Location(
    'AB2',
    'ERROR! The app devs didn\'t care enough to make 2 AB\'s.\n'
    'There\'s nothing here. Go away, shoo.')
Gazebo = Location(
    'Gazebo',
    'There\'s some MS17 party going on there. Oh god so much cake wasted.\n'
    'Talking about wasting stuff, they\'re fixing the covers...')
Behind_AB = Location(
    'Behind AB',
    'Aww! 3 cute puppies run up to you.\n'
    r"""
           ^_         __         __
      (___/ "`;  \___()"`;  /___()"`;
      /,    /`   /,    /`   /,    /`
      \\"--\\   //"--//    \\"--\\

    """)
Animal_Facility = Location(
    'Animal Facility',
    'The everlasting humm of the machines...\n' +
    'What are these machines? What happens here? SO MANY QUESTIONS!')
Room69 = Location(
    'Room No. 69',
    'Why is it numbered 69 if it is the only room here?\n' +
    'I have found this place unlocked for the first time. Should explore it a bit.')

"""Connect the Locations to make a traversable map"""
Main_Gate.append_locations([Behind_AB, Admin, CAF])
East_Gate.append_locations([Animal_Facility, Behind_AB])
T_Point.append_locations([CAF, Outside_LHC, Admin, Health_Center])
Health_Center.append_locations([T_Point, BB_Court])
Admin.append_locations([Main_Gate, CAF, T_Point])
CAF.append_locations([Admin, Main_Gate, T_Point])
Library.append_locations([Outside_LHC, Gazebo, Computer_Centre])
Computer_Centre.append_locations([Library])

Outside_LHC.append_locations([T_Point, Library, Rotunda, Animal_Facility])
LHC.append_locations([LH1, LH2, LH3, LH4, LH5, LH6, LH7, Outside_LHC])
LH1.append_locations([LHC])
LH2.append_locations([LHC])
LH3.append_locations([LHC])
LH4.append_locations([LHC])
LH5.append_locations([LHC])
LH6.append_locations([LHC])
LH7.append_locations([LHC])

Rotunda.append_locations([Outside_LHC, H5, H6, H7, H8, Stadium])
H5.append_locations([H5_SR])
H6.append_locations([Rotunda, H6_SR])
H7.append_locations([Rotunda, H7_SR])
H8.append_locations([Rotunda, H8_SR])
H5_SR.append_locations([H5])
H6_SR.append_locations([H6])
H7_SR.append_locations([H7])
H8_SR.append_locations([H8])

Stadium.append_locations([Rotunda, BB_Court, Shopping_Complex])
BB_Court.append_locations([Health_Center, Stadium])
Shopping_Complex.append_locations([Stadium, VH])
VH.append_locations([Shopping_Complex])
VH_Terrace.append_locations([VH])

AB1.append_locations([Gazebo, AB2, Behind_AB, AB1_1F])
AB1_1F.append_locations([AB1, AB1_2F])
AB1_2F.append_locations([AB1_1F, AB1_3F])
AB1_3F.append_locations([AB1_2F, AB1_4F])
AB1_4F.append_locations([AB1_3F, AB1_5F, EBL_Lab])
EBL_Lab.append_locations([AB1_4F])
AB1_5F.append_locations([AB1_4F])
AB2.append_locations([Gazebo, Behind_AB, AB1])
Gazebo.append_locations([Library, AB1, AB2, Behind_AB])
Behind_AB.append_locations([Main_Gate, East_Gate, AB1, AB2, Gazebo])
Animal_Facility.append_locations([Outside_LHC, East_Gate, ])
Room69.append_locations([Animal_Facility])


"""Build Actual clues"""

def clue8Action():
    print("Is half the year over already?!")
    im_show("calender.jpg")
    ans = int(input("Enter the correct year: "))
    if ans == 2036:
        return True
    return False

clue8 = Collectable(
    "An unusually clean sheet of paper",
    "Taped to the pillar, above the wash basin" ,
    "Seems kinda out of place between all these Melody chocolate posters from 2007" ,
    hidden=False,
    action=clue8Action,
    nextnotes=None,
    onComplete="Congratulations! You have successfully reached the end of this treasure hunt\n"
               "You can go back to dying of boredom now. Bye.", #something else
    onFail="Tsk.Tsk. So close yet so far. Try again.")


def clue7Action():
    print("There is a file. Save it in your PC.")
    a = input("Would you like to proceed?[Y/N]")
    if(a == "Y"):
        _ = copyFile("image.jpg")
    b = input("Enter the number if you have found it or press N to go back.")
    if(b == "690"):
        Pocket.append("Note - Truly, 69 is an important number")
        Animal_Facility.append_locations([Room69])
        return True
    return False


clue7 = Collectable(
    "Found a USB drive",
    "Hanging from the ceiling by means of a thread!\n"
    "Either the developer was too sleepy to think of anything better "
    "or this is a wierd place.",
    "Should plug it in my pc to check what it is",
    hidden=False,
    action=clue7Action,
    nextnotes=[clue8],
    onComplete="That was some smart work! Truly 69 is an important number!",
    onFail="What's the first thing you do when you don't know what a file is?")


def clue6Action():
    print("""
            The quest is to find the direction of your life...\n
            Two roads... first towards the accelerator and second towards jordon\n
            And let your octaves fill the keanu reeves movie\n
            Apply some contrast of free will and maybe lose the negativity ...\n
            You should be good to go now\n
            """)

    ans = int(input("Enter your password: "))
    if ans == 22:
        Pocket.append(
            "Clue - H-ate me or love me, you need to Study with me")
        Pocket.append("Key to VH Terrace")
        VH.append_locations([VH_Terrace])
        return True
    return False


clue6 = Collectable(
    "An old box",
    "between H6 & H8",
    "It has a paper stuck on it...\n"
    "Man these treasure hunt people need to stop dipping paper in coffee to make it seem old..\n"
    "There's also a number lock with two digits!\n",
    hidden=True,
    action=clue6Action,
    nextnotes=None,
    onComplete="The box clicked open! Let's see what's inside."
    "A key to VH Terrace and a Note that says-\n"
    "H-ate me or love me, you need to Study with me",
    onFail="The box didn't open.\n"
    "Hehe seems like you're directionally challenged :)\n"
    "Look at it from a different perspective maybe")


def clue5Action():
    i = 0
    question_prompt = ["Cell's leader says 'Carry on!' suspiciously...",
                       "Is the Spanish Crown alive?", "Hiding in a plaza having a handicap",
                       "Chris, who left the hotel, heads the Public Relations Forum at Caribou Biosciences"]
    answers = ["KARYON", "CORONAVIRUS", "ZAHAVI", "CRISPR"]
    while i < len(question_prompt):
        print(question_prompt[i])
        ans = input("Enter your answer: ")
        if ans.upper() == answers[i]:
            i += 1
        else:
            return False
    Pocket.append("Bio Pop quiz answer sheet - Should show friends in Rotunda")
    return True


clue5 = Collectable(
    "Bio Pop Quiz",
    "tucked inside the bottle...?",
    "Why would you do that?\n"
    "A small sheet with a few questions (that will definitely be counted for your consolidated grades :-))",
    True,
    clue5Action,
    nextnotes=[clue6],
    onComplete="Yay!! You answered everything correctly!\n"
    "*happy biologist noises*\n"
    "Maybe you should go tell your friends in Rotunda",
    onFail="OOPS. Looks like you'll need to start all over again")


def clue4Action():
    if dst := copyFile("mutations.pdf"):
        Pocket.append("mutations.pdf in " + dst)
        return True
    return False


clue4 = Collectable(
    "BIO211 experiment draft",
    "in the dustbin",
    "Maybe this holds some mysteries to the next location?",
    hidden=True,
    action=clue4Action,
    nextnotes=[clue5],
    onComplete="Read the copied file, the secret lies within",
    onFail="File copy error, retry")


def clue3Action():
    print("PENALTY at 45 degrees")
    im_show("cube.jpg")
    print("Message: C.Amjg md eclcrgaq")  # change this please
    a = input("What does that mean? ")
    if a == "E.Coli of genetics":  # change this please
        Pocket.append("Clue - E.Coli of genetics")
        return True
    return False


clue3 = Collectable(  # put the clue in lhc rn, change it to anywhere
    "Poster",
    "on the softboard",
    "Its the poster of the Cubing competition held in college some time back",
    True,  # hidden false to check
    clue3Action,
    nextnotes=[clue4],
    onComplete="Hmm? Is that important?",
    onFail="Just search the net man")


def clue2Action():
    opensite("clue2.html")
    a = input("What's the password? ")
    if a == "acceptme":
        Pocket.append("Clue - Large Hadron Collider")
        return True
    return False


clue2 = Collectable(
    "Quantum Computer",
    "in the BIG BIG hall",
    "Another webpage on the way, on a quantum computer!\n"
    "They used a qunatum computer for opening a webpage?\n"
    "Perfect utilization of a non-existent resource",
    True,
    clue2Action,
    nextnotes=[clue3],  # made clue 3 next
    onComplete="Yeah, this was a joke. Now head to the Large Hadron Collider..?",
    onFail="Noooo! This one is dumb too.")


def clue1Action():
    opensite('clue1.html')
    a = input("What's the key? ")
    if a == "TUr!ng":
        Pocket.append("Clue - Costly Machines, easy clues...")
        return True
    return False


clue1 = Collectable(
    "Tablet",
    "on the Table",
    "You will be led to a webpage. Solve the clue, go to the next",
    hidden=False,
    action=clue1Action,
    nextnotes=[clue2],
    onComplete="Costly Machines, easy clues...",
    onFail="No, it's the first question. It's dumber than you think!")


def lhckey_action():
    if input("Pick it?[Y N] ") == "Y":
        Outside_LHC.append_locations([LHC])
        Pocket.append("LHC Key")
        return True
    return False


lhckey = Collectable(
    "LHC Key",
    "hanging by the security",
    "It looks like a normal key. Maybe you can finally see what's inside LHC?",
    hidden=False,
    action=lhckey_action,
    onComplete="Now get out of here before the security guard comes back",
    onFail="There was a nice art exhibition in LHC I heard?")


""" Build FLUFF """
hostel_cctv = Collectable(
    "Notice",
    "on the Soft Board",
    """
    ========================================
    |                                      |
    |   YOU ARE UNDER CCTV SURVIELLENCE!   |
    |                                      |
    ========================================
    """)


def fake_clue_action():
    print("The password is 5")  # some message
    return input("What's the password? ") == "5"  # some prompt


fake_clue = Collectable(
    "Fake Clue",
    "under some table",  # some specific place
    "This is a test clue",  # message of a clue
    False,  # Not hidden
    fake_clue_action,  # action object
    [hostel_cctv],  # next note
    "Yay! Look for a treat in the Hostels",
    "Noo, you dumb?")


def biswas_car_action():
    global here
    choice: Location = random.choice(
        [Behind_AB, East_Gate, Animal_Facility, LHC, BB_Court, Stadium, Shopping_Complex])
    print("You followed the car and ended up in " + choice.name + "!")
    here = choice
    return False


biswas_car = Collectable(
    "A Red sedan",
    "coming from Animal Facility road",
    "It's approaching almost quasistatically...\n"
    "Why would someone be driving around at midnight?! This is pretty shady."
    "Probably not important. It's not like they're going to run over anybody.\nRight?\n\nRIGHT?",
    hidden=False,
    action=biswas_car_action,
    onComplete="Unreachable. Report to devs",
    onFail="This had better be worth-- \n WAIT! THE DRIVER IS ASLEEP?! *facepalm*")


stadium_test = Collectable(
    name="Rocket Pad",
    spot="in the stadium",
    desc="Lets fly the rocket.\n"
    "It went so high that you can't even see it!!!\n\n\n"
    "Oh no! It's falling back! RUNNN!",)


def printer_3d_action():
    print("Printer shows a message 'Please input the blueprint'")
    print("You should wait for the MS19 kids to finish...\n\nOr you could just print the blueprints now...")
    if input("Do you want to print the blueprint? [Y N] ") == "Y":
        Pocket.append("3D Printed Rocket")
        return True
    return False


printer_3d = Collectable(
    name="a 3D printer",
    spot="outside physics lab",
    desc="You go near the 3D printer and see a bunch of MS19 students sleeping around it.\n"
    "\n\nThey are probably tired from waiting their turn at the printer.",
    hidden=True,
    action=printer_3d_action,
    nextnotes=[stadium_test],
    onComplete="The Printer started making weird noises.\n\n\n"
    "You got a 3d printed rocket!\n"
    "Better get out of here before the MS19 kids wake up.",
    onFail="Lets get outta here")


def samrat_inno_action():
    im_show("rocket.jpg")
    print("Maybe I can 3D print this and see if it works")
    if input("Do you want to steal - no, borrow - this? [Y N] ") == "Y":
        Pocket.append("Rocket.jpg")
        return True
    return False


samrat_inno = Collectable(
    name="a Blueprint",
    spot="on the table",
    desc="Innovation #42054....\n\n",
    hidden=False,
    action=samrat_inno_action,
    nextnotes=[printer_3d],
    onComplete="We will have to find a 3D printer...",
    onFail="Nope, it's someone else's property")


def art_competition_action():
    im_show("art1.jpg")
    im_show("art2.jpg")
    im_show("art3.jpg")
    return False


art_competition = Collectable(
    name="multiple art pieces",
    spot="on soft boards",
    desc="There was an art competition held a few days ago.\n"
    "These are some of the beautiful paintings some people have made!",
    hidden=False,
    action=art_competition_action,
    onComplete="Unreachable. Report to devs",
    onFail="Damn! Those were so pretty! I wish I could make things like that")


def room69_action():
    im_show('69.jpg')
    Pocket.append("Clue - Go to Shopping Complex")
    print("Let's take a picture of this.")
    a = input("Do you want to continue[Y/N]")
    if(a == "Y"):
        _ = copyFile("69.jpg")
    return False


room69poster = Collectable(
    name='A lot of cult articles',
    spot='everywhere, even on the ceiling',
    desc='There is a poster on the wall. Should read it.',
    hidden=False,
    action=room69_action,
    onFail="Those are some weird things...\n"
    "I'm hungry now... I should check if Shopping Complex is open",
    onComplete="Unreachable. Report to devs.")


def torch_action():
    print("You turn it on and its very bright!\n")
    if input("Do you want to take it [Y N]? ") == "Y":
        H5.append_locations([Rotunda])
        Pocket.append("A red Torch")
        return True
    return False


torch = Collectable(
    "Torch",
    "on the table",
    "It's a nice red color.",
    action=torch_action,
    hidden=False,
    onComplete="You can now see in the dark and outside!",
    onFail="You should really take it...")


def mmystery_board_action():
    im_show("board.jpg")
    return False


mmystery_board = Collectable(
    name="flowchart",
    spot="on the board",
    desc="These Murder Mystery people are out of their mind.",
    hidden=False,
    action=mmystery_board_action,
    onComplete="Unreachable. Report to devs",
    onFail=""
)


def mmystery_poster_action():
    im_show("mmystery.jpg")
    return False


mmystery_poster = Collectable(
    name="poster for murder mystery",
    spot="on the table",
    desc="There's a sign under the poster. '- Bhavneet Singh'",
    hidden=False,
    action=mmystery_poster_action,
    onComplete="Unreachable. Report to devs",
    onFail="This guy can make nice posters!"
)
"""Add Notes to Locations"""

Computer_Centre.append_collectable([clue1])
CAF.append_collectable([clue2])
EBL_Lab.append_collectable([clue4])
LHC.append_collectable([art_competition, clue3])
LH5.append_collectable([clue5])
Rotunda.append_collectable([clue6])
H8_SR.append_collectable([clue7])
Shopping_Complex.append_collectable([clue8])

H5.append_collectable([hostel_cctv])
H6.append_collectable([hostel_cctv])
H7.append_collectable([hostel_cctv])
H8.append_collectable([hostel_cctv])

AB1_3F.append_collectable([printer_3d])
AB1_5F.append_collectable([samrat_inno])
Stadium.append_collectable([stadium_test])

Admin.append_collectable([lhckey])
H5_SR.append_collectable([torch])
T_Point.append_collectable([biswas_car])
Room69.append_collectable([room69poster])


def makemap(root):
    g: nx.DiGraph = nx.DiGraph()

    def makenodes(root, l):
        if root not in l:
            l.append(root)
            for loc2 in root.locations:
                g.add_edge(root.name, loc2.name)
                makenodes(loc2, l)
    makenodes(root, [])
    nx.draw_kamada_kawai(
        g,
        with_labels=True,
        node_size=750,
        font_size=7,
        width=2,
        edge_color='#6B6B6B')
    plt.show()


hello_banner = '''Welcome to the Virtual Treasure Hunt!
The Treasure Hunt will go on until you finish it. The first person to finish will win.
This is an individual game, but you can always team up with someone else.
But remember that they can hide things from you and win themselves.
You can use the internet.
Please remember that if you exit from this app (by pressing the X or by
shutting down your computer), you will HAVE to restart.
You can minimize this safely, however.
We suggest that you also keep a notepad window open to note down information.

Some clues may seem too technical, but they're generally straight forward.
Just search the internet. Clues may be from
- HTML and VERY SIMPLE Javascript
- Python. If you know what loops are, you are good to go
- Easy Science or math puzzles
- Some Science Trivia

USE THE INTERNET!

Go forth and do your best!'''

print(hello_banner)
input("Press Enter to start")

screen_clear()
print("This is a sys test. Report to devs if any errors are shown.")
input("Enter to continue:")
makemap(Rotunda)
im_show("rocket.jpg")
copyFile("mutations.pdf")

here = H5_SR
while True:
    screen_clear()
    msg = ""
    print(here)
    print("\n\n")
    print("If you want to search around, type search or ls")
    print("If you want to view map, type map")
    print("If you want to view pocket, type pocket")
    print("If you want to go somewhere else, "
          "type goto _location_ or cd _location_")
    print("If you are debugging and want to exit, type exit. "
          "Remove before publishing to prevent accidental closing")

    inp = input("Your choice: ")
    if re.search(r"^(search|ls)$", inp):
        msg = here.search()
    elif match_obj := re.search(r"^(goto|cd) .*", inp):
        new_loc = inp[len(match_obj.group(1)) + 1:]
        msg, here = here.goto(new_loc)
    elif re.search(r"^map$", inp):
        makemap(here)
    elif re.search(r"^pocket$", inp):
        Pocket.show()
    elif re.search(r"^exit", inp):
        close_game()
    else:
        msg = "Invalid Input"
    if (msg):
        timed_print(msg, 0)
