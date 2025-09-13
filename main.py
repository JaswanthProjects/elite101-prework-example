def greet_user():
    print("Welcome to the food Chatbot")
    name = input("What is your name? ")
    age = int(input(f"Hello {name}, How old are you? " ))

    if age < 15:
        print(f"Welcome {name}, Ur {age} years old?. Oh you super duper young! Anyway, how may I help you today?")
    elif 15 <= age < 18:
        print(f"Welcome {name}, Ur {age} years old?. Oh you entering in the big leagues now! Anyway, how may I help you today?")
    elif 18 <= age < 55:
        print(f"Welcome {name}, Ur {age} years old?. There you are all nice and grown up! Anyway, how may I help you today?")
    elif 55 <= age < 100:
        print(f"Welcome {name}, Ur {age} years old?. Well dang, Keep that health in shape! Anyway, how may I help you today?")
    elif age > 100:
        print(f"Welcome {name}, Ur {age} years old?. Wow, ur defo dead or ur superhuman! Anyway, how may I help you today?")
    else:
        print("invalid age")


def main_menu():
    print("""
    Please choose from the following options: 
    1. Order food for delivery
    2. Order food for pickup
    3. Make a reservation
    4. Exit the conversation
    """)

    choice = int(input("Please choose an option: "))

    if choice == 1:
        resturant_name = input("Enter the resturant you want to order from: ")
        #  code help =  https://www.w3schools.com/python/ref_string_split.asp
        food_items = input("Enter food items separated by commas: ").split(",")
        delivery_address = input("Enter the address you want it delievered to: ")

        cost = len(food_items) * 2 
        print(f"Cost of the items is ${cost}")
        tip = int(input("How much tip do you want to add?"))
        total_cost = tip + cost
        print(f"Total cost is {total_cost}")

        confirm_order = input(
            f"Confirm Please. The resturant is {resturant_name}. The food items are {food_items}. "
            f"The delivery address is {delivery_address}, total-cost is {total_cost}. Say yes or no: "
        ).lower()

        if confirm_order == "yes":
            order_time = len(food_items) * 10
            print(f"Your order time is {order_time} minutes until delivery")
        else:
            print("Let's try again!")
            main_menu()  

    elif choice == 2:
        resturant_name = input("Enter the resturant you want to order from: ")
        #  code help =  https://www.w3schools.com/python/ref_string_split.asp
        food_items = input("Enter food items separated by commas: ").split(",")

        cost = len(food_items) * 2 
        print(f"Cost of the items is ${cost}")

        confirm_order = input(
            f"Confirm Please. The resturant is {resturant_name}. The food items are {food_items}. "
            f"The cost is {cost}. Say yes or no: "
        ).lower()

        if confirm_order == "yes":
            order_time = len(food_items) * 10
            print(f"Your order time is {order_time} minutes until pick up")
        else:
            print("Let's try again!")
            main_menu()  


    elif choice == 3:
        resturant_name = input("Enter the resturant you want to reserve: ")
        reservation_name = input("Enter the name you want to reserve under: ")
        reservation_time = input("Enter the time you want to reserve: ")
        members = int(input("How many people do you want to reserve for? "))

        confirm_order = input(
            f"Confirm Please. The resturant is {resturant_name}. The reservation name is {reservation_name}. "
            f"The reservation time is { reservation_time}, members are {members}. Say yes or no: "
        ).lower()
        
        if confirm_order == "yes":
            print("Reservation confirmed")
        else:
            print("Let's try again!")
            main_menu()  

    elif choice == 4:
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Try again.")
        main_menu()  


greet_user()

# Then show menu
main_menu()
