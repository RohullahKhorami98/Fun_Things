class subnetting:
    def __init__(self,subnet, network_address) -> None:
        self.subnet = subnet
        self.network_address = network_address
    def to_binary(self, subnet, network_address):
        sublist = subnet.split(".")
        networklist = network_address.split(".")
        subbin = [bin(int(x))[2:].zfill(8) for x in sublist]
        networkbin = [bin(int(y))[2:].zfill(8) for y in networklist]
        return subbin, networkbin
    



if __name__ == "__main__":
    network_address = input()
    subnet = input()
    s = subnetting(subnet, network_address)
    subbin, networkbin = s.to_binary(subnet, network_address)
    print(networkbin,"\n",subbin)