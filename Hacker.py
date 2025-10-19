"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    def __init__(self, name: str):
        self.__name = name
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = None
        self.__trace_level = 0
        self.__is_exposed = False
        self.__trace_threshold = 5

    def __str__(self) -> str:
        return ("\n------------------------------------------------\n" +
                self.__name + " - " + self.__describe_trace_level() + "\n" +
                f"Rig: {None if self.__rig is None else self.__rig.name}" +
                self.__describe_stored_assets() +
                "\n------------------------------------------------\n")

    def __describe_trace_level(self) -> str:
        """ Returns a description of the Hacker's condition based on their trace level and whether they are exposed."""
        description = ""
        if self.__is_exposed:
            description += "Exposed"
        else:
            description += "Not Exposed"
        description += f" (Trace Level: {self.__trace_level}/{self.__trace_threshold})"
        return description

    def __describe_stored_assets(self) -> str:
        """ Returns a string of the Asset objects stored in the Hacker's inventory, listed in a visually appealing way."""
        description = f"Assets in Inventory:"
        index = 1
        for asset in self.__inventory:
            description = description + f"\n{index}. " + asset.__str__()
            index += 1
        return description
