#author__uy_thea
#date_Septermber_25_2024

#this program will calculate the missing component from the ohm's law
#Ask the user what they want to calculate: Voltage, Current, or Resistance.
#Based on their choice, prompt the user to input the appropriate values.
#Use Ohm's Law to calculate the missing variable and display the result.
#Handle cases where division by zero might occur.

while True: #set a loop for the entire program
    
    while True:
        try:
            component = input("Enter the component you want to calculate:\nV = Voltage\nI = Current\nR = Resistance\nAnswer: ") #ask the user for the component they want to calculate
            component = component.upper() #convert the answer of the user to uppercase
            
            if component == "V": #if the user is missing the value for the voltage, this block of code will execute
                try:
                    current = float(input("Enter the value of current: "))
                    resistance = float(input("Enter the value of resistance: "))
                    voltage = round((current*resistance),2)
                    print(f"Voltage = {voltage} volts")
                    break
                except ValueError:
                    print("Invalid Input")
                    continue


            elif component == "I": #if the user wants to calculate the value for the current, this block of code will execute
                try:
                    voltage = float(input("Enter the value of voltage: "))
                    resistance = float(input("Enter the value of resistance: "))
                    current = round((voltage/resistance),2)
                    print(f"Current = {current} amps")
                    break
                except:
                    print("Invalid Input")
                    continue

            elif component == "R": #if the user if missing the value for the resistance, this block of code will execute
                try:
                    voltage = float(input("Enter the value of voltage: "))
                    current = float(input("Enter the value of current: "))
                    resistance = round((voltage/current),2)
                    print(f"Resistanc = {resistance} ohms")
                    break
                except:
                    print("Invalid Input")
                    continue
    
        except ValueError:
            print("Invalid Input")
            continue
        print("\n")

                
    while True: #ask the user if they want to try again
        ans = str(input("Do you want to try again? Yes or No: "))
        upper_ans = ans.upper()
        if upper_ans == "YES":
            break
        elif upper_ans == "NO":
            print("\nThank you for using my program!")
            exit()
        else:
            print("Invalid Input")   
