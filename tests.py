from Asset import Asset
from Hacker import Hacker
from Rig import Rig

charlie = Hacker("Charlie")
alex = Hacker("Alex")
rig1 = Rig("Rig1")
rig2 = Rig("Rig2")
charlie.acquire_rig(rig1, "charli3L0VESbananas3332!!")
alex.acquire_rig(rig2, "14slytherinLemonzzz@")

charlie.get_asset_from_rig("Data Spike")  # valid
