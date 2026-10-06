def get_input():
    # keep asking until the user enters it right
    while True:
        try:
            # get input and split it by /
            x,y = input("Enter in x/y:   ").split('/')
            x_int,y_int = int(x),int(y)
            
            #Defensive coding(Learned from CS50)
            try:
                if x_int > y_int:
                    print("X cannot be greater than y")
                elif y_int == 0:
                    print("Y cannot be zero")
                else:
                    return x_int,y_int
            except ZeroDivisionError:
                print("Cannot divide by zero")
            
        except ValueError:
            print("Please enter in integer")

def output(x,y):
    # calculate percentage
    percent = x/y * 100
    
    # print E for empty and F for full, rounded to no decimal places
    if percent <= 1:
        print(f"{percent:.0f}%","E")
    elif percent == 50:
        print("H")
    elif percent >= 99:
        print(f"{percent:.0f}%","F")
    else:
        print(f"{percent:.0f}%")

def main():
    a,b = get_input()
    output(a,b)

if __name__=="__main__":
    main()