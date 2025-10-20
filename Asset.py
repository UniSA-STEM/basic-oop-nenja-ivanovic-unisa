"""
File: Asset.py
Description: Contains the Asset class. Assets are very simple objects that only protect simple attributes which
describe them (name, description, encryption status and attack damage). In addition, they are responsible for
validating that new Asset instances fall into one of 5 predefined  types, and can also generate one of these
randomly when prompted.
Author: Nenja Ivanovic
ID: 110462390
Username: ivany005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from random import randint


class Asset:
    available_assets = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]

    def __new__(cls, name: str = None):
        """
        Allocate a new Asset instance, validating the proposed name before creation.
        :param name: The proposed asset name of the new instance that needs to be validated.
        """
        if name not in Asset.available_assets and name is not None:
            print(f"The asset '{name}' does not exist. Available assets are: {Asset.available_assets}")
            return None
        return super().__new__(cls)

    def __init__(self, name: str = None) -> None:
        """
        Initialise new Asset instances.
        :param name: The asset's name.
        """
        if name is None:  # generate a random asset when no name is specified
            random_index = randint(0, len(Asset.available_assets) - 1)
            name = Asset.available_assets[random_index]

        self.__name = name
        self.__encrypted = False
        self.__description = "NA"
        self.__attack_damage = 0

        if name == "CryptoToken":
            self.__description = "Used to acquire or repair rigs."
        elif name == "Data Spike":
            self.__description = "Used in battles."
            self.__attack_damage = 1
        elif name == "Removable Drive":
            self.__description = "Found in rigs and used for extraction."
        elif name == "Security Chip":
            self.__description = "Used to encrypt or decrypt assets."
        elif name == "Hardware Patch":
            self.__description = "Used to upgrade rigs."

    def __str__(self):
        """Return a string description of the Asset"""
        name = f"{self.name}: {self.description}"
        if self.encrypted: name += " [Encrypted]"
        return name

    # getters;
    def get_name(self) -> str:
        """Get the asset name"""
        return self.__name

    def get_description(self):
        """Get the asset description"""
        return self.__description

    def get_encrypted(self):
        """Get the asset encryption status"""
        return self.__encrypted

    # properties:
    name = property(get_name)
    description = property(get_description)
    encrypted = property(get_encrypted)

    def encrypt(self) -> None:
        """set the asset encryption status to Encrypted"""
        self.__encrypted = True

    def decrypt(self) -> None:
        """set the asset encryption status to Decrypted"""
        self.__encrypted = False

    def deal_damage(self) -> int:
        """get the asset's attack damage, and print a description of the asset dealing damage"""
        print(f"...The {self.__name} deals {self.__attack_damage} damage.")
        return self.__attack_damage
