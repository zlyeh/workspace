for i in range (1,51,2):
    totalP = 0
    numP = pow(i, 2)
    totalP = totalP + numP

print('---------------------------------------')

for i in range(2, 51, 2):
    totalM = 0
    numM = pow(i, 2)
    totalM = totalM + numM

print('奇數和=', totalP)
print('偶數和=', totalM)

print(totalP-totalM)

