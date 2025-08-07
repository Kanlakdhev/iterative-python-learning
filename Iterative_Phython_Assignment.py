""" Programming Fundamentals (COSC2531)  Assignment 1    NAME:Devendran kannan   STUDENT_ID:4131740 I have attempted the PART 3 completely 
   The design of the program is to create the menu option for booking the apartment , get the necessary details from the user(guest) and retrieve & display the given output based on the case study
   To implement the design,1)using multiple functions for handling each menu option and calling the menu function(output) in each function 2)using while loop for getting  multiple inputs and if-else conditions for checking the given condition
   3)using dictionary over list to access the datas easily by using a key 4)mathematical calculation example:total_cost,sub_cost,reward_points

   Challanges faced:1)difficult to break the nested while loop by using break statement 2) took a long time to understand the part of extrabed concept in  the given case study 
   3) thinking a logic for creating history dictionary was extremely hard .

"""




#intialized given data in dictionary with respect to supplementary items, apartments and guests. 
Apartments = {"U12swan": [95.0, 2], "U209duck": [106.7, 3], "U49goose": [145.2, 4]}
Guests = {"Alyssa": 20, "Luigi": 32}
suppl = {"car_park": 25, "breakfast": 21, "toothpaste": 5, "extra_bed": 50}
#for saving supplementary items,intialized empty list
supplementary_items = []
#for storing guests order history , assigns history as dictionary
history = {}
#This function display the menu options and reads the choice of menu from the user
def output():
    print("=" * 57)
    print("Welcome to Pythonia Service Apartments!")
    print("1) Make a booking")
    print("2) Add/update information of an apartment unit")
    print("3) Add/update information of a supplementary item")
    print("4) Display existing guests")
    print("5) Display existing apartment units")
    print("6) Display existing supplementary items")
    print("7) Display a guest booking and order history")
    print("0) Exit the program")
    print("=" * 57)
    print("Enter a number to choose an option:")
    #getting a input for the user
    choice = input()
    #based on the choice ,it calls the respective function
    if choice == "1":
        make()
    elif choice == "2":
        add_apart()
    elif choice == "3":
        add_supp()
    elif choice == "4":
        display_guests()
    elif choice == "5":
        display_apart()
    elif choice == "6":
        display_supp()
    elif choice == "7":
        display_booking_history()
    elif choice == "0":
        exit() #it exits from the overall program
    else:
        
        output()#it calls the function recursively other than [0,1,2,3,4,5,6,7]
#this function makes a booking with required inputs
def make():
    print("Making a booking")

    #it checks the guest name until the guest name is valid
    while True:
        Guest = input("Please enter the guest name: ")
        if Guest.isalpha():#if guest name is valid ,it should contain alphabet characters
            break #once the correct name is given,it breaks the while loop
        else:
            print("error: name must contain only alphabetic characters.")

    print("Please enter the number of guests")
    Number = int(input())#getting no of guests as int data type in numeric format.

    #it checks whether the apartment exists
    while True:
        print("Please enter the Apartment id (e.g., U12swan)")
        Apartment_id = input()
        #if the apartment id is unavailable,it prints the error prompt
        if Apartment_id not in Apartments:
            print("error: apartment ID not available")
        
        else:
            rate = Apartments[Apartment_id][0]
            capacity = Apartments[Apartment_id][1]
            print(f"The selected unit rate is ${rate:.2f}")#if apartment exists,prints the rate and capacicty 
            break#it breaks the current while loop
    #prints the warning prompt for excessing the no of guests above the given capacity
    if Number > capacity:
        print("Warning,Please consider ordering an extra bed")

   
    extrabed_capacity = 0
#this while loop gets the input of extrabed and quantity of it and runs until the 
    while Number > (capacity + extrabed_capacity):
        print("Supplementary items")
        #this while loop runs until the character(y/n) is given correctly by the user
        while True:
            print("Do you want to order an extra bed? (y/n)")
            ch = input()
            if ch == "y":
                while True:#this while loop runs until the quantity is other than  1 or 2
                    quantity = int(input("Enter the desired quantity of extra beds (1 or 2): "))
                    if quantity in [1,2]:
                        extrabed_capacity = quantity * 2
                        
                        print(f"extra beds provided. temporary capacity increased by {extrabed_capacity}.")
                        break #this breaks the while loop if the quantity is 1 or 2
                    else:
                        print("error:  only order 1 or 2 extra beds.")
                break #this breaks the while loop if the order of the extra bed is done that means charcter should be "y".
            elif ch == "n":
                break #this breaks the while loop if the user does not want to order any extra bed that means character should be "n".
            else:
                print("Error: Please enter 'y' or 'n'.")

        if Number > (capacity + extrabed_capacity): #it checks the no of guests with increased capacity and if the no of guests exceeds the capcicty,it will display the main menu
            print("Error: Even with extra beds, the number of guests exceeds the capacity.")
            print("Booking cannot proceed. Exiting to the main menu.")
            output()#calls the output function
            return

    print("Please enter the check-in date")
    Check_in_date = input()

    print("Please enter the check-out date")
    Check_out_date = input()
   #it checks wheter the length of the stay is in between 1 to 7 days
    while True:
        Length_of_stay = int(input("Please enter the length of stay (1-7 days): "))
        if  Length_of_stay in [1,2,3,4,5,6,7]:
            break
        else:
            print("error,length of stay must be between 1 and 7 days.")

    print("Please enter the booking date")
    Booking_date = input()
