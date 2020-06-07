import re

from GameObjects import Location, Note, screen_clear, timed_print


"""Build all the locations"""

Main_Gate = Location(
    "Main Gate",
    "A Nice Big Arch!\nStudents are coming back from their friday night party at 12am...")
East_Gate = Location(
    "East Gate",
    "A train passes by...")
T_Point = Location(
    "T point",
    "Hunh, I can see something weird in this mirror, Oh thats just me...")
Admin = Location(
    "Admin",
    "You enter the lovely automatic sliding doors, a cool blast of AC...\n" +
    "You see the IISER-M model and remember that 4 more hostels need to be built. But there's no funds...")
CAF = Location(
    "CAF",
    "Very sensitive machines which may be disturbed by students eating in the cafeteria\n" +
    "You hear someone shouting at someone else in the distance, but do not record it, for it would be a violation of privacy")
Library = Location("Library", "So quiet...")

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
H5_SR = Location('H5_SR', "Back to the start...")
H6 = Location('H6', 'Hos... The rest of the banner is torn...')
H6_SR = Location(
    'H6_SR',
    'You see a couple snogging. They see you. It\'s so awkward')
H7 = Location('H7', 'Someone is taking their clothes to wash...')
H7_SR = Location(
    'H7_SR',
    'Those Dance Club people are still dancing in the Dance Room')
H8 = Location(
    'H8',
    'Some MS18 kids are loitering around...')
H8_SR = Location(
    'H8_SR',
    'The ACs are off, its so hot...\nOh wait, they are on... Why is it hot then?')

Stadium = Location('Stadium', 'A lapwing shouts in the distance...')
BB_Court = Location('BB Court', 'Why the fuck do lapwings make so much noise?')
VH = Location(
    'VH',
    'Dollar building. You see some... WHY THE FUCK ARE LAPWINGS EVERYWHERE?')
VH_Terrace = Location(
    'VH Terrace',
    'Haaah! Nice and windy. You see a couple of friends talking about the struggles of life...')
Shopping_Complex = Location(
    'Shopping_Complex',
    'It\'s so empty and quiet. Aunty must have gone home...')

AB1 = Location(
    'AB1',
    'You buy a nice coffee for 10rs, coz neither of you have change')
AB1_1F = Location('AB1_1F', 'People playing Badminton...')
AB1_2F = Location('AB1_2F', 'Eerily dark and quiet')
AB1_3F = Location(
    'AB1_3F',
    'One lone MS13 is studying there. Why haven\'t they graduated yet?')
AB1_4F = Location('AB1_4F', 'Eerily dark and quiet')
AB1_5F = Location(
    'AB1_5F',
    'Eerily dark and quiet, but there\'s some news article about Plastic Firecrackers...')
AB2 = Location(
    'AB2',
    'ERROR! The app devs didn\'t care enough to make 2 AB\'s. There\'s nothing here.')
Gazebo = Location(
    'Gazebo',
    'There\'s some MS17 party going on there. Oh god so much cake wasted.\n'
    'Talking about wasting stuff, they\'re fixing the covers...')
Behind_AB = Location('Behind AB', 'Aww! 3 cute puppies run up to you.')
Animal_Facility = Location(
    'Animal_Facility',
    'The everlasting humm of the machines...\n' +
    'What are these machines? What happens here? SO MANY QUESTIONS!')

"""Connect the Locations to make a traversable map"""
Main_Gate.append_locations([Behind_AB, Admin, CAF])
East_Gate.append_locations([Animal_Facility, Behind_AB])
T_Point.append_locations([CAF, LHC, Admin, BB_Court])
Admin.append_locations([Library, Main_Gate, CAF, T_Point])
CAF.append_locations([Admin, Main_Gate, T_Point])
Library.append_locations([Admin, LHC, Gazebo])

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
H5.append_locations([Rotunda, H5_SR])
H6.append_locations([Rotunda, H6_SR])
H7.append_locations([Rotunda, H7_SR])
H8.append_locations([Rotunda, H8_SR])
H5_SR.append_locations([H5])
H6_SR.append_locations([H6])
H7_SR.append_locations([H7])
H8_SR.append_locations([H8])

Stadium.append_locations([Rotunda, BB_Court, Shopping_Complex])
BB_Court.append_locations([T_Point, Stadium])
Shopping_Complex.append_locations([Stadium, VH])
VH.append_locations([VH_Terrace, Shopping_Complex])

