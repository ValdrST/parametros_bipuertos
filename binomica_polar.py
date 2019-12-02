import math
if __name__ == "__main__":
    binom = complex(input())
    r = math.sqrt(binom.real**2+binom.imag**2)
    alfa = math.atan(binom.imag/binom.real)
    
    print("{0} {1}°".format(r,math.degrees(alfa)))