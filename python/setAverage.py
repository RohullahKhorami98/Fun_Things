def average(array):
    # your code goes here
    orderedArray = set(array)
    return sum(orderedArray)/len(orderedArray)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)