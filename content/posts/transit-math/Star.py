from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class Star:
    """
    Star centered at (0, 0)
    """

    limb_dark: Optional[str] = None
    limb_dark_coeffs: Optional[list[float]] = None

    def flux(self, time_steps: int = 1):
        raise NotImplementedError


@dataclass
class RectStar(Star):
    width: float
    height: float

    def flux(self, time_steps: int = 1):
        if self.limb_dark is None:
            return time_steps * self.width * self.height
        raise NotImplementedError


@dataclass
class CircleStar(Star):
    radius: float

    def flux(self, time_steps: int = 1):
        if self.limb_dark is None:
            return time_steps * np.pi * self.radius**2
        raise NotImplementedError
