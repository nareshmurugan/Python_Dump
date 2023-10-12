from itertools import permutations

lst = list(range(1, 10))

n = 3
triplets = list(permutations(lst, n))
triplets = [set(x) for x in triplets]

def array_unique(seq):  
    checked = [] 
    for x in seq:
        if x not in checked: 
            checked.append(x) 
    return checked

triplets = array_unique(triplets)

result = []
m = n * 3
for x in triplets:
    for y in triplets:
        for z in triplets:
            if len(x.union(y.union(z))) == m:
                result += [[x, y, z]]

def groups(sets, i):
    result = [sets[i]]

    for x in sets:
        flag = True
        for y in result:
            for r in x:
                for p in y:
                    if len(r.intersection(p)) >= 2:
                        flag = False
                        break
                    else:
                        continue
                if flag == False:
                    break
        if flag == True:
            result.append(x)

    return result

for i in range(len(result)):
    print('%d:' % (i + 1))
    for x in groups(result, i):
        print(x)
