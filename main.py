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
    "You enter the lovely automatic sliding doors, a cool blast of AC...\n" +
    "You see the IISER-M model and remember that 4 more hostels need"
    "to be built. But there's no funds...")
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

LHC = Location("LHC", "Ah the good old LHC...")
LH1 = Location('LH1', "Locked...")
LH2 = Location('LH2', "Locked...")
LH3 = Location('LH3', "Locked...")
LH4 = Location('LH4', "Locked...")
LH5 = Location('LH5', "Someone has left their bottle outside. Locked...")
LH6 = Location('LH6', "Someone forgot their unbrella. Locked...")
LH7 = Location(
    'LH7',
    "The watchman shoos you away. The stage is too precious to even repair...")


Rotunda = Location(
    'Rotunda',
    'You see a gang of MS19 making a lot of noise...')
H5 = Location(
    'H5',
    'Caretaker\'s Office is locked. Why is it always locked? Hmm...')
H5_SR = Location('H5 SR', "Back to the start...")
H6 = Location('H6', 'Hos... The rest of the banner is torn...')
H6_SR = Location(
    'H6 SR',
    'You see a couple snogging. They see you. It\'s so awkward')
H7 = Location('H7', 'Someone is taking their clothes to wash...')
H7_SR = Location(
    'H7 SR',
    'Those Dance Club people are still dancing in the Dance Room')
H8 = Location(
    'H8',
    'Some MS18 kids are loitering around...')
H8_SR = Location(
    'H8 SR',
    'The ACs are off, its so hot...\nOh wait, they are on... '
    'Why is it so hot then? Oh the ACs aren\'t working')

Stadium = Location('Stadium', 'A lapwing shouts in the distance...')
BB_Court = Location('BB Court', 'Why the fuck do lapwings make so much noise?')
VH = Location(
    'VH',
    'Dollar building. You see some... WHY THE FUCK ARE LAPWINGS EVERYWHERE?')
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
    'ERROR! The app devs didn\'t care enough to make 2 AB\'s.'
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

"""Connect the Locations to make a traversable map"""
Main_Gate.append_locations([Behind_AB, Admin, CAF])
East_Gate.append_locations([Animal_Facility, Behind_AB])
T_Point.append_locations([CAF, LHC, Admin, Health_Center])
Health_Center.append_locations([T_Point, BB_Court])
Admin.append_locations([Library, Main_Gate, CAF, T_Point])
CAF.append_locations([Admin, Main_Gate, T_Point])
Library.append_locations([Admin, LHC, Gazebo, Computer_Centre])
Computer_Centre.append_locations([Library])

LHC.append_locations([T_Point, Library, Rotunda, LH1,
                      LH2, LH3, LH4, LH5, LH6, LH7])
LH1.append_locations([LHC])
LH2.append_locations([LHC])
LH3.append_locations([LHC])
LH4.append_locations([LHC])
LH5.append_locations([LHC])
LH6.append_locations([LHC])
LH7.append_locations([LHC])

Rotunda.append_locations([LHC, H5, H6, H7, H8, Stadium])
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
VH.append_locations([VH_Terrace, Shopping_Complex])
VH_Terrace.append_locations([VH])

AB1.append_locations([Gazebo, AB2, Behind_AB, AB1_1F, Animal_Facility])
AB1_1F.append_locations([AB1, AB1_2F])
AB1_2F.append_locations([AB1_1F, AB1_3F])
AB1_3F.append_locations([AB1_2F, AB1_4F])
AB1_4F.append_locations([AB1_3F, AB1_5F, EBL_Lab])
EBL_Lab.append_locations([AB1_4F])
AB1_5F.append_locations([AB1_4F])
AB2.append_locations([Gazebo, Behind_AB, AB1])
Gazebo.append_locations([Library, AB1, AB2, Behind_AB])
Behind_AB.append_locations([Main_Gate, East_Gate, AB1, AB2, Gazebo])
Animal_Facility.append_locations([LHC, East_Gate, AB1])


