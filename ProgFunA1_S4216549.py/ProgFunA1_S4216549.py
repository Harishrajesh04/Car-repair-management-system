#Name: Harish Rajesh
#STudent ID: S4216549
#Assignment 1 of Programming fundamnetlas 
#Date of start is 20-03-2026
#The things I understand from the pdf is: I need to create the car repair shop management for customers and the basic data is Tim and Rose
#In this assignment, you are developing a management system for a car repairshop. The receptionists or mechanics at the shop are the ones that use this system to process service jobs and print out the receipts for the customers. You are required to implement the program following the below requirements

#creating datas for the management system

customer_data = {"Tim": True, "Rose": False} #this is the data that is given in the pdf

#this service data is also given in the pdf
services_data = {"inspection":{"hours":1.0, "input_hours": False, "parts_needed": False},
                 "diagnostic":{"hours":1.0, "input_hours": False, "parts_needed": False},
                 "maintenance":{"hours":2.0, "input_hours": False, "parts_needed": True},
                 "repair":{"hours":None, "input_hours": True, "parts_needed": True}}

#parts data is there in the page no 4 in the pdf

parts = {"oil": 35.0,"filter": 25.0, "brake":120.0, "battery": 180.0, "radiator": 420.0, "motor": 280.0}

#getting input from the cuustomer
def perform_service():
    while True:
        customer_name = input("Enter the customer name: ").strip()
        if customer_name.isalpha():
            break
        print("Invalid name, try again")

    while True:
        service_required = input("Enter the service required: ").strip().lower()
        if service_required in services_data:
            break
        print("Invalid service, try again")
    if customer_name not in customer_data:
        customer_data[customer_name] = False 


    #service hours 

    if service_required == "repair":
        while True:
            value = input("Enter the number of hours: ")
            try:
                hours = float(value)
                if hours >= 1 and (hours * 2).is_integer():
                    break
                else:
                    print("Invalid hours")
            except:
                print("Invalid input")
    else:
        hours = services_data[service_required]["hours"]

    
    if services_data[service_required]["parts_needed"]:
        while True:
            part_name = input("Enter part name: ").strip().lower()
            if part_name in parts:
                part_cost = parts[part_name]
                break
            print("Invalid part, try again")
    else:
        part_name = None
        part_cost = 0


    #now we need to add the cost calculation where this requires to use our brain

    rate = 40.0

    service_cost = hours * rate
    original_cost = service_cost + part_cost

    if customer_data[customer_name]:
        discount = original_cost * 0.10 #this is for the old customer
    else:
        discount = 0 #this is for the new customer because theyy are new

    total_cost = original_cost - discount

    #now we need to print thr receipt format

    print("-" * 50)
    print("Receipt")
    print("-" * 50)
    print(f"{service_required}: {hours} x 40")

    if part_name:
        print(f"{part_name}: {part_cost}")

    print("-" * 50)
    print(f"Original cost: {original_cost}")
    print(f"Discount: {discount}")
    print(f"Total cost: {total_cost}")
    print("-" * 50)

    if not customer_data[customer_name]:
        member_choice = input("Become member? (y/n): ").strip().lower()
        if member_choice == "y":
            customer_data[customer_name] = True
            print("Now you are a member.")

def display_customers():
    for name, member in customer_data.items():
        print(name, "->", member)


def display_services():
    for service_name, details in services_data.items():
        print(service_name, "->", details)

def display_parts():
    for part_name, price in parts.items():
        print(part_name, "->", price)

def update_services():
    service_name = input("Enter service name to update: ").strip().lower()

    if service_name in services_data:
        new_value = input("Enter new hours or na: ").strip().lower()

        if new_value == "na":
            services_data[service_name]["hours"] = None
            services_data[service_name]["input_hours"] = True
        else:
            services_data[service_name]["hours"] = float(new_value)
            services_data[service_name]["input_hours"] = False

        print("Service updated")
    else:
        print("Service not found")

def update_parts():
    action = input("Add or remove part? (a/r): ").strip().lower()

    if action == "a":
        part_name = input("Enter new part name: ").strip().lower()
        price = float(input("Enter price: "))
        parts[part_name] = price
        print("Part added")
    elif action == "r":
        part_name = input("Enter part name to remove: ").strip().lower()
        if part_name in parts:
            del parts[part_name]
            print("Part removed")
        else:
            print("Part not found")
    else:
        print("Invalid choice")

while True:
    print("\n1. Perform service")
    print("2. Display customers")
    print("3. Display services")
    print("4. Display parts")
    print("5. Update services")
    print("6. Update parts")
    print("0. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        perform_service()
    elif choice == "2":
        display_customers()
    elif choice == "3":
        display_services()
    elif choice == "4":
        display_parts()
    elif choice == "5":
        update_services()
    elif choice == "6":
        update_parts()
    elif choice == "0":
        print("Thank you")
        break
    else:
        print("Invalid choice")