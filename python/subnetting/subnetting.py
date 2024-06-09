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
        network_address, subnet, num_subnets = info(args.SubnetClass)
        s = C.classCs(subnet, network_address,num_subnets)
        subbin, networkbin = s.to_binary(subnet, network_address)
        print(networkbin,"\n",subbin)
    else:
        print("Invalid Class")