"""Build Actual clues"""


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
    None,
    "Yay!! You answered everything correctly!\n"
    "*happy biologist noises*\n"
    "Maybe you should go tell your friends in Rotunda",
    "OOPS. Looks like you'll need to start all over again")


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
    onComplete="Read the copied file, the secret lies within",
    onFail="File copy error, retry"
)


def clue3Action():
    print("PENALTY at 45 degrees")
    im_show("cube.jpg")
    print("Message: C.Amjg md eclcrgaq")  # change this please
    a = input("What does that mean? ")
    if a == "E.Coli of genetics":  # change this please
        Pocket("Clue - E.Coli of genetics")
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
        Pocket.append("clue - Large Hadron Collider")
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
    return True


biswas_car = Collectable(
    "A Red sedan",
    "coming from Animal Facility road",
    "It's approaching almost quasistatically...\n"
    "Why would someone be driving around at midnight?! This is pretty shady.",
    hidden=False,
    action=biswas_car_action,
    nextnotes=[],
    onComplete="This had better be worth-- \n WAIT! THE DRIVER IS ASLEEP?! *facepalm*",
    onFail="Probably not important. It's not like they're going to run over anybody.\nRight?\n\nRIGHT?")


stadium_test = Collectable(
    name="Rocket Pad",
    spot="in the stadium",
    desc="Lets fly the rocket.\n"
    "It went so high that you can't even see it!!!\n\n\n"
    "Oh no! It's falling back! RUNNN!",
)


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
    hidden=True,
    action=samrat_inno_action,
    nextnotes=[printer_3d],
    onComplete="We will have to find a 3D printer...",
    onFail="Nope, it's someone else's property")


def art_competition_action():
    im_show("art1.jpg")
    im_show("art2.jpg")
    im_show("art3.jpg")
    return True


art_competition = Collectable(
    name="multiple art pieces",
    spot="on soft boards",
    desc="There was an art competition held a few days ago.\n"
    "These are some of the beautiful paintings some people have made!",
    hidden=False,
    action=art_competition_action,
    onComplete="Damn! Those were so pretty! I wish I could make things like that"
)


def torch_action():
    print("You turn it on and its very bright!\n")
    if input("Do you want to take it [Y N]? ") == "Y":
        H5.append_locations([Rotunda])
        Pocket.append(torch)
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

"""Add Notes to Locations"""

H5.append_collectable([hostel_cctv])
H6.append_collectable([hostel_cctv])
H7.append_collectable([hostel_cctv])
H8.append_collectable([hostel_cctv])
H5_SR.append_collectable([torch])
Computer_Centre.append_collectable([clue1])
CAF.append_collectable([clue2])
T_Point.append_collectable([biswas_car])
AB1_3F.append_collectable([printer_3d])
AB1_5F.append_collectable([samrat_inno])
Stadium.append_collectable([stadium_test])
LHC.append_collectable([art_competition, clue3])
LH5.append_collectable([clue5])
EBL_Lab.append_collectable([clue4])



def makemap():
    g: nx.DiGraph = nx.DiGraph()
    for loc in [Main_Gate, East_Gate, T_Point, Health_Center, Admin, CAF, Library, Computer_Centre, LHC, LH1, LH2, LH3, LH4, LH5, LH6, LH7, Rotunda, H5, H5_SR, H6, H6_SR, H7,
                H7_SR, H8, H8_SR, Stadium, BB_Court, VH, VH_Terrace, Shopping_Complex, AB1, AB1_1F, AB1_2F, AB1_3F, AB1_4F, EBL_Lab, AB1_5F, AB2, Gazebo, Behind_AB, Animal_Facility]:
        for loc2 in loc.locations:
            g.add_edge(loc.name, loc2.name)
    nx.draw_kamada_kawai(g, with_labels=True)
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
        makemap()
    elif re.search(r"^pocket$", inp):
        Pocket.show()
    elif re.search(r"^exit", inp):
        close_game()
    else:
        msg = "Invalid Input"
    if (msg):
        timed_print(msg, 0)
