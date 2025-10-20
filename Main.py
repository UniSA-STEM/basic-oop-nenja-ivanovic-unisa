"""
File: main.py
Description: 5 sample test scenarios are run to demonstrate how the Asset, Hacker, and Rig classes interact with each
other. The module instantiates instance of classes and simulates Hackers battling via their Rigs.
Author: Nenja Ivanovic
ID: 110462390
Username: ivany005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Hacker import Hacker
from Rig import Rig
from random import randint


# Test: Add various items to rig storage.
def trial1():
    """Test: Add various items to rig storage."""
    rig1 = Rig("Rig1")
    print(rig1)
    rig1.store_asset(Asset("dat"))  # invalid
    rig1.store_asset(Asset("CryptoToken"))  # invalid
    rig1.store_asset(Asset("Data Spike"))  # valid
    rig1.store_asset(Asset("Data Spike"))  # storage full
    print(rig1)


# Test: Initiate hacker and acquire a rig. Upgrade rig.
def trial2():
    """Test: Initiate hacker and acquire a rig."""
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

    # upgrade rig:
    charlie.upgrade_rig()  # no hardware patch
    charlie.find_asset(Asset("Hardware Patch"))
    charlie.find_asset(Asset("Security Chip"))
    charlie.find_asset(Asset("Security Chip"))

    charlie.encrypt_inventory_asset("Hardware Patch")
    charlie.upgrade_rig()  # hardware patch is encrypted

    charlie.decrypt_inventory_asset("Hardware Patch")
    charlie.upgrade_rig()  # valid


# Test: Transfer assets between hacker inventories and rig storage. Manage Hacker trace level and rig
# random asset generation.
def trial3():
    """ Test: Transfer assets between hacker inventories and rig storage. Manage Hacker trace level and rig
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

    charlie.lay_low()  # reduce trace level and generate random assets in rig
    charlie.lay_low()
    charlie.lay_low()

    print(charlie)
    print(rig1)


# Test: Launch data spike attacks, take rig damage, extract all from broken rig, repair damage.
def trial4():
    """Test: Launch data spike attacks, take rig damage and repair damage."""
    charlie = Hacker("Charlie")
    alex = Hacker("Alex")
    rig1 = Rig("Rig1")
    rig2 = Rig("Rig2")
    charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
    alex.acquire_rig(rig2, "14slytherinLemonzzz@")

    alex.get_asset_from_rig("Removable Drive")
    alex.extract_all_rig_assets(rig1)  # rig not broken yet

    alex.launch_data_spike(rig1)
    alex.launch_data_spike(rig1)
    alex.launch_data_spike(rig1)  # no spike available

    alex.lay_low()  # generate assets
    alex.lay_low()
    alex.lay_low()
    alex.lay_low()
    alex.launch_data_spike(rig1)  # if new data spikes have been generated, rig 1 is attacked when already broken.
    alex.launch_data_spike(3)  # incorrect input
    charlie.launch_data_spike(rig2)

    alex.extract_all_rig_assets(rig1)  # removable drive was used up in earlier attempt
    alex.find_asset(Asset("Removable Drive"))
    alex.extract_all_rig_assets(rig1)

    print(alex)
    print(rig1)


# Test: Encryption and decryption of storage/inventory assets.
def trial5():
    """Encryption and decryption of storage/inventory assets."""
    charlie = Hacker("Charlie")
    alex = Hacker("Alex")
    rig1 = Rig("Rig1")
    rig2 = Rig("Rig2")
    charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
    alex.acquire_rig(rig2, "14slytherinLemonzzz@")

    alex.encrypt_inventory_asset("CryptoToken")  # token does not yet exist
    print(alex)
    alex.find_asset(Asset("CryptoToken"))
    print(alex)
    alex.encrypt_inventory_asset("CryptoToken")  # does not have Security Chip

    alex.find_asset(Asset("Security Chip"))
    print(alex)
    alex.encrypt_inventory_asset("CryptoToken")  # valid

    print(alex)  # token should be encrypted

    alex.decrypt_inventory_asset("CryptoToken")  # no more security chips.
    alex.find_asset(Asset("Security Chip"))
    alex.decrypt_inventory_asset("CryptoToken")  # valid

    # storing a specific inventory asset in rig and encrypting rig assets:
    alex.store_asset_in_rig("CryptoToken")
    alex.store_asset_in_rig("CryptoToken")  # has already been transferred

    alex.encrypt_rig_asset("CryptoToken")  # no security chip in rig

    alex.find_asset(Asset("Security Chip"))
    alex.store_asset_in_rig("Security Chip")
    alex.encrypt_rig_asset("CryptoToken")  # valid

    # transferring all inventory assets to rig and decrypting rig assets:
    alex.find_asset(Asset("Security Chip"))
    alex.find_asset(Asset("Security Chip"))
    alex.find_asset(Asset("Security Chip"))
    alex.find_asset(Asset("Security Chip"))  # ^add lots of chips to inventory

    alex.store_all_assets_in_rig()
    alex.encrypt_rig_asset("Security Chip")
    print(alex)
    print(rig2)

    # retrieve all rig assets into inventory:
    alex.extract_all_rig_assets()
    print(alex)
    print(rig2)


print("//////////////////////////////////////////////////////////////////////     SET 1 TESTS")
trial1()

print("//////////////////////////////////////////////////////////////////////     SET 2 TESTS")
trial2()

print("//////////////////////////////////////////////////////////////////////     SET 3 TESTS")
trial3()

print("//////////////////////////////////////////////////////////////////////     SET 4 TESTS")
trial4()

print("//////////////////////////////////////////////////////////////////////     SET 5 TESTS")
trial5()
