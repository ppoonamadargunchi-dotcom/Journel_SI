import sys
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

if __name__ == "__main__":
    p = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple interest: ",simple_interest(p,r,t))