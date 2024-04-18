"""
Author: EJ
Project 2
Date: 10/13
Description: This file defines the computer system classes,
that are inherited by Linux and Windows Classes. These are
used in the proceeding files.
"""
from abc import ABC, abstractmethod

"""
Parent class that sets basic computer variables and fucntions
"""
class ComputerSystem(ABC):
    def __init__(self, ip_address, year_purchase, operating_system):
        self.ip_address = ip_address
        self._year_purchase = year_purchase
        self.operating_system = operating_system

    @property
    def year_purchase(self):
        return self._year_purchase

    @abstractmethod
    def getSpace(self):
        pass

        """
        Linux class computer that inherits Computer System functions
        """
class Linux(ComputerSystem):
    def __init__(self, ip_address, year_purchase, operating_system, fs_space):
        super().__init__(ip_address, year_purchase, operating_system)
        self.fs_space = fs_space

    def getSpace(self):
        return self.fs_space
        """
        Windows class computer that inherits Computer System functions
        """
class Windows(ComputerSystem):
    def __init__(self, ip_address, year_purchase, operating_system, c_drive_space):
        super().__init__(ip_address, year_purchase, operating_system)
        self.c_drive_space = c_drive_space

    def getSpace(self):
        return self.c_drive_space

