logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1,n2):
    return (n1+n2)
#print(add(5,2))
def sub(n1,n2):
    return (n1-n2)
#print(sub(5,2))  
def mul(n1,n2):
    return (n1*n2)
#print(mul5,2))
def div(n1,n2):
    return (n1/n2)
#print(div(5,2))
def power(n1,n2):
    return (n1**n2)
#print(power(2,3))
def calculator():
    dict={"+":add,"-":sub,"*":mul,"/":div,"**":power}
    n1=float(input(f"What's the first number?:"))
    for i in dict:
        print(i)
    q=True
    while q:
        l=input(f"pick an operation:")
        n2=float(input(f"What's the next number?:"))
        x=dict[l]
        answer=x(n1,n2)
        print(f"{n1}{l}{n2}={answer}")
        k=input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation:\n")
        if k=='y':
            n1=answer
        else:
            q=False
            print("thanks")
            #clear()
            calculator()

#main        
calculator()    
