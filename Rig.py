"""
File: Rig.py
Description: Contains the Rig class. The rig class does not perform actions of its own accord, but responds to action
requests made by Hacker objects. Rig object methods contain the nuances of events involving transfer of assets, attack
launching, repair and upgrading.
Author: Nenja Ivanovic
ID: 110462390
Username: ivany005
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from random import randint


class Rig:
    """Creates Rig objects."""

    def __init__(self, name: str):
        self.__name = name
        self.__registered = False  # whether the rig belongs to someone
        self.__password = None  # hacker will pick a password when they register the device (tracks ownership)
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
        """Returns a formatted string description of the Rig, including its condition and stored assets."""
        return ("------------------------------------------------\n" +
                self.__name + " - " + self.__describe_condition() + "\n" + self.__describe_stored_assets() +
                "\n------------------------------------------------\n")

    # getters
    def get_name(self) -> str:
        """Returns a string of the Rig's name."""
        return self.__name

    def get_registered(self) -> bool:
        """Returns True if the Rig has been acquired by someone, False if not."""
        return self.__registered

    # properties
    name = property(get_name)
    registered = property(get_registered)

    def __storage_capacity_available(self) -> bool:
        """
        Compares the maximum rig storage capacity and current fullness to determine if there is remaining storage room.
        :return: True if room remaining, False if storage is full.
        """
        return self.__max_storage - self.__storage_counter > 0

    def __describe_condition(self) -> str:
        """ Returns a description of the Rig's condition based on its health and upgrade level."""
        condition = ""
        if self.__broken_state:
            condition += "Broken"
        else:
            condition += "Pristine"
        condition += f" (Level {self.__upgrade_level})"
        return condition

    def __describe_stored_assets(self) -> str:
        """Iterates through the Asset objects in the Rig's storage and returns a formatted string summary of them."""
        description = f"\nAssets stored ({self.__storage_counter}/{self.__max_storage}):"
        if len(self.__storage) == 0:
            description += " None"
        else:
            index = 1
            for asset in self.__storage:
                description = description + f"\n{index}. " + asset.__str__()
                index += 1
        return description

    def __get_unencrypted_assets(self) -> list[Asset]:
        """Returns a list of all the assets in the rig's storage which are not encrypted."""
        return [asset for asset in self.__storage if asset.encrypted != True]

    def __search_unencrypted_assets_by_name(self, name: str) -> list[Asset]:
        """Searches the Rig storage for unencrypted assets by name, and returns a list of matches."""
        matches = []
        for asset in self.__get_unencrypted_assets():
            if asset.name == name:
                matches.append(asset)
        return matches

    def __access_authorized(self, password: str = None, print_warnings: bool = True) -> bool:
        """Matches a provided password against the registered one to determine if a caller has authority to access the
        Rig's controlled methods.
        :param password: The password string created by the owner of the rig when the rig was registered.
        :param print_warnings: True (default) prints warnings if unauthorized access is allowed, False does not print
        warnings (used when multiple access requests are made consecutively by the 'retrieve_all()' method).
        :return: True if the password is correct (access authorized), False if incorrect (access denied)."""

        authorized = (password == self.__password)
        if not authorized:
            if self.__broken_state:  # if the rig is broken, enemy hacker can bypass password requirements.
                authorized = True
                if print_warnings: print(f"...{self.name} allows access to unauthorized user: WARNING!")
            else:
                print(f"...{self.name} denies access to unauthorized user.")
        return authorized

    def retrieve_asset(self, name: str, password: str = None, print_warnings: bool = True) -> Asset | None:
        """
        Allows objects from other classes to take resources from the rig's storage if they pass the rig's security
        measures.
        :param name:The name of the asset which the user wishes to retrieve from the rig's storage.
        :param password: The password created by the owner of the rig when the rig was registered.
        :param print_warnings: True (default) prints warnings if unauthorized access is allowed, False does not print the
        warnings (used when multiple items are retrieved consecutively by the 'retrieve_all()' method).
        :return: Asset if an asset with a matching name is found in the rig's storage which is unencrypted,
        otherwise nothing.
        """
        if not self.__access_authorized(password, print_warnings): return None
        assets = self.__search_unencrypted_assets_by_name(name)
        if len(assets) == 0:
            print(f"...{self.__name} fails to retrieve {name} from storage; the asset is encrypted or does not exist.")
            return None
        else:
            asset = assets[0]
            self.__storage_counter -= 1
            self.__storage.remove(asset)
            print(f"...{self.__name} retrieves {name} from storage.")
            return asset

    def retrieve_all_assets(self, password: str = None) -> list[Asset] | None:
        """
        Authorizes access of the object calling the function and then iterates through the list of unencrypted assets,
        calling the retrieve_asset() function on each.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: A list of assets if the retrieval is successful, None if not.
        """
        if not self.__access_authorized(password): return None
        assets = self.__get_unencrypted_assets()
        if len(assets) == 0:
            print(f"...{self.__name} has no stored assets available for retrieval.")
            return None
        else:
            print(f"...{self.__name} begins retrieving stored assets...")
            count = 0
            for asset in assets:
                self.retrieve_asset(asset.name, password, print_warnings=False)
                count += 1
            print(f"...{self.__name} finishes retrieval of {count} asset(s).")
            return assets

    def store_asset(self, asset: Asset, password: str = None) -> Asset | None:
        """
        Try to store an asset into storage, ensuring first that access is authorized, there is storage space and
        that the asset type is allowed.
        :param asset: The asset item that wants to be stored.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: Returns the Asset object if it was not able to be stored, or None if it was.
        """
        if not self.__access_authorized(password): return asset

        if self.__storage_capacity_available():
            if isinstance(asset, Asset):
                self.__storage.append(asset)
                self.__storage_counter += 1
                print(f"...{self.__name} stores a {asset.name}. "
                      f"Assets stored: {self.__storage_counter}/{self.__max_storage}")
                return None
            else:
                print(f"...{self.__name} cannot store the asset; the asset is not recognized.")
        else:
            print(f"...{self.__name} cannot store the asset; storage is full.")
        return asset

    def register_password(self, new_password: str, existing_password: str = None) -> None:
        """
        Set up a new password for rig access, or replace an existing one if authorized.
        :param new_password: A string denoting the new password to be registered.
        :param existing_password: The password required to verify that the user is authorized to replace
        the existing password.
        :return: None
        """
        if not self.__access_authorized(existing_password):
            print(f"...{self.__name} rejects new password; "
                  f"the existing password must be provided before a new one can be registered.")
        else:
            self.__password = new_password
            self.__registered = True
            print(f"...{self.__name} successfully registers new password.")

    def upgrade(self, hardware_patch: Asset) -> None | Asset:
        """Upgrade the rig by consuming a hardware patch asset. Return the provided asset if it is not the correct type."""
        if isinstance(hardware_patch, Asset) and hardware_patch.name == "Hardware Patch":
            self.__upgrade_level += 1
            self.__max_hp += 2
            self.__max_storage += 1
            self.__damage_counter = 0  # reset to zero
            print(f"...{self.__name} is upgraded to {self.__describe_condition()}. "
                  f"It now has {self.__max_storage} storage space and {self.__max_hp} damage tolerance.")
            return None
        else:
            print(f"...{self.__name} fails to upgrade; a hardware patch was not provided.")
            return hardware_patch

    def repair(self, crypto_token: Asset) -> Asset | None:
        """Repair the rig by consuming a CryptoToken. Return the provided asset if it is not the correct type."""
        if self.__damage_counter < self.__max_hp:
            print(f"...{self.__name} does not need a repair as it has no damage.")
        elif not (isinstance(crypto_token, Asset) and crypto_token.name == "CryptoToken"):
            print(f"...{self.__name} fails to repair; a CryptoToken was not provided.")
        else:
            self.__damage_counter = 0
            self.__broken_state = False
            print(f"...{self.__name} is repaired! {self.__describe_condition()}.")
            return None
        return crypto_token

    def generate_asset(self) -> None:
        """If storage space is available, alls the Asset class constructor to produce a random asset from the
         available list and stores it."""
        if self.__storage_capacity_available():
            new_asset = Asset()
            print(f"{self.__name} generates a {new_asset.name}.")
            self.store_asset(new_asset, self.__password)
        else:
            print(f"{self.__name} tries to generate an asset, but there is no storage space available.")

    def take_damage(self, asset: Asset) -> None:
        """
        Increase damage_counter by the damage dealt by the offensive asset.
        :param asset: The asset object used to attack the rig.
        :return: None
        """
        if isinstance(asset, Asset):
            initial_remaining_health = self.__max_hp - self.__damage_counter
            damage = asset.deal_damage()
            if initial_remaining_health <= 0:
                print(f"...{self.__name} continues to be broken.")
            else:
                self.__damage_counter += damage
                remaining_health = self.__max_hp - self.__damage_counter
                if remaining_health <= 0:
                    self.__broken_state = True
                    print(f"...{self.__name} is broken!")
                else:
                    print(f"...{self.__name} is {remaining_health} away from becoming broken.")

    def launch_data_spike(self, target, password: str = None) -> None:
        """
        Attack another Rig instance using a stored Data Spike if one is available.
        :param Rig target: The Rig object that will receive the attack damage.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: None
        """
        if not self.__access_authorized(password): return None

        if not isinstance(target, Rig):
            print(f"...{self.__name} fails to launch a data spike; the target was not a rig.")
        else:
            data_spike = self.retrieve_asset("Data Spike", password)
            if data_spike is None:
                print(f"...{self.__name} fails to launch a data spike; it cannot find one in storage.")
            else:
                print(f"...{self.__name} launches the data spike on {target.name}!")
                target.take_damage(data_spike)
        return None

    def encrypt_stored_asset(self, name: str, password: str = None) -> None:
        """
        Searches storage for an unencrypted asset by name and encrypts it if there is also a Security Chip in storage.
        :param name: The name of the asset to be encrypted.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: None
        """
        if not self.__access_authorized(password): return None

        matching_assets = self.__search_unencrypted_assets_by_name(name)
        if len(matching_assets) == 0:
            print(f"...{self.__name} fails to encrypt the asset; the asset is already encrypted or does not exist.")
        else:
            security_chip = self.retrieve_asset("Security Chip", password)
            if security_chip is None:
                print(f"...{self.__name} fails to encrypt the {name}; it cannot find a Security Chip in storage.")
            else:
                for asset in self.__storage:
                    if asset.name == name and not asset.encrypted:
                        asset.encrypt()
                        break
                print(f"...{self.__name} encrypts the {name} using 1 Security Chip.")
        return None

    def decrypt_stored_asset(self, name: str, password: str = None) -> None:
        """
        Searches storage for an encrypted asset by name and decrypts it if there is also a Security Chip in storage.
        :param name: The name of the asset to be decrypted.
        :param password: The password created by the owner of the rig when the rig was registered.
        :return: None
        """
        if not self.__access_authorized(password): return None

        matching_assets = self.__search_unencrypted_assets_by_name(name)
        if len(matching_assets) == self.__storage_counter:
            print(f"...{self.__name} fails to decrypt the asset; the asset is already decrypted or does not exist.")
        else:
            security_chip = self.retrieve_asset("Security Chip", password)
            if security_chip is None:
                print(f"...{self.__name} fails to decrypt the {name}; it cannot find a Security Chip in storage.")
            else:
                for asset in self.__storage:
                    if asset.name == name and asset.encrypted:
                        asset.decrypt()
                        break
                print(f"...{self.__name} decrypts the {name} using 1 Security Chip.")
        return None
