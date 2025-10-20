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
        return [asset for asset in self.__inventory if asset.encrypted != True]

    def __scan_inventory_by_name(self, name: str) -> list[Asset]:
        """Searches the Hacker's inventory for unencrypted assets by name, and returns a list of matches."""
        matches = []
        for asset in self.__get_unencrypted_assets():
            if asset.name == name:
                matches.append(asset)
        return matches

    def find_asset(self, asset: Asset) -> None:
        """
        Add an asset to inventory that is found/ exists outside Rig generation. [Used mainly for testing purposes.]
        :param asset: The asset object to be added to inventory.
        :return: None
        """
        if not isinstance(asset, Asset):
            print(f"{self.__name} thought they found an asset, but it turned out to be nothing special.\n")
        else:
            self.__inventory.append(asset)
            print(f"{self.__name} found an unclaimed {asset.name} and added it to their inventory.\n")

    def retrieve_asset(self, name: str) -> Asset | None:
        """
        Allows objects from other classes to take resources from the Hacker's inventory.
        :param name:The name of the asset which the hacker wishes to retrieve from their inventory.
        :return: Asset if an asset with a matching name is found in the Hacker's inventory which is unencrypted, otherwise nothing.
        """
        assets = self.__scan_inventory_by_name(name)
        if len(assets) == 0:
            print(f"{self.__name} fails to retrieve {name} from inventory;"
                  f" the {name} must be encrypted or does not exist.")
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
                  f"rig was actually something else.")
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

        print("")  # formatting
        return None

    def __increase_trace_level(self) -> None:
        """Increases a Hacker's trace level when they perform a risky action, and updates their 'is_exposed' status
        if the level reaches the trace threshold. A summary statement is outputted."""
        self.__trace_level += 1
        if self.__trace_level == self.__trace_threshold:
            self.__is_exposed = True
        print(f"...{self.__name}'s trace level increases as a result of this risky action: "
              f"{self.__name} is {self.__describe_trace_level()}.\n")

    def get_asset_from_rig(self, name: str, alt_rig: Rig = None) -> None:
        """
        Request a rig to retrieve an asset specified by name from its storage, and transfer the asset into
        personal inventory.
        :param name: The name of the asset to be transferred.
        :param alt_rig: (optional) The Rig instance from which the asset is to be transferred if not from the
        hacker's own Rig (default).
        :return: None
        """
        if self.__is_exposed:
            print(f"{self.__name} wants to transfer assets, but can't because they are too exposed.\n")
        else:
            if alt_rig is None and self.__rig is None:
                print(f"{self.__name} wants to transfer assets from their rig, "
                      f"but can't because ... they don't have a rig.\n")
            else:
                if alt_rig is None:
                    rig = self.__rig  # taking from own rig
                    print(f"{self.__name} tries to transfer a {name} from {rig.name}...")
                else:
                    rig = alt_rig  # taking from someone else's rig
                    print(f"{self.__name} tries to steal a {name} from {rig.name}...")
                self.__inventory.append(rig.retrieve_asset(name, self.__rig_password))
                # remove 'None' if that is what was returned:
                self.__inventory = [asset for asset in self.__inventory if asset is not None]
                self.__increase_trace_level()
        return None

    def extract_all_rig_assets(self, alt_rig: Rig = None) -> None:
        """
        Request a rig to retrieve all stored unencrypted assets, and transfer the assets into
        personal inventory.
        :param alt_rig: (optional) The Rig instance from which the assets are to be transferred if not from the
        hacker's own Rig (default).
        :return: None
        """
        if self.__is_exposed:
            print(f"{self.__name} wants to extract rig assets, but can't because they are too exposed.\n")
        else:
            if alt_rig is None and self.__rig is None:
                print(f"{self.__name} wants to extract all assets from their rig, "
                      f"but can't because ... they don't have a rig.\n")
            else:
                if alt_rig is None:
                    rig = self.__rig  # taking from own rig
                    print(f"{self.__name} tries to extract all assets from {rig.name}...")
                else:
                    rig = alt_rig  # taking from someone else's rig
                    print(f"{self.__name} tries to extract all assets from {rig.name}...")
                    removable_drive = self.retrieve_asset("Removable Drive")
                    if removable_drive is None:
                        print(f"{self.__name} fails to execute the extraction; "
                              f"they cannot find a Removable Drive in their inventory.\n")
                        return None
                self.__inventory += rig.retrieve_all_assets(self.__rig_password)
                # remove 'None' if that is what was returned:
                self.__inventory = [asset for asset in self.__inventory if asset is not None]
                self.__increase_trace_level()
        return None

    def store_asset_in_rig(self, name: str) -> None:
        """
        Retrieve an asset specified by name from inventory and transfer the asset into
        Rig storage.
        :param name: The name of the asset to be transferred.
        :return: None
        """
        if self.__is_exposed:
            print(f"{self.__name} wants to transfer assets, but can't because they are too exposed.\n")
        elif self.__rig is None:
            print(f"{self.__name} wants to transfer assets to their rig, "
                  f"but can't because ... they don't have a rig.\n")
        else:
            asset = self.retrieve_asset(name)
            if asset is not None:
                print(f"{self.__name} tries to transfer a {name} to {self.__rig.name}...")
                self.__rig.store_asset(asset, self.__rig_password)
                self.__increase_trace_level()
            else:
                print("")  # formatting
        return None

    def store_all_assets_in_rig(self) -> None:
        """
        Transfer as many inventory assets as possible into Rig storage.
        :return: None
        """
        if self.__is_exposed:
            print(f"{self.__name} wants to transfer assets, but can't because they are too exposed.\n")
        elif self.__rig is None:
            print(f"{self.__name} wants to transfer assets to their rig, "
                  f"but can't because ... they don't have a rig.\n")
        elif len(self.__get_unencrypted_assets()) == 0:
            print(f"{self.__name} wants to transfer assets to their rig, "
                  f"but can't because there are no unencrypted assets in their inventory.\n")
        else:
            print(f"{self.__name} tries to transfer all their assets to {self.__rig.name}...")
            rejected_asset = None
            transfer_count = 0
            while rejected_asset is None and len(self.__get_unencrypted_assets()) > 0:
                next_asset = self.__get_unencrypted_assets()[1].name
                rejected_asset = self.__rig.store_asset(self.retrieve_asset(next_asset), self.__rig_password)
                transfer_count += 1
            if rejected_asset is not None:
                self.__inventory.append(rejected_asset)
                transfer_count -= 1
            print(f"...{self.__name} successfully transferred {transfer_count} asset(s) to {self.__rig.name}")
            self.__increase_trace_level()
        return None

    def launch_data_spike(self, target_rig: Rig) -> None:
        """
        Uses the hacker's registered rig to attack another hacker's rig with a data spike.
        :param target_rig: The Rig object that will receive the attack damage.
        :return: None
        """
        if self.__is_exposed:
            print(f"{self.__name} wants to launch a data spike, but can't because they are too exposed.")
            return None
        if self.__rig is None:
            print(f"{self.__name} wants to launch a data spike from their rig, "
                  f"but can't because ... they don't have a rig.")
            return None
        print(f"{self.__name} attempts to use {self.__rig.name} to launch a data spike...")
        self.__rig.launch_data_spike(target_rig, self.__rig_password)
        self.__increase_trace_level()
        return None

    def lay_low(self) -> None:
        """Reduces hacker trace level by one if it is greater than zero, sets is_exposed status to False and
         asks the rig to generate an asset if it has storage space."""
        if self.__trace_level - 1 >= 0:
            self.__trace_level -= 1
            self.__is_exposed = False
        print(f"{self.__name} lays low to reduce their trace level to: {self.__describe_trace_level()}")

        if isinstance(self.__rig, Rig):  # rig generates a random asset as a result
            self.__rig.generate_asset()

        print("")

    def encrypt_inventory_asset(self, name: str) -> None:
        """
        Searches inventory for an unencrypted asset by name and encrypts it if there is also a Security Chip in inventory.
        :param name: The name of the asset to be encrypted.
        :return: None
        """
        matching_assets = self.__scan_inventory_by_name(name)
        if len(matching_assets) == 0:
            print(f"{self.__name} fails to encrypt an asset; the asset is already encrypted or does not exist.\n")
        else:
            security_chip = self.retrieve_asset("Security Chip")
            if security_chip is None:
                print(f"{self.__name} fails to encrypt the {name}; "
                      f"they cannot find a Security Chip in their inventory.\n")
            else:
                for asset in self.__inventory:
                    if asset.name == name and not asset.encrypted:
                        asset.encrypt()
                        break
                print(f"{self.__name} encrypts the {name} using 1 Security Chip.\n")
        return None

    def decrypt_inventory_asset(self, name: str) -> None:
        """
        Searches inventory for an encrypted asset by name and decrypts it if there is also a Security Chip in inventory.
        :param name: The name of the asset to be decrypted.
        :return: None
        """
        if len(self.__get_unencrypted_assets()) == len(self.__inventory):
            print(f"{self.__name} fails to decrypt the asset; the asset is already decrypted or does not exist.")
        else:
            security_chip = self.retrieve_asset("Security Chip")
            if security_chip is None:
                print(f"{self.__name} fails to decrypt the {name}; "
                      f"they cannot find a Security Chip in their inventory.")
            else:
                for asset in self.__inventory:
                    if asset.name == name and asset.encrypted:
                        asset.decrypt()
                        break
                print(f"{self.__name} decrypts the {name} using 1 Security Chip.")
        print("")  # formatting
        return None

    def encrypt_rig_asset(self, name: str) -> None:
        """
        Asks the owned rig to encrypt an asset in its storage.
        :param name: The name of the asset to be encrypted.
        :return: None
        """
        if self.__rig is None:
            print(f"{self.__name} wants to encrypt an asset stored in their rig, "
                  f"but can't because ... they don't have a rig.")
        else:
            print(f"{self.__name} attempts to use {self.__rig.name} to encrypt a stored {name}...")
            self.__rig.encrypt_stored_asset(name, self.__rig_password)
        print("")  # formatting
        return None

    def decrypt_rig_asset(self, name: str) -> None:
        """
        Asks the owned rig to decrypt an asset in its storage.
        :param name: The name of the asset to be encrypted.
        :return: None
        """
        if self.__rig is None:
            print(f"{self.__name} wants to decrypt an asset stored in their rig, "
                  f"but can't because ... they don't have a rig.")
        else:
            print(f"{self.__name} attempts to use {self.__rig.name} to decrypt a stored {name}...")
            self.__rig.decrypt_stored_asset(name, self.__rig_password)
        print("")  # formatting
        return None
