import math

def main():
    A,B,V = map(int,input().split())
    return math.ceil((V-B)/(A-B))
print(main())