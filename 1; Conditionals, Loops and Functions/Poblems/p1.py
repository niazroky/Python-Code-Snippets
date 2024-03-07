import math

def is_rational(num):
    root = num ** 0.5
    if root.is_integer():
        return True
    else:
        return False

num = int(input("Enter an integer: "))
if is_rational(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")