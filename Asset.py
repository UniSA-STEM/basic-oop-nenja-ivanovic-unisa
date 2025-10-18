"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    available_assets = ["CryptoToken", "Dataspike", "Removable_Drive", "SecurityChip", "HardwarePatch"]

    def __init__(self, name: str):
        assert name in Asset.available_assets, f"The item '{name}' does not exist. Available assets are: {Asset.available_assets}"
        self.__name = name
        self.__encrypted = False

        if name == "CryptoToken:":
            self.__description = "Used to acquire or repair rigs."
        elif name == "Dataspike":
            self.__description = "Used in battles."
        elif name == "Removable_Drive":
            self.__description = "Found in rigs and used for extraction."
        elif name == "SecurityChip":
            self.__description = "Used to encrypt or decrypt assets."
        else:
            self.__description = "Used to upgrade rigs."

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def encrypt(self) -> None:
        self.__encrypted = True

    def decrypt(self) -> None:
        self.__encrypted = False
