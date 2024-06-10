import math
from itertools import product
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
        bits = network_bits[-1][:int(number_of_bits)]
        return bits 
    def bit_combinations(self):
        length_bits = len(self.calculate_number_of_subnets(self.number_of_subnets))
        bin_list = [0,1]
        combo = list(product(bin_list, repeat=length_bits))
        bit_combo = ["".join(map(str,c)) for c in combo]
        return bit_combo
    def get_network_ranges(self):
        subbin, networkbin = self.to_binary(self.subnet, self.network_address)
        new_sub_combo = list()
        new_network_combo = list()
        bits = self.calculate_number_of_subnets(self.number_of_subnets)
        bit_combos = self.bit_combinations()
        for c in range(len(bit_combos)):
            temp = subbin[c][:-len(bits)]
            new_sub_combo.append(temp+bit_combos[c])
        print(new_sub_combo)
        return new_sub_combo
