"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Hacker import Hacker
from Rig import Rig
from random import randint


# Test: attempting to add various items to rig storage.
def trial1():
    """Test: attempting to add various items to rig storage."""
    rig1 = Rig("Rig1")
    print(rig1)
    rig1.store_asset(Asset("dat"))  # invalid
    rig1.store_asset(Asset("CryptoToken"))  # invalid
    rig1.store_asset(Asset("Data Spike"))  # valid
    rig1.store_asset(Asset("Data Spike"))  # storage full
    print(rig1)


# Test: initiate hacker and acquire a rig.
def trial2():
    """Test: initiate hacker and acquire a rig."""
    charlie = Hacker("Charlie")
    alex = Hacker("Alex")
    rig1 = Rig("Rig1")
    rig2 = Rig("Rig2")

    print(charlie)
    charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
    print(charlie)  # should not have anything in her inventory.
    charlie.acquire_rig(rig2, "W4MBOtxl")  # already has rig

    alex.acquire_rig(Asset("Hardware Patch"), "14slytherinLemonzzz@")  # rig not provided
    alex.acquire_rig(rig1, "14slytherinLemonzzz@")  # rig already owned
    alex.retrieve_asset("CryptoToken")  # lose token
    alex.acquire_rig(rig2, "14slytherinLemonzzz@")  # does not have token


# Test: transfer assets between hacker inventories and rig storage. Manage Hacker trace level and rig
# random asset generation.
def trial3():
    """ Test: transfer assets between hacker inventories and rig storage. Manage Hacker trace level and rig
    random asset generation."""
    charlie = Hacker("Charlie")
    alex = Hacker("Alex")
    rig1 = Rig("Rig1")
    rig2 = Rig("Rig2")
    charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
    alex.acquire_rig(rig2, "14slytherinLemonzzz@")

    charlie.get_asset_from_rig("Data Spike")  # valid
    print(charlie)
    print(rig1)

    charlie.get_asset_from_rig("Data")  # not real data
    charlie.get_asset_from_rig("CryptoToken")  # rig does not currently possess this object.
    charlie.get_asset_from_rig("Data Spike", rig2)  # trying to steal from another hacker's rig.
    charlie.get_asset_from_rig("Data Spike", rig2)
    charlie.get_asset_from_rig("Data Spike", rig2)  # too exposed
    print(charlie)

    charlie.lay_low()
    charlie.lay_low()
    charlie.lay_low()
    charlie.lay_low()
    charlie.lay_low()
    print(charlie)
    print(rig1)


# Test: Launch data spike attacks, take rig damage and repair damage.
def trial4():
    """Test: Launch data spike attacks, take rig damage and repair damage."""
    charlie = Hacker("Charlie")
    alex = Hacker("Alex")
    rig1 = Rig("Rig1")
    rig2 = Rig("Rig2")
    charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
    alex.acquire_rig(rig2, "14slytherinLemonzzz@")

    alex.launch_data_spike(rig1)
    alex.launch_data_spike(rig1)
    alex.launch_data_spike(rig1)  # no spike available
    alex.get_asset_from_rig("Data Spike", rig1)
    alex.lay_low()  # generate assets
    alex.lay_low()
    alex.lay_low()
    alex.lay_low()
    alex.launch_data_spike(rig1)  # if new data spikes have been generated, rig 1 is attacked when already broken.
    alex.launch_data_spike(3)  # incorrect input
    charlie.launch_data_spike(rig2)


trial4()
