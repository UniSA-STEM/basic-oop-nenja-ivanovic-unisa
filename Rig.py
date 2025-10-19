"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


class Rig:
    def __init__(self, name: str):
        self.__name = name
        self.__password = None  # hacker will pick a password when they register the device
        # attributes measuring damage:
        self.__damage_counter = 0
        self.__broken_state = False
        # attributes measuring storage:
        self.__storage = [Asset("Data Spike"), Asset("Data Spike"), Asset("Removable Drive")]
        self.__storage_counter = 3
        # attributes affected by an upgrade:
        self.__upgrade_level = 0
        self.__max_hp = 2
        self.__max_storage = 5

    def __str__(self) -> str:
        return "\n------------------------------------------------\n" + self.__name + " - " + self.__describe_condition() + "\n" + self.__describe_stored_assets() + "\n------------------------------------------------\n"

    # getters
    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_inventory_counter(self):
        return self.__storage_counter

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_max_hp(self):
        return self.__max_hp

    def get_max_inventory(self):
        return self.__max_storage

    def __storage_capacity_available(self) -> bool:
        """
        Compares the maximum rig storage capacity and current fullness to determine if there is remaining storage room.
        :return: True if room remaining, False if storage is full.
        """
        return self.__max_storage - self.__storage_counter > 0

    def __describe_condition(self) -> str:
        """ Returns a description of the Rig based on its health and upgrade level."""
        condition = ""
        if self.__broken_state:
            condition += "Broken"
        else:
            condition += "Pristine"
        condition += f" (Level {self.__upgrade_level})"
        return condition

    def __describe_stored_assets(self) -> str:
        """ Returns a string of the Asset objects stored in the Rig's storage, listed in a visually appealing way."""
        description = f"Assets stored ({self.__storage_counter}/{self.__max_storage}):"
        index = 1
        for asset in self.__storage:
            description = description + f"\n{index}. " + asset.__str__()
            index += 1
        return description

    def __get_unencrypted_assets(self) -> list[Asset]:
        """Returns a list of all the assets in the rig's storage which are not encrypted."""
        return [asset for asset in self.__storage if not asset.get_encrypted]

    def __search_unencrypted_assets_by_name(self, name: str) -> list[Asset]:
        """Searches the Rig storage for unencrypted assets by name, and returns a list of matches."""
        matches = []
        for asset in self.__get_unencrypted_assets():
            if asset.name == name:
                matches.append(asset)
        return matches

    def __access_authorized(self, password: str = None) -> bool:
        """Matches a provided password against the registered to authorize user access."""
        if self.__broken_state:  # if the rig is broken, enemy hacker can bypass password requirements.
            authorized = True
            print(f"WARNING: Unauthorized access has occurred on {self.__name}.")
        else:
            authorized = (password != self.__password)
            if not authorized: print("Access denied.")
        return authorized

    def retrieve_asset(self, name: str, password: str = None) -> Asset | None:
        """
        Allows objects from other classes to take resources from the rig's storage if they pass the rig's security measures.
        :param name:The name of the asset which the user wishes to retrieve from the rig's storage.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: Asset if an asset with a matching name is found in the rig's storage which is unencrypted, otherwise nothing.
        """
        if not self.__access_authorized(password): return None

        assets = self.__search_unencrypted_assets_by_name(name)
        if len(assets) == 0:
            print(f"Unable to retrieve {name} from {self.__name}; the asset is encrypted or does not exist.")
            return None
        else:
            asset = assets[0]
            self.__storage_counter -= 1
            self.__storage.remove(asset)
            print(f"An unencrypted {name} has been retrieved from {self.__name}'s storage.")
            return asset

    def retrieve_all_assets(self, password: str = None) -> list[Asset] | None:
        """
        Authorizes access of the object calling the function and then iterates through the list of unencrypted assets, calling
        the retrieve_asset() function on each.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: A list of assets if the retrieval is successful, None if not.
        """
        if not self.__access_authorized(password): return None
        assets = self.__get_unencrypted_assets()
        if len(assets) == 0:
            print(f"There are no assets in {self.__name} available for retrieval.")
            return None
        else:
            print("Please wait, retrieving assets...")
            count = 0
            for asset in assets:
                self.retrieve_asset(asset.name, password)
                count += 1
            print(f"Retrieval complete ({count} asset(s) have been retrieved from {self.__name}).")
            return assets

    def store_asset(self, asset: Asset, password: str = None) -> Asset | None:
        """
        Try to store an asset into storage, ensuring first that access is authorized, there is storage space and that the asset type is allowed.
        :param asset: The asset item that wants to be stored.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: Returns the Asset object if it was not able to be stored, or None if it was.
        """
        if not self.__access_authorized(password): return asset

        if self.__storage_capacity_available():
            if isinstance(asset, Asset):
                self.__storage.append(asset)
                self.__storage_counter += 1
                print(
                    f"'{asset.name} stored in {self.__name}. Assets stored: {self.__storage_counter}/{self.__max_storage}")
                return None
            else:
                print(f"Cannot store asset; asset not recognized.")
        else:
            print("Cannot store asset; storage is full.")
        return asset

    def register_password(self, new_password: str, existing_password: str = None) -> None:
        """
        Set up a new password for rig access, or replace an existing one if authorized.

        :param new_password: A string denoting the new password to be registered.
        :param existing_password: The password required to verify that the user is authorized to replace the existing password.
        :return: None
        """
        if not self.__access_authorized(existing_password):
            print("You must provide the existing password before you can register a new one.")

        else:
            self.__password = new_password
            print(f"New password successfully registered on {self.__name}.")
        return None

    def upgrade(self, hardware_patch: Asset) -> None:
        """Upgrade the rig by consuming a hardware patch asset."""
        if isinstance(hardware_patch, Asset) and hardware_patch.name == "Hardware Patch":
            self.__upgrade_level += 1
            self.__max_hp += 2
            self.__damage_counter = 0  # reset to zero
            print(f"Upgrade complete! {self.__name} is now {self.__describe_condition()}.")
        else:
            print(f"Upgrade failed. A hardware patch is required to upgrade {self.__name}.")
        return None
