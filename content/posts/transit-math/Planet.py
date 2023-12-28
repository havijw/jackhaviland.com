from dataclasses import dataclass

import numpy as np
from Star import CircleStar, RectStar, Star


@dataclass
class Planet:
    """
    Planet orbiting Star
    Period is 1.0, transit center time depends on init position
    For default init position (0, 0), transit center is 0.0
    """

    orbit_angle: float
    orbit_semi_major_axis: float
    orbit_inclination: float = 0.0
    orbit_eccentricity: float = 0.0
    orbit_periastron: float = 90.0
    position: tuple[float, float] = (0, 0)
    delta_t: float = 0.05
    _t: float = 0

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def step_position(self, time_steps: int = 1):
        """Mutates self"""
        for _ in range(time_steps):
            self._t += self.delta_t
            # TODO implement position logic

    def overlap(self, s: Star) -> float:
        raise NotImplementedError


@dataclass
class RectPlanet(Planet):
    width: float
    height: float

    def overlap(self, s: Star) -> float:
        if isinstance(s, RectStar):
            star_left = -s.width / 2
            star_right = s.width / 2
            star_top = s.height / 2
            star_bottom = -s.height / 2
            planet_left = self.x - self.width / 2
            planet_right = self.x + self.width / 2
            planet_top = self.y + self.height / 2
            planet_bottom = self.y - self.height / 2
            overlap_width = max(
                0, min(star_right, planet_right) - max(star_left, planet_left)
            )
            overlap_height = max(
                0, min(star_top, planet_top) - max(star_bottom, planet_bottom)
            )
            return overlap_width * overlap_height
        raise NotImplementedError


@dataclass
class CirclePlanet(Planet):
    radius: float

    def overlap(self, s: Star) -> float:
        if isinstance(s, CircleStar):
            # TODO this logic is from ChatGPT and needs to be verified
            distance_between_centers = np.sqrt(self.x**2 + self.y**2)
            if distance_between_centers >= self.radius + s.radius:
                # planet is completely outside star
                return 0
            elif distance_between_centers + min(self.radius, s.radius) <= max(
                self.radius, s.radius
            ):
                # planet is completely inside star (or vice-versa)
                return np.pi * min(self.radius, s.radius) ** 2

            self_r_sq = self.radius**2
            s_r_sq = s.radius**2
            d_sq = distance_between_centers**2

            angle1 = np.arccos(
                (self_r_sq + d_sq - s_r_sq)
                / (2 * self.radius * distance_between_centers)
            )
            angle2 = np.arccos(
                (s_r_sq + d_sq - self_r_sq) / (2 * s.radius * distance_between_centers)
            )

            area1 = 0.5 * angle1 * self_r_sq - 0.5 * self_r_sq * np.sin(2 * angle1)
            area2 = 0.5 * angle2 * s_r_sq - 0.5 * s_r_sq * np.sin(2 * angle2)

            return area1 + area2


def flux(s: Star, p: Planet, time_steps: int) -> float:
    def get_overlap_then_step(p: Planet, s: Star):
        overlap = p.overlap(s)
        p.step_position()
        return overlap

    return s.flux(time_steps) - sum(
        get_overlap_then_step(p, s) for _ in range(time_steps)
    )
