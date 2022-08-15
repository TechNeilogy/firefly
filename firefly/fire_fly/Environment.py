from typing import Tuple
import numpy as np
import scipy.spatial as sps

from .Config import Config

from .Neighbor import Neighbor

from .FireFly import FireFly


class Environment:

    def __init__(
        self,
        config: Config
    ) -> None:

        self.config = config

        dimensions = 2 if self.config.two_d else 3

        self.points = np.random.uniform(0.0, 1.0, (config.count, dimensions))

        self.count = len(self.points)

        if self.config.two_d:
            self.d = np.random.uniform(0.2, 2.0, self.count)
        else:
            self.d = np.ones(self.count)

        self.f = np.random.uniform(0, 1.0, self.count)

        self.fire_flies = [
            FireFly(self.config, i) for i in range(self.count)
        ]

        kdtree = sps.KDTree(self.points[:, 0:dimensions])

        for i in range(self.count):

            kd = kdtree.query(
                self.points[i],
                k=self.config.neighbor_count,
                distance_upper_bound=self.config.neighbor_bound
            )

            fire_fly = self.fire_flies[i]

            for j in range(len(kd[0])):
                d = kd[0][j]
                ndx = kd[1][j]
                if ndx == i or ndx >= self.count:
                    continue
                fire_fly.neighbors.append(
                    Neighbor(
                        self.fire_flies[ndx],
                        d * fire_fly.donation 
                    )
                )

    def update(self) -> None:

        fired: list[FireFly] = []

        for fire_fly in self.fire_flies:
            if fire_fly.update():
                self.f[fire_fly.ndx] = 1.0
                fired.append(fire_fly)
            else:
                self.f[fire_fly.ndx] = max(self.f[fire_fly.ndx] - 0.02, 0)

        for fire_fly in fired:
            donation = fire_fly.donation
            for neighbor in fire_fly.neighbors:
                neighbor.fire_fly.charge += donation
