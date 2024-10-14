st = 0
end = 100
for c in range(st,end+1) :
    if c > 1 :
        for i in range(2,c) :
            if c % i == 0 :
                break
        else:
            print(c)