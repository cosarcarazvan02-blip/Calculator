def read_number(prompt:str)-> float:
    while True:
        s=input(prompt).strip().replace(",",".")
        try:
            return float(s)
        except ValueError:
            print("Enter a valid number!")

def read_operator()->str:
    while True:
        op=input("Operator(+, -, *, / or q)").strip().lower()
        if op in {"+", "-", "*", "/", "q"}:
            return op
        else:
            print("Enter a valid operator!")
def calculate(a:float, b:float, op:str):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                return "Error"
            return a / b
def game():
    read_number()
    print("Calculator.Press q to exit")
    op=read_operator()
    while True:
        if op=="q":
            print("Goodbye!")
            break
    calculate()
    game()
        



