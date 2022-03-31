import datetime                    #time library, to get Real Date information.
import os                          #Operating system to provide cross-platform compatibility

foods = []                    #Variable List of foods, names + prices.
drinks = []                   #Variable List of drinks, names + prices.
services = []                 #Variable List of other services, names + prices.

prices = [0] * 100        #Variable List of prices. 

var_discount_1 = 200                      #First discount starts.
var_discount_2 = 500                     #Second discount starts.
var_discount_3 = 1000                     #Third discount starts.
var_discount_1_rate = 0.05                #First discount rate.
var_discount_2_rate = 0.10                #Second discount rate.
var_discount_3_rate = 0.15                #Third discount rate.

navigator_symbol = "/" # This will make the program runnable on any unix based enviroument. 
if os.name == "nt":
    navigator_symbol = "\\" # This will make the program runnable on Windows.
    
# create list
    def def_default():
    global drinks, foods, services, price, list_item_order    
    list_item_order = [0] * 100       #list, length 100. Max index number is 99.Index: 0-39 for foods, index: 40-79 for drinks,Index: 80-99 for other services.
def_default()                                      
                                            
#Design for Main Menu. 
def main():
    while True:
        print("*" * 28 + "RESTAURANT ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     #"*" * 31 means, write (*) 31 times.
              "\n(O) ORDERMEAL   (R) REPORT (C) CANCEL  (P) PAY (E) EXIT\n" + "_" * 72)
            
        input1 = str(input("Please Select Your Operation: ")).upper()   #Input to choose operation. Make everything UPPER case. 
        if (len(input1) == 1):            #Checking input length.                               
            if (input1 == 'O'):                                          
                print("\n" * 10)                                        
                ordermeal()        #call the ordermeal function.                                  
                break
            
            elif (input1 == 'R'):                                        
                print("\n" * 10)                                        
               report()           #call the report function.                           
                break
            
            elif (input1 == 'c'):                                        
                print("\n" * 10)
                cancelorder()   #call the cancelorder function.                                  
                break
            
            elif (input1 == 'P'):                                        
                print("\n" * 10)                                         
                pay()        #call the pay function.                                      
                break
            
            elif (input1 == 'E'):                                        
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")           
                break
            
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input1) + "). Try again!")  #If O, R, P, E not inserted then Invalid input error meaasge is displayed.
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input1) + "). Try again!") #If input length not equal to 1 then Invalid input error message is displayed.

#Design for ordermeal menu.
 def def_ordermeal():                                            
    while True:                                             
        print("*" * 31 + "ORDERS MENU" + "*" * 31 + "\n"     
              "\n(F) FOODS (D)  DRINKS  (s) SERVICES  (C) CANCEL (M) MAIN MENU (E) EXIT\n" + "_" * 72) # ordermeals and services Menu Structure

        input2 = str(input("Please Select Your Operation: ")).upper() 
        if len(input2) == 1:
            if (input2 == 'F'):  
                print("\n" * 10)
                foodmenu() # Show Food Menu
                break
            
            elif (input2 == 'D'):
                print("\n" * 10)
                drinksmenu() # Show drinks Menu
                break
            
             elif (input1 == 'c'):                                        
                print("\n" * 10)
                cancelorder()   #call the cancelorder function.                                  
                break
            
            elif (input2 == 'S'):
                print("\n" * 10)
                services() # Show Services Menu
                break
            
            elif (input2 == 'M'):
                print("\n" * 10)
                main() # Show Main Menu
                break
            
            elif (input2 == 'E'):
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")
                break
            
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input2) + "). Try again!")   
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input2) + "). Try again!")
            
