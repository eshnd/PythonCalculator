def calc():
    try:
        inp1 = input("What is the first number ('exit' to exit): ")
        if (inp1 == "exit"):
            return 0
        inp = float(inp1)
        inp2 = input("What is the operation: ")
        inp3 = float(input("What is the second number: "))

        match (inp2):
            case "+":
                print(inp + inp3)
            case "-":
                print(inp - inp3)
            case "/":
                print(inp / inp3)
            case "^":
                print(pow(inp,inp3))
            case "%":
                print(inp % inp3)
        return 1
    except:
        print("error!!!")
        return 1
while (True):
    if (calc()==0):
        exit()
