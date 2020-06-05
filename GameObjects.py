import time
import os
from typing import Callable, Type, List


class Note:
    def __init__(self, message: str, spot: str, hidden: bool = True,
                 action: Callable[[], bool] = None,
                 nextnote=None,
                 onComplete: str = "Clue completed", onFail: str = "Incorrect answer",
                 ) -> None:
        """Initialises a Note object

        Args:
            message (str): The message that is displayed
            spot (str): A more specific location where it is found. For example, "under a bottle"
            hidden (bool): Whether the Note is visible or not
            action (Callable[[], bool]) = None: The action to do to challenge the player.
            onComplete (str) = "Clue completed": The string to print if action completed successfully
            onFail (str) = "Incorrect answer": The string to print if action unseccessful
        """
        self.message = message
        self.spot = spot
        self.hidden = hidden
        self.nextnote = nextnote
        self.action = action
        self.onComplete = onComplete
        self.onFail = onFail

    def __str__(self) -> str:
        """Get a string representation to print

        Returns:
            str: [description]
        """
        return "Found a Note " + self.spot + "!\n\n Note reads:\n" + self.message + "\n\n"

    def show(self):
        print(self)
        if (self.action is not None and
                input("Do you want to solve the clue[Y N]? ") == "Y"):
            while True:
                screen_clear()
                if (self.action()):
                    print(self.onComplete)
                    self.hidden = True
                    self.nextnote.hidden = False
                    break
                else:
                    print(self.onFail)
                    if (input("Try again[Y N]? ") == "N"):
                        break


class Location:
    def __init__(self, name: str, description: str,
                 notes: List[Note] = None, locations: List = None) -> None:
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

    def append_notes(self, newnotes: List):
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
                input("Press Enter for the Next Note.")
            return "No more notes"

    def goto(self, new_loc_name: str):
        for loc in self.locations:
            if loc.name == new_loc_name:
                return "Going to " + new_loc_name, loc
        return "No such connecting location.", self


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def timed_print(msg: str, secs: int):
    print(msg, end="", flush=True)
    for _ in range(secs):
        time.sleep(1)
        print(".", end="", flush=True)
    print()
