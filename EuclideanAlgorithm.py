a = int(raw_input("Input a: "))
b = int(raw_input("Input b: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print "GCD(a, b) = ", a

