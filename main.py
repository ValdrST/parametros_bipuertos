import numpy as np

if __name__ == "__main__":
    print("Z11")
    z11 = complex(input())
    print("Z12")
    z12 = complex(input())
    print("Z21")
    z21 = complex(input())
    print("Z22")
    z22 = complex(input())

    z = [[z11,z12],[z21,z22]]
    deltaz= z11*z22 - z12*z21
    print("[Z]")
    print(np.array(z))
    y = (1/deltaz)*np.array([[z22,-z12],[-z21,z11]])
    print("[Y]")
    print(y) 
    h = np.array([[deltaz/z22,-z21/deltaz],[-z21/deltaz,1/z22]])
    print("[h]")
    print(h)
    g = (1/z11)*np.array([[1,-z12],[z21,deltaz]])
    print("[g]")
    print(g)
    T = (1/z21)*np.array([[z11,deltaz],[1,z22]])
    print("[T]")
    print(T)