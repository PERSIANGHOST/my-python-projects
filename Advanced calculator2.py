class Calculator:
    def __init__(self):
        self.num1= self.get_number("enter your first number  : ")
        self.num2= self.get_number("enter your second number  : ")
        self.op = input ("enter your operate  ( + - * / ** // % ) : ")

    def get_number(self, prometr):
        while True:
            try:
                return int(input(prometr))
            except ValueError:
                print("Invalid input! Please enter a number.")

    
    @property
    def  operate(self):    
        """
        This method is for performing mathematical operations.  |   این متد برای انجام عملیات های ریاضی هستش
        """
        if self.op == "+":
            return self.num1 + self.num2
        elif self.op == "-":
            return self.num1 - self.num2
        elif self.op == "*":
            return self.num1 * self.num2
        elif self.op == "/":
            if self.num2 == 0:
                return "Division by zero is not allowed!!!"
            return self.num1 / self.num2
        elif self.op == "**":
            return self.num1 ** self.num2
        elif self.op == "//":
            if self.num2 == 0:
                return "Division by zero is not allowed!!!"
            return self.num1 // self.num2
        elif self.op == "%":
            if self.num2 == 0 :
                return "Division by zero is not allowed!!!"
            return self.num1 % self.num2
        else:
            return "Invalid operation!"
        
while True:
    calc = Calculator()
    print('Result : ', calc.operate)
    again = input("Do you want to try again? (y/n): ").lower()
    if again != "y":
        print("sayonara!!!")
        break