#calculates the total cost
    total_cost = rate * Length_of_stay
#if guests already exists and reward points is more than 100 ,ask user to process discount or not
    if Guest in Guests and Guests[Guest] >= 100:
        current_points = Guests[Guest]
        print(f"{Guest} has {current_points} reward points.")
        while True:
            print("Do you want to use your reward points to get a discount? (y/n)")
            character = input()
            if character == 'y':
                #calculate the discount 
                discount = (current_points // 100) * 10
                total_cost -= discount #gets reduce discount amount from total points
                remaining_points = current_points % 100
                Guests[Guest] = remaining_points #remaining reward points are added to guest dictionary
                print(f"${discount:.2f} deducted from the total cost using reward points.")
                print(f"Remaining reward points: {remaining_points}")
                break
            elif character == 'n':
                print("No reward points used.") #if guest's reward points are not used,there is no change in guest dictionary
                break
            else:
                print("Error: Enter 'y' or 'n'.") #invalid character so while loop runs again

#calculates the reward points by rounding off the total cost
    reward_points = round(total_cost)
    #it adds to reward point to guests dictionary
    if Guest in Guests:
        Guests[Guest] += reward_points
    else:
        Guests[Guest] = reward_points

    sub_total = 0 #the cost of all the supplementary items is assigned as 0
    flag = 0
    print("Supplementary items")
    
    while flag==0:
        #this main while loop runs until the  given wrong character other than y or n
        while True:
            print("Do you want to order a supplementary item? (y/n)")
            ch = input()
            if ch == "y" or ch == "n":
                if ch == "y":
                    #this while loop runs and gets the multiple supplementary items from a user
                    while True:
                        item_id = input("Enter the supplementary item ID: ")
                        if item_id in suppl:#it calculates cost (price*quantity) only when item is available in suppl dictionary
                            print(f"The price of the selected item ID is ${suppl[item_id]:.2f}")
                            #this while loop runs until the given quantity is positive 
                            while True:
                                quantity = int(input("Enter the desired quantity: "))
                                if quantity > 0:
                                    price = suppl[item_id]
                                    cost = price * quantity #it calculates the cost when the quantity is positive
                                    print(f"The cost for the supplementary item will be ${cost:.2f}")
                                    break #it breaks the while loop of quantity validiation.
                                else:
                                    print("Error: Quantity must be a positive .")
                            #this loop runs until the vaild characters is given(y or n) 
                            while True:
                                print("Confirmation (y/n):")
                                con = input()
                                if con in ["y", "n"]: #if the user confirm the order,it will save the supplementary items details in supplementary_items list.
                                    if con == "y":
                                        print("Supplementary order is confirmed")
                                        supplementary_items.append({'item_id': item_id, 'quantity': quantity, 'price': price})
                                        sub_total += cost #add the cost of each and every supplementary items
                                    else:
                                        print("Item cancelled")#if a user needs no confirmation ,item gets cancelled and wont be storing in the supplementary_items.
                                    break#it breaks the while loop if con is y/n
                                else:
                                    print("Error: Please enter 'y' or 'n'")
                            break#it breaks the while loop if supplementary items is found.
                        else:
                            print("Error: Supplementary item ID not found")
                    break#it breaks the main while loop
                elif ch == "n":
                    flag = 1 #this flag is for outermost while loop ,if the order of the supplementary item does not want continue ,then it displays the user and their supplementary items details. 
                    print("=" * 57)
                    print("Pythonia Serviced Apartments - Booking Receipt")
                    print("=" * 57)
                    print("Guest Name:", Guest)
                    print("Number of guests:", Number)
                    print("Apartment name:", Apartment_id)
                    print(f"Apartment rate: ${rate:.2f} AUD")
                    print("Check-in date:", Check_in_date)
                    print("Check-out date:", Check_out_date)
                    print(f"Length of stay: {Length_of_stay} nights")
                    print("Booking date:", Booking_date)
                    print("-" * 81)
                    print("Supplementary Items:")
                    #diplay the supplementary items details from the supplementary_items dictionary
                    for item in supplementary_items:
                        print(f"Item ID: {item['item_id']}")
                        print(f"Quantity: {item['quantity']}")
                        print(f"Price: ${item['price']:.2f}")
                        print(f"Cost: ${item['price'] * item['quantity']:.2f}")
                    print(f"Sub-total: ${sub_total:.2f} AUD")
                    print("-" * 81)
                    print(f"Total cost: ${total_cost + sub_total:.2f} AUD")
                    print(f"Earned points: {reward_points} points")
                    print("Thank you for your booking! We hope you will have an enjoyable stay")
                    print("=" * 57)
                    break#it breaks the main while loop
            else:
                print("Error: Please enter 'y' or 'n'.") 
#if the guest not existing in booking history dictionary,create a list as value and guest name as key
    if Guest not in history:
        history[Guest] = [] 
#inside the list ,creating a dictionary for each order with the keys("apartment_id,quantity,supplementary,total_cost,earned_rewards") with the respective values
    history[Guest].append({
        "apartment_id": Apartment_id,
        "quantity": Number,
        "supplementary": {item['item_id']: item['quantity'] for item in supplementary_items},# comphresion is used to fetch item id and quantity from the supplementary_items list and save the itemid as key and quantity as value in the supplementary value 
        "total_cost": total_cost + sub_total,
        "earned_rewards": reward_points})

    output() #calls the main function and displays the menu again.
#this function for adding or updating the new apartment details and checks the validation of apartment id format
def add_apart():
    apar_details = input("Enter the apartment details (ID rate capacity): ")
    
    apartment_id, rate, capacity = apar_details.split() #split function splits the input into aparatment_id ,rate and capacity
    rate = float(rate)
    capacity = int(capacity)
    if apartment_id[0] == "U" and apartment_id[1:3].isdigit() and apartment_id[3:].isalpha(): #checks the apartment id format
        Apartments[apartment_id] = [rate, capacity]#now adds or updates the rate and capacity as list (value) of apartment id (key) in apartment dictionary.
    else:
        print("Error: Incorrect format")
    
    output()#calls the main function and displays the menu again.

def add_supp():
    while True:
        supp_details = input("Enter the items and prices to update the supplementary items (e.g., toothpaste 5.2, shampoo 8.2): ")
        items_prices = [item for item in supp_details.split(',')] #used list comphresion to save items and prices as list type.
        flag = True
        for item_price in items_prices:
            l = item_price.split()#now split the items and price seperately.
            
            item = l[0]
            price = float(l[1])
            if price <= 0: #if the price is invalid ,the for loop breaks and display the main menu
                print("Error: Prices must be greater than 0.")
                flag = False
                break
            

            suppl[item] = price #if the price is vaild ,adds the  price as value for the key item

        if flag:
            break#it breaks the while loop 

    output()#calls the main function and displays the menu again.

#this function displays the guest details [guest dictionary(guest name(key) and reward points(value))]
def display_guests():
    for i in Guests:
        print(f"Guest name: {i}, Reward points: {Guests[i]}")
    output()#calls the main function and displays the menu again.

#this function displays the details of apartments and fetchs from [apartments dictionary (apartment id(key) and [rate and capacity](value))]
def display_apart():
    for i in Apartments:
        print(f"Apartment unit ID: {i}, Nightly rate: ${Apartments[i][0]:.2f}, Capacity: {Apartments[i][1]}")
    output()#calls the main function and displays the menu again.

#this function displays the details of supplementary items and fetchs from [suppl list]
def display_supp():
    for i in suppl:
        print(f"Supplementary item: {i}, Price: ${suppl[i]:.2f}")
    output()#calls the main function and displays the menu again.

#this function displays the order history of the guest and the order history details are fetched from the history dictionary
def display_booking_history():
    #this while loop until the guest is found 
    while True:
        guest_name = input("Enter the guest name: ")
        if guest_name not in history:#the guest name is not available because no order is done yet by that user
            print("Error: Guest name not found.")
        else:
            break

    print(f"This is the booking and order history for {guest_name}.")
    print("                List                      Total Cost  Earned Rewards")

    order_no = 1 #order_no start from 1
    
    for order in history[guest_name]:
        items = []
        if order["apartment_id"]:
            items.append(f"{order['quantity']} x {order['apartment_id']}")
        for item, quantity in order["supplementary"].items():
            items.append(f"{quantity} x {item}")

        items_str = ", ".join(items)
        print(f"Order {order_no} {items_str} ${order['total_cost']} {order['earned_rewards']}")
        order_no += 1

    output()#calls the main function and displays the menu again.

output()#call the main function for the first time and displays the menu.

