s =input("")
vc=0
cc=0
dc=0
for i in s:
    if i  in ['a','e','i','o','u']:
        vc+=1
    elif i in['0','1','2','3','4','5','6','7','8','9']:
        dc+=1
    elif i not in['a','e','i','o','u']:
        cc+=1
   
print(vc)
print(dc)
print(cc)