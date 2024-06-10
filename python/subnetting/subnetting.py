import classC as C
import argparse

def info(Class_choice):
    print("SUBNETTING Class {}".format(Class_choice))
    network_address = input("Enter the network address: ")
    subnet = input("Enter the subnet: ")
    num_subnets = input("Enter the number of subnets: ")
    return (network_address, subnet, num_subnets)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='python subnetting.py -S <class> / --SubnetClass <class>',
        description='SUBNETTING class A, B, C',)
    parser.add_argument('-s','--SubnetClass' ,choices={'C':'ClassC','B':'ClassB','A':'ClassA'} , help='Select the class', type=str)
    args = parser.parse_args()
    
    if args.SubnetClass == 'A':
        print("SUBNETTING Class A")
    elif args.SubnetClass == 'B':
       print("SUBNETTING Class B")
    elif args.SubnetClass == 'C':
       # network_address, subnet, num_subnets = info(args.SubnetClass)
        subnet, network_address, num_subnets = "192.168.1.0", "255.255.255.0", 4
        s = C.classCs(subnet, network_address,num_subnets)
        subbin, networkbin = s.to_binary(subnet, network_address)
        print(networkbin,"\n",subbin)
        print(s.bit_combinations())
        print(s.calculate_number_of_subnets(num_subnets))
        get_network_ranges = s.get_network_ranges()
    else:
        print("Invalid Class")