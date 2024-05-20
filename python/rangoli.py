def print_rangoli(size):
    # your code goes here
   
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    pat = alph[:size]
    all = list()
    for i in range(size):
        temp = pat[i+1:size]
        all.append(temp[::-1]+pat[i:size])
    cha = list()
    for i in all:
        temp = (size * 2) - (len(i)+1)
        temp1 = []
        for j in range(temp):
            temp1.append("-")
        cha.append(temp1)
    mergedAll = list()
    for l in all:
        temp10 = "-".join(x for x in l)
        mergedAll.append(temp10)
  
    merged = list()
    for x,y in zip(mergedAll,cha):
        merged.append(y+[x]+y)
    mega = merged[::-1]+merged[1:size]
    
    for l in mega:
        print("".join(x for x in l))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
