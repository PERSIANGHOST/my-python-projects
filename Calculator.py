# ماشین حسلب ساده
#============================================================
# print(x)
# print(z)
# print(y)
#============================================================
while True:
    x = int(input("enter your number: "))
    z = input("enter operator ( / , * , - , + ): ")
    y = int(input("enter your number: "))
#============================================================
    if z == "+":
        result = x + y
    elif z == "-":
        result = x - y
    elif z == "*":
        result = x * y
    elif z == "/":
        if y != 0:
            result = x / y
        else :
            print("Cannot divide by zero!")
            continue
    print("Result:",result)
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice != "yes":
        break
