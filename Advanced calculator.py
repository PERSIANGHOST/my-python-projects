# ماشین حساب پیشرفته
#============================================================
import math
def calculator():
    print("Calculator") # ماشین حساب
    print("Possible operations:") # عملیات ریاضی
    print("plural = + ") # جمع
    print("subtraction = - ") # تفریق 
    print("multiplication = * ") # ضرب
    print("division = / ") # تفریق
    print("power = ** ") # توان
    print("Correct division = //")  # تقسیم صحیح
    print("the remainder = % ") # باقیمانده

    def get_input():
        try:
            num1 = float(input("enter your number : ")) # عدد را وارد کنید
            op = input("Enter mathematical operations  : ") # عملیات مورد نظر را وارد کنید
            num2 = float(input("enter your number : ")) # عدد را وارد کنید
        except ValueError:
            print("Please enter a valid number! .") # لطفا عدد معتبر وارد کنید
            return
    
        if op == "+":
            result = num1 + num2
        elif op == "-" :
            result = num1 - num2
        elif op == "*" :
            result = num1 * num2
        elif op == "/" :
            if num2 == 0 :
                print("Division by zero is not allowed.!") # تقسیم بر صفر مجاز نیست
                return
            result = num1 / num2
        elif op == "**" :
            result = num1 ** num2
        elif op == "//" :
            result = num1 // num2
        elif op == "%" :
            result = num1 % num2
        else :
            print("Invalid operation.") # عملیات نامعتبر
            return
        print("result :", result) # نتیجه
    get_input()
while True:
    calculator()
    again = input("Do you want to perform another operation? (y/n): ") # میخواهید ادامه دهید؟
    if again.lower() != "y" :
        print("sayonara!") # بدرود
        break

