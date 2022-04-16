num  = int(input("enrter a four digits number :" )
d4 = num%10
d3 = (num%100)//10
d2 = (num%1000)//100
d1 = num//1000
sum=(d1+d2+d3+d4)
print(sum)