
def abs_err(n,m):
    """Return the absolute error in the approximation, m,
       of a scalar quantity, n"""
    return round(abs(n-m), 10)

def rel_err(n,m):
    """Return the relative error in the approximation, m,
       of a scalar quantity, n != 0"""
    try:
        return round(abs(n-m)/abs(n), 10)
    except:
        return "Invalid input"


def ster_approx(n):
    """Return the factorial of a number, its Sterling's
       approximation the absolute and relative errors"""
    from math import e, pi, sqrt, factorial
    
    try:
        Sn = sqrt(2*pi*n) * pow(n/e, n)
        return f"{n}!={factorial(n)}\t{Sn}\t{abs_err(factorial(n), Sn)}\t\
               {rel_err(factorial(n), Sn)}"
    except:
        return "Invalid input"


def polym_eval(x, *args):
    """Return the value from the nested evaluation of a polynomial of any degree.
       The first argument is the point, x, at which to evaluate;
       the remaining arguments are the coefficients of the polynomial
       entered in increasing order of degree"""
    #We apply Honer's rule
    n = len(args)
    p = args[n-1]
    for i in range(n-2, -1, -1):
        p = p * x + args[i]
    return p



if __name__ == "__main__":
    print(polym_eval(1, 5,1,2,3))


