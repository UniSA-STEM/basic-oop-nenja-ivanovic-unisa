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

    def __init___(self, name: str):
        self.__name = name
        # attributes measuring damage:
        self.__damage_counter = 0
        self.__broken_state = False
        # attributes measuring storage:
        self.__storage = [Asset("Data Spike"), Asset("Data Spike"), Asset("Removable Drive")]
        self.__inventory_counter = 3
        # attributes affected by an upgrade:
        self.__upgrade_level = 0
        self.__max_hp = 2
        self.__max_inventory = 5

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_inventory_counter(self):
        return self.__inventory_counter

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_max_hp(self):
        return self.__max_hp

    def get_max_inventory(self):
        return self.__max_inventory
   