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
        self.__rig_password = None
        self.__trace_level = 0
        self.__is_exposed = False
        self.__trace_threshold = 5

    def __str__(self) -> str:
        return ("------------------------------------------------\n" +
                self.__name + " - " + self.__describe_trace_level() + "\n" +
                f"Rig: {None if self.__rig is None else self.__rig.name}\n" +
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
        description = f"\nAssets in Inventory:"
        if len(self.__inventory) == 0:
            description += " None"
        else:
            index = 1
            for asset in self.__inventory:
                description = description + f"\n{index}. " + asset.__str__()
                index += 1
        return description

    def __get_unencrypted_assets(self) -> list[Asset]:
        """Returns a list of all the assets in the Hacker's inventory which are not encrypted."""
        return [asset for asset in self.__inventory if asset.get_encrypted != True]

    def __scan_inventory_by_name(self, name: str) -> list[Asset]:
        """Searches the Hacker's inventory for unencrypted assets by name, and returns a list of matches."""
        matches = []
        for asset in self.__get_unencrypted_assets():
            if asset.name == name:
                matches.append(asset)
        return matches

    def retrieve_asset(self, name: str) -> Asset | None:
        """
        Allows objects from other classes to take resources from the Hacker's inventory.
        :param name:The name of the asset which the hacker wishes to retrieve from their inventory.
        :return: Asset if an asset with a matching name is found in the Hacker's inventory which is unencrypted, otherwise nothing.
        """
        assets = self.__scan_inventory_by_name(name)
        if len(assets) == 0:
            print(f"{self.__name} fails to retrieve {name} from inventory;"
                  f" the {name} must be encrypted or does not exist.\n")
            return None
        else:
            asset = assets[0]
            self.__inventory.remove(asset)
            return asset

    def acquire_rig(self, rig: Rig, password: str) -> None:
        """
        Allows the hacker to purchase an available rig for 1 CryptoToken and register a password on it.
        :param rig: The rig object which the Hacker wishes to try to acquire.
        :param password: The password that will be registered on the rig if it is successfully acquired.
        :return:None
        """
        if self.__rig is not None:
            print(f"{self.__name} fails to acquire a rig; "
                  f"{self.__name} cannot bring themself to replace {self.__rig.name}.")
        elif not isinstance(rig, Rig):
            print(f"{self.__name} fails to acquire a rig; the object they thought was a "
                  f"rig was actually something else...")
        elif rig.registered:
            print(f"{self.__name} fails to acquire a rig; the rig they wanted already belongs to someone else.")
        else:
            crypto_token = self.retrieve_asset("CryptoToken")
            if crypto_token is None:
                print(f"{self.__name} fails to acquire a rig; a rig costs 1 CryptoToken "
                      f"and {self.__name} can't find any.")
            else:
                print(f"{self.__name} acquires {rig.name} for 1 CryptoToken. Hooray!")
                self.__rig = rig
                self.__rig_password = password
                self.__rig.register_password(password)
        print("")
        return None

    def get_asset_from_rig(self, name: str, alt_rig: Rig = None) -> None:
        self.__trace_level += 1

        if alt_rig is None:
            rig = self.__rig  # taking from own rig
            print(f"{self.__name} tries to transfer a {name} from {rig.name}...")
        else:
            rig = alt_rig  # taking from someone else's rig
            print(f"{self.__name} tries to steal a {name} from {rig.name}...")

        self.__inventory.append(rig.retrieve_asset(name, self.__rig_password))
        # remove 'None' if that is what was returned:
        self.__inventory = [asset for asset in self.__inventory if asset is not None]
        print("")
        return None
