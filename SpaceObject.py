# -*- coding: utf-8 -*-
"""Define the SpaceObject class"""

import Vector


class SpaceObject:

    """Represent an object in space.

    Provide a base class which has the primary attributes and functions of any object that could be present in a space
    environment.
    """

    def __init__(self, location=None, velocity=None, mass=None, ):
        """Create SpaceObject

        """
