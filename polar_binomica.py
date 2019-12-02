import math
if __name__ == "__main__":
    print("escalar")
    e = float(input())
    print("grados")
    g = float(input())
    a = e * math.cos(math.radians(g))
    b = e * math.sin(math.radians(g))
    
    print("{0} {1}j".format(a,b))