"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
# from Hacker import Hacker
from Rig import Rig


#
def test1():
    """Test: attempting to add various items to rig storage."""
    rig1 = Rig("Rig1")
    print(rig1)
    rig1.store_asset(Asset("dat"))  # invalid
    rig1.store_asset(Asset("CryptoToken"))  # invalid
    rig1.store_asset(Asset("Data Spike"))  # valid
    rig1.store_asset(Asset("Data Spike"))  # storage full
    print(rig1)


test1()
