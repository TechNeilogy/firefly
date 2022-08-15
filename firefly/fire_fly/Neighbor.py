from dataclasses import dataclass

from .FireFly import FireFly


@dataclass
class Neighbor:
    
    fire_fly: FireFly = None
    distance: float = 0.0