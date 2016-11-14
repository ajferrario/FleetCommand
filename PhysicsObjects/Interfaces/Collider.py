# -*- coding: utf-8 -*-
"""Define the Collider Interface"""

import abc


class Collider(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def detect_collision(self):
        """Detects whether another object is occupying the same space as this object"""
