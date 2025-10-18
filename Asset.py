"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    available_assets = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]

    def __init__(self, name: str):
        if name not in Asset.available_assets:
            print(f"The item '{name}' does not exist. Available assets are: {Asset.available_assets}")
        else:
            self.__name = name
            self.__encrypted = False

            if name == "CryptoToken:":
                self.__description = "Used to acquire or repair rigs."
            elif name == "Data Spike":
                self.__description = "Used in battles."
            elif name == "Removable Drive":
                self.__description = "Found in rigs and used for extraction."
            elif name == "Security Chip":
                self.__description = "Used to encrypt or decrypt assets."
            else:
                self.__description = "Used to upgrade rigs."

    def __str__(self):
        name = f"{self.name}: {self.description}"
        if self.__encrypted: name += " [Encrypted]"
        return name

    # getters;
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    # properties:
    name = property(get_name)
    description = property(get_description)
    encrypted = property(get_encrypted)

    def encrypt(self) -> None:
        self.__encrypted = True

    def decrypt(self) -> None:
        self.__encrypted = False
