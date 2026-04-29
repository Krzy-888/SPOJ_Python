# https://pl.spoj.com/problems/RNO_DOD/

t = int(input())
for i in range(t):
    n = int(input())
    lista_liczb = list(map(int,input().split()))
    print(sum(lista_liczb))