AB1.append_locations([Gazebo, AB2, Behind_AB, AB1_1F, Animal_Facility])
AB1_1F.append_locations([AB1, AB1_2F])
AB1_2F.append_locations([AB1_1F, AB1_3F])
AB1_3F.append_locations([AB1_2F, AB1_4F])
AB1_4F.append_locations([AB1_3F, AB1_5F])
AB1_5F.append_locations([AB1_4F])
AB2.append_locations([Gazebo, Behind_AB, AB1])
Gazebo.append_locations([Library, AB1, AB2, Behind_AB])
Behind_AB.append_locations([Main_Gate, East_Gate, AB1, AB2, Gazebo])
Animal_Facility.append_locations([LHC, East_Gate, AB1])

"""Build Notes"""
hostel_cctv = Note(
    "YOU ARE UNDER CCTV SURVIELLENCE",
    "on the Soft Board")



def fake_clue_action():
    print("The password is 5")  # some message
    return input("What's the password? ") == "5"  # some prompt


def printer_3d_action():
    print("You go near the 3D printer and see a bunch of MS19 students sleeping around it.\nThey are probably tired from waiting their turn at the printer.\n\n\nPrinter shows a message 'Do you want to start printing?'")
    return input("Do you want to print? [Y N] ") == "Y"

def samrat_inno_action():
    return input("Do you want to print and test this? [Y N] ")=="Y"

def print_inno_action():
    print("Lets print the innovation blueprint")
    return input("Do you want to print? [Y N] ") == "Y"

fake_clue = Note(
    "This is a test clue",  # message of a clue
    "under some table",  # some specific place
    False,  # Not hidden
    fake_clue_action,  # action object
    hostel_cctv,  # next note
    "Yay! Look for a treat in the Hostels",
    "Noo, you dumb?")

printer_3d = Note(
    "You see a 3D printer",
    "outside physics lab",
    False,
    printer_3d_action,
    fake_clue,
    onComplete="The Printer started making weird noises.\nSHIT the students MS19 kids will wake up.\n\nBetter get out of here",
    onFail = "Lets get outta here")

stadium_test = Note(
    "Lets fly this rocket.\n\n\nOH SHIT!!!!! IT HIT A LAPWIG!! \nRUUUUUN!!!!!",
    "in the stadium",
    )

print_inno = Note(
    "Theres the 3D printer, and its free? Huh",
    "outside physics lab",
    True,
    print_inno_action,
    stadium_test,
    "Yay, Lets go to the stadium to test it",
    "Naa dont wanna print it")

samrat_inno = Note(
    "There's a Blueprint, Innovation #42054....\n\n#show image rocket.jpg\n\nMaybe I can 3D print this and see if it works.",
    "near Samrat's Lab",
    False,
    samrat_inno_action,
    print_inno,
    "We will have to find a 3D printer.",
    "Naa it wont be that fun anyways.")


"""Add Notes to Locations"""
H5.append_notes([hostel_cctv])
H6.append_notes([hostel_cctv])
H7.append_notes([hostel_cctv])
H8.append_notes([hostel_cctv])

H5_SR.append_notes([fake_clue])

AB1_3F.append_notes([printer_3d,print_inno])
AB1_4F.append_notes([samrat_inno])
Stadium.append_notes([stadium_test])

hello_banner = '''Welcome to the Virtual Treasure Hunt!
The Treasure Hunt will go on until you finish it. The first person to finish will win.
This is an individual game, but you can always team up with someone else.
But remember that they can hide things from you and win themselves.
You can use the internet.
Please remember that if you exit from this app (by pressing the X or by shutting down your computer),
you will HAVE to restart. You can minimize this safely, however.
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
    print(here)
    print("\n\n")
    print("If you want to search around, type search or ls")
    print("If you want to go somewhere else, type goto _location_ or cd _location_")

    inp = input("Your choice: ")
    if re.search(r"(search|ls)", inp):
        msg = here.search()
    elif match_obj := re.search(r"(goto|cd) .*", inp):
        new_loc = inp[len(match_obj.group(1)) + 1:]
        msg, here = here.goto(new_loc)
    else:
        msg = "Invalid Input"

    if (msg):
        timed_print(msg, 3)
