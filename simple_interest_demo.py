# Simple Interest Calculator

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

si = simple_interest(p, r, t)
print("Simple Interest:", si)
