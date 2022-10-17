a = int(input("number one: "))
b = int(input("number two: "))
# verify that the second number is not zero

while b == 0:
    b = int(input("non zi può, dimmi number two: "))

# print result
print("the result is ", (a / b))

