import classC as C
import argparse


if __name__ == "__main__":
    print("SUBNETTING Class C")
    network_address = input("Enter the network address: ")
    subnet = input("Enter the subnet: ")
    s = C.classCs(subnet, network_address)
    subbin, networkbin = s.to_binary(subnet, network_address)
    print(networkbin,"\n",subbin)