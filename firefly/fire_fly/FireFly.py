import numpy as np

from .Config import Config


class FireFly:
    
    def __init__(
        self,
        config: Config,
        ndx: int
    ) -> None:

        self.ndx = ndx
        
        self.threshold = np.random.uniform(
            0.99, 
            1.01
        )

        increment_scale = 0.001

        self.increment = np.random.uniform(
            self.threshold * 0.9 * increment_scale,
            self.threshold * 1.1 * increment_scale
        )

        self.donation = self.increment * config.donation_level

        self.charge = np.random.uniform(
            0, 
            self.threshold
        )

        from .Neighbor import Neighbor

        self.neighbors: list[Neighbor] = []

        self.fired = 0

    def __repr__(self) -> str:

        return f'{self.threshold}|{self.increment}'

    def update(
        self
    ) -> bool:
        
        self.charge += self.increment
        
        if self.fired < 1 and self.charge > self.threshold:
            self.fired = 8
            while self.charge > self.threshold:
                self.charge -= self.threshold
            self.threshold = np.random.uniform(
                0.99, 
                1.01
            )
        else:
            self.fired = max(self.fired - 0.1, 0)

        return self.fired > 6