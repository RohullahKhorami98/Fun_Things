from collections import Counter
X = int(input())
sizelist = Counter(map(int, input().split()))
customer = int(input())
counter = 0
for i in range(customer):
    size, price = map(int, input().split())
    if sizelist[size]:
        sizelist[size] -= 1
        print(sizelist)
        counter+=price
print(counter)