import math
"""
This module contains the `classCs` class, which is used for subnetting class C.
Attributes:
    subnet (str): The subnet mask of the network.
    network_address (str): The network address of the network.
    number_of_subnets (int): The number of subnets to be created.

Methods:
    to_binary(subnet, network_address)
        Converts the subnet and network address to binary.
    calculate_number_of_subnets(number_of_subnets)
        Calculates the number of bits needed to represent the number of subnets.
"""

class classCs:
    def __init__(self,subnet: str, network_address: str,number_of_subnets: int) -> None:
        self.subnet = subnet
        self.network_address = network_address
        self.number_of_subnets = number_of_subnets
    #### TO BINARY ####
    def to_binary(self, subnet, network_address):
        sublist = subnet.split(".")
        networklist = network_address.split(".")
        subbin = [bin(int(x))[2:].zfill(8) for x in sublist]
        networkbin = [bin(int(y))[2:].zfill(8) for y in networklist]
        return subbin, networkbin
    #### NUMBER OF SUBNETS ####
    def calculate_number_of_subnets(self, number_of_subnets):
        number_of_bits = math.log2(number_of_subnets)
        _ , network_bits = self.to_binary(self.subnet, self.network_address)
        bits = network_bits[:int(number_of_bits)]
        return bits
    