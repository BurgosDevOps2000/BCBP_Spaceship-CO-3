from game.components.powerups.power_ups import PowerUps
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUps):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)