# foods menu.             
  def foodmenu():
    while True:
            print("*" * 26 + "ORDER FOODS" + "*" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|") #  foods Menu Structure
            foodmenu = open('files'+navigator_symbol+'foods.fsd', 'r').read() 
        print(foodmenu)

            i = 0
            while i < len(foods):
                var_space = 1
                if i <= 8:                     
                    var_space = 2

                if i < len(foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(foods[i]) + "  | "
                else:
                    food = " " * 36 + "| " # 36 is a constant for indention in console to fixup list in print
                print(food)
                i += 1

            print("\n (M) MAIN MENU  (D)  DRINKS (s) SERVICES (C) CANCEL (P) PAY (E) EXIT\n" + "_" * 72)

            input1 = input("Please Select Your Operation: ").upper() 
            if (input1 == 'M'):
                print("\n" * 10)
                main() # call main function.
                break
            
             elif (input1 == 'D'):
                print("\n" * 10)
                drinksmenu() # Show drinks Menu
                break
            
            elif (input1 == 'S'):
                print("\n" * 10)
                services() # Show Services Menu
                break
            
             elif (input1 == 'c'):                                        
                print("\n" * 10)
                cancelorder()  #call the cancelorder function.                                  
                break
            
            elif (input1 == 'P'):
                print("\n" * 10)
                pay() # Handling payment call pay function.
                break
            
            else (input1 == 'E'):
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")
                break
try: # encapsulate errors  with try/except
input2 = input("no of orders ").upper() 
    if int(input2>=0) and (int(input2)<40)
    list_item_order[int(input1) - 1] += int(input2) 
    print("\n" * 10)
    print("Successfully Ordered!")
    foodmenu() # Return foods Menu
    break
    else:
    print("\n" * 10 + "ERROR: Invalid Input (" + str(input2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input1) + "). Try again!")
                
# drinks menu.             
def drinksmenu():
    while True:
            print("*" * 26 + "ORDER BEVERAGES" + "*" * 26)
            print(" |NO| |DRINKS NAME|         |PRICE|") # drinks Menu Structure
            drinksmenu = open('files'+navigator_symbol+'drinks.fsd', 'r').read() 
        print(drinksmenu)

            i = 0
            while i < len(drinks):
                var_space = 1
                if i <= 8:                     
                    var_space = 2

                if i < len(drinks):
                    drinks = " (" + str(i + 1) + ")" + " " * var_space + str(drinks[i]) + "  | "
                else:
                   drinks = " " * 36 + "| " 
                print(drinks)
                i += 1

            print("\n (M) MAIN MENU  (F)  FOODS (s) SERVICES (C) CANCEL (P) PAY (E) EXIT\n" + "_" * 72)

            input1 = input("Please Select Your Operation: ").upper() 
            if (input1 == 'M'):
                print("\n" * 10)
                main() # call main function.
                break
            
             elif (input1 == 'F'):
                print("\n" * 10)
                foodmenu() # Show foods Menu
                break
            
            elif (input1 == 'S'):
                print("\n" * 10)
                services() # Show Services Menu
                break
            
             elif (input1 == 'c'):                                        
                print("\n" * 10)
                cancelorder()  #call the cancelorder function.                                  
                break
            
            elif (input1 == 'P'):
                print("\n" * 10)
                pay() 
                break
            
            else (input1 == 'E'):
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")
                break
try:
    input2 = input("no of orders ").upper() 
    if int(input2>=40) and (int(input2)<80)
    print("\n" * 10)
    print("Drink Successfully Ordered!" + str(list_services[int(input_1) - 41]))
    list_item_order[int(input1) - 1] += int(input2)
    drinksmenu() # Return drinks Menu
    break
    else:
    print("\n" * 10 + "ERROR: Invalid Input (" + str(input2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input1) + "). Try again!")

# services menu.             
def services():
    while True:
            print("*" * 29 + "OTHER SERVICES" + "*" * 29)
            print(" |NO| |SERVICE NAME|      |PRICE|")  # Services Menu Structure
            servicesoffered = open('files'+navigator_symbol+'services.fsd', 'r').read() 
        print(servicesoffered)

            i = 0
            while i < len(services):
                var_space = 1
                if i <= 8:                     
                    var_space = 2

                if i < len(services):
                    services= " (" + str(i + 1) + ")" + " " * var_space + str(services[i]) + "  | " 
                else:
                   services = " " * 36 + "| " 
                print(services)
                i += 1

            print("\n (M) MAIN MENU  (C) CANCEL (P) PAY (E) EXIT\n" + "_" * 72)

            input1 = input("Please Select Your Operation: ").upper() 
            if (input1 == 'M'):
                print("\n" * 10)
                main() 
                break
            
             elif (input1 == 'c'):                                        
                print("\n" * 10)
                cancelorder()                                   
                break
            
            elif (input1 == 'P'):
                print("\n" * 10)
                pay() 
                break
            
            else (input1 == 'E'):
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")
                break
try:
    int(input2)
    if int(input2>= 80) and (int(input2) < 100):
    print("\n" * 10)
    print("Service Successfully Ordered!"+ str(list_services[int(input_1) - 81])) # Adding services to orders array 
    list_item_order[int(input_1) - 1] = 1 
    services() # Return services Menu
    break
    else:
    print("\n" * 10 + "ERROR: Invalid Input (" + str(input2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input1) + "). Try again!")
                
# cancel order               
def cancelorder()
        while True:
        print("*" * 28 + "CALCEL THE ORDER?" + "*" * 24 + "\n") 
        print("\n(O) ORDERMEAL   (R) REPORT (E) EXIT\n" + "_" * 72)
            
        input1 = str(input("Please Select Your Operation: ")).upper()   #Input to choose operation. Make everything UPPER case. 
        if (len(input1) == 1):            #Checking input length.                               
            if (input1 == 'O'):                                          
                print("\n" * 10)                                        
                ordermeal()        #call the ordermeal function.                                  
                break
            
            elif (input1 == 'R'):                                        
                print("\n" * 10)                                        
               report()           #call the report function.                           
                break
            
            elif (input1 == 'E'):                                        
                print("*" * 32 + "THANK YOU AND COME AGAIN " + "*" * 31 + "\n")           
                break
            
            else: print ("*" * 32 + "CANCEL THE ORDER" + "*" * 31 + "\n")

 # file reports menu.                
def report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        file_report = open('files'+navigator_symbol+'report.fsd', 'r').read() # Reading out reports from report.fsd
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            main() # back to main menu
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU AND COME AGAIN" + "*" * 31 + "\n") # Exit and break up the loop
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

# payment menu. ###
def pay():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_order): #Enumarating order array items and summing up its prices * quantities
            if(list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(foods[i]) + "  x  " + str(list_item_order[i]) # string appending the formated food name and formated order structure from quantity and final price
                    print(" " * 17 + str(foods[i]) + "  x  " + str(list_item_order[i])) #print it out
                    total_price += price[i] * list_item_order[i] # Calculating the total price for food
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(drinks[i - 40]) + "  x  " + str(list_item_order[i])
                    print(" " * 17 + str(drinks[i - 40]) + "   x  " + str(list_item_order[i]))
                    total_price += list_item_price[i] * list_item_order[i] # Calculating the total price for drinks
                if (i >= 80) and (i < 100):
                    report_new += "\n" + " " * 17 + str(services[i - 80])
                    print(" " * 17 + str(services[i - 80]))
                    total_price += list_item_price[i] * list_item_order[i] # Calculating the total price for services
                i += 1
            else:
                i += 1
                
### Applying Discounts Ruless
        if total_price > var_discount_3: 
            total_price -= total_price * var_discount_3_rate  ### To Be Implemented Further
            
main() # Execute Main menu Loop