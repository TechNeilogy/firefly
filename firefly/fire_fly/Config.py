from dataclasses import dataclass


@dataclass
class Config:

    count: int = 500
    two_d: bool = True
    neighbor_count: int = 40
    neighbor_bound: float = 0.2
    donation_level: float = 20
    color_highlight: bool = False