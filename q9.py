def lbToKg(k):
    return round(k*0.45359237,2)

N = int(input())
l  = list(map(int, input().split()))
k=list()
for i in range(N):
    k.append(lbToKg(l[i]))
print(k)