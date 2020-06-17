from typing import Callable, List
from GameEngine import screen_clear, timed_print


class Collectable:
    def __init__(self, name: str, spot: str, desc: str, hidden: bool = False,
                 action: Callable[[], bool] = None,
                 nextnotes: List = None,
                 onComplete: str = "Clue completed", onFail: str = "Incorrect answer",
                 ) -> None:
        """Initialises a Note object

        Args:
            name(str): Name of this Collectable
            desc (str): The message that is displayed
            spot (str): A more specific location where it is found. For example, "under a bottle"
            hidden (bool) = False: Whether the Note is visible or not
            pocketable (bool) = False: Whether to add to pocket or not
            action (Callable[[], bool]) = None: The action to do to challenge the player.
            onComplete (str) = "Clue completed": The string to print if action completed successfully
            onFail (str) = "Incorrect answer": The string to print if action unseccessful
        """
        self.name = name
        self.desc = desc
        self.spot = spot
        self.hidden = hidden
        self.nextnotes = nextnotes if nextnotes else []
        self.action = action
        self.onComplete = onComplete
        self.onFail = onFail

    def __repr__(self):
        
        return "Found a " + self.name + " " +self.spot + \
            "\n" + self.desc + "\n\n"

    def show(self):
        print(self)
        if (self.action is not None and
                input("Do you want to check it out[Y N]? ") == "Y"):
            while True:
                screen_clear()
                if (self.action()):
                    print(self.onComplete)
                    self.hidden = True
                    for i in self.nextnotes:
                        i.hidden = False
                    break
                else:
                    print(self.onFail)
                    if (input("Try again[Y N]? ") == "N"):
                        break

    @staticmethod
    def noaction():
        return True


class Location:
    def __init__(self, name: str, description: str,
                 notes: List[Collectable] = None, locations: List = None) -> None:
        self.name = name
        self.description = description
        self.notes = notes or []
        self.locations = locations or []

    def __str__(self):
        return ("You are in " + self.name + "\n" +
                "-----------------------------\n\n" +
                self.description + "\n\n" +
                "-----------------------------\n\n" +
                "Connecting Locations: \n" +
                "\n".join(["****" + i.name for i in self.locations]))

    def append_locations(self, newlocs: List):
        """Append connecting locations to this Location

        Args:
            newlocs (List): [description]
        """
        self.locations.extend(newlocs)

    def append_collectable(self, newnotes: List):
        """Append notes to this location

        Args:
            newnotes (list): List of notes to append
        """
        self.notes.extend(newnotes)

    def search(self):
        """Search for unhidden Notes

        Returns:
            None
        """
        timed_print("Searching", 5)
        if len([i for i in self.notes if not i.hidden]) == 0:
            return "Nothing here"
        else:
            for i in self.notes:
                screen_clear()
                i.show()
                print()
                input("Press Enter to continue searching")
            return "Nothing else here!"

    def goto(self, new_loc_name: str):
        for loc in self.locations:
            if loc.name.lower().strip() == new_loc_name.lower().strip():
                return "Going to " + loc.name, loc
        return "No such connecting location.", self


class _PocketClass:
    def __init__(self):
        self.contents = []

    def __contains__(self, item):
        self.contents.__contains__(item)

    def append(self, item: Collectable):
        self.contents.append(item)

    def show(self):
        screen_clear()
        print("This is your pocket: ")
        print()
        for i in self.contents:
            print(i)
        print()
        input("Enter to close")


Pocket = _PocketClass()
