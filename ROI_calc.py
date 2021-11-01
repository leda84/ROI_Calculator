# create a program that will calculate the Return on Investment(ROI) for a rental property.


class ROICalc():

    def __init__(self):
        pass
        


    def expenses(self):
        while True:
            input("Hit ENTER to calculate monthly expenses. Enter 'q' at any time to quit.  ")

            tax = input("\nHow much is your monthly tax on the property? (round up to whole dollar) ")
            if tax.lower() == "q":
                break
            elif tax.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            insurance = input("\nHow much are you paying on insurance monthly? (round up to whole dollar) ")
            if insurance.lower() == "q":
                break
            elif insurance.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue

            utilities = input("\nIf your tenant will not be covering utilities, about how much will you pay per month? (round up to whole dollar) ")
            if utilities.lower() == "q":
                break
            elif utilities.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue

            snowLawn = input("\nHow much will you put aside monthly to cover Lawn Care & Snow Removal? (round up to whole dollar) ")
            if snowLawn.lower() == "q":
                break
            elif snowLawn.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue

            hoafees = input("\nHow much are your monthly HOA fees? (enter 0 if not applicable) (round up to whole dollar) ")
            if hoafees.lower() == "q":
                break
            elif hoafees.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            vacancy = input("\nHow much will you be putting aside each month to cover for future vacancy? (round up to whole dollar) ")
            if vacancy.lower() == "q":
                break
            elif vacancy.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            repairs = input("\nHow much would you like to set aside monthly for future repairs? (round up to whole dollar) ")
            if repairs.lower() == "q":
                break
            elif repairs.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            capex = input("\nHow much would you like to put aside monthly for CapEx? new roof, windows, etc... (round up to whole dollar) ")
            if capex.lower() == "q":
                break
            elif capex.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            propmang = input("\nHow much will you be spending monthly on property management? (round up to whole dollar) ")
            if propmang.lower() == "q":
                break
            elif propmang.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            mortgage = input("\nHow much is your monthly mortgage? (round up to whole dollar) ")
            if mortgage.lower() == "q":
                break
            elif mortgage.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            
            total = int(tax) + int(insurance) + int(utilities) + int(hoafees) + int(snowLawn) + int(vacancy) + int(repairs) + int(capex) + int(propmang) + int(mortgage)
            print(f"\nYour total monthly expenses are: ${total} \n")
            break


    def cashflow(self):
        while True:
            answer = input("\nTo calculate cash flow, you will need to know your monthly expenses." "\nDo you know your monthly expenses? (yes/no or 'q' to quit) ")
            if answer.lower() == 'q':
                break
            elif answer.lower() == 'no':
                self.expenses()
                break #so that when you break out of expenses, you won't be returned back to this
            elif answer.lower() == 'yes':
                pass
            else: # used in case they input anything other than 'q' 'yes' or 'no'
                continue

            expenses = input("\nHow much are your monthly expenses? (round up to whole dollar) ") 
            if expenses.lower() == "q":
                break
            elif expenses.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue

            rent = input("\nHow much will you be charging for rent on the property? (round up to whole dollar) ")
            if rent.lower() == "q":
                break
            elif rent.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue

            cashflow = int(rent) - int(expenses)

            print(f"\nYour monthly cashflow is: ${cashflow} \n")
            break
            
        
    def roi(self):
        while True:
            answer = input("\nTo calculate ROI, you will need to know your monthly cashflow." "\nDo you know your monthly cashflow? (yes/no or 'q' to quit) ")
            if answer.lower() == 'q':
                break
            elif answer.lower() == 'no':
                self.cashflow()
                break
            elif answer.lower() == 'yes':
                pass
            else: # used in case they input anything other than 'q' 'yes' or 'no'
                continue

            cashflow = input("\nEnter your monthly cash flow (round up to whole dollar): ")
            if cashflow.lower() == "q":
                break
            elif cashflow.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            downPayment = input("\nEnter your down payment (round up to whole dollar): ")
            if downPayment.lower() == "q":
                break
            elif downPayment.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            closing = input("\nEnter your closing costs (round up to whole dollar): ")
            if closing.lower() == "q":
                break
            elif closing.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            rehab = input("\nEnter your rehab budget (round up to whole dollar): ")
            if rehab.lower() == "q":
                break
            elif rehab.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            misc = input("\nEnter any other miscellaneous investments to property (round up to whole dollar): ")
            if misc.lower() == "q":
                break
            elif misc.isdigit() == False:
                print("Please enter a number")
                # TO TAKE USER BACK TO ENTER A NUMBER
                continue
            
            total_investment = int(downPayment) + int(closing) + int(rehab) + int(misc)
            print(f"\n\nYour Total Investment is: ${total_investment}")
            annual_cashflow = int(cashflow) * 12
            print(f"Your Annual Cashflow is: ${annual_cashflow}")
            roi = (annual_cashflow/total_investment) * 100
            print(f"Your Cash on Cash Return On Investment is: {roi}% per year \n\n")
            break








# created object with class roicalc
my_calc = ROICalc()


# Creating function to run the calculator

def runCalc():
    while True:
        action = input("\nWhat would you like to do? (enter a number)" "\n\t 1. Calculate Monthly Expenses" "\n\t 2. Calculate Monthly Cashflow"  "\n\t 3. Calculate ROI" "\n\t 4. Quit" "\n")

        if int(action) == 4:
            print("Thank you for using the calculator!")
            break

        elif int(action) == 1:
            my_calc.expenses()

        elif int(action) == 2:
            my_calc.cashflow()

        elif int(action) == 3:
            my_calc.roi()



runCalc()

