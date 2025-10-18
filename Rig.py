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
    storable_assets = ["Data Spike", "Removable Drive", "Security Chip"]

    def __init___(self, name: str):
        self.__name = name
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

    def storage_capacity_available(self) -> bool:
        """
        Compares the maximum rig storage capacity and current fullness to determine if there is remaining storage room.
        :return: True if room remaining, False if storage is full.
        """
        return self.__max_storage - self.__storage_counter == 0

    def store_item(self, asset: Asset) -> Asset | None:
        """
        Try to store an asset into storage, ensuring first that there is space and that asset type is allowed.
        :param Asset asset: The asset item that wants to be stored.
        :return: Returns the Asset object if it was not able to be stored, or None if it was.
        """
        if self.storage_capacity_available():
            if isinstance(asset, Asset) and asset.name in Rig.storable_assets:
                self.__storage.append(asset)
                self.__storage_counter += 1
                print(
                    f"'{asset.name} stored in {self.__name}. Assets stored: {self.__storage_counter}/{self.__max_storage}")
                return None
            else:
                print(f"{self.__name} is unable to store that type of item.")
        else:
            print("Cannot store asset; storage is full.")
        return asset
