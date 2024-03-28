# HW_P2: Advanced Data Handling with Python

# Task 1: Hotel Room Booking Tracker
'''
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Develop a program that:
Manages room bookings, where each room has details such as booking status (booked/available) and customer name.

Implement functions to:
Book a room (mark as booked and assign to a customer).
Check-out a customer (mark room as available and remove customer name).
Display the status of all rooms.
'''

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "booked", "customer": "Rosa Hernandez"},
    "104": {"status": "available", "customer": ""}
}

def booking_room():
    room = input("Enter what room number you would like to book: ")
    if room in hotel_rooms:
        if hotel_rooms[room]["status"] == "available":
            name = input("Enter the customers name: ")
            hotel_rooms[room].update({"status": "booked"})
            hotel_rooms[room].update({"customer": name})
            print(f"You have sucessfully booked room {room} for {name}")
        else:
            print(f"Sorry, room {room} is already booked by {hotel_rooms[room]["customer"]}.")
    else:
        print(f"Sorry room {room} is not found in our records. Please try a valid room number")

def checking_out():
    room = input("Enter what room number you would like to check-out from: ")
    if room in hotel_rooms:
        if hotel_rooms[room]["status"] == "booked":
            name = hotel_rooms[room]["customer"]
            hotel_rooms[room].update({"status": "available"})
            hotel_rooms[room].update({"customer": ""})
            print(f"You have sucessfully checked-out for room {room} for {name}")
        else:
            print(f"Sorry, room {room} is already available.")
    else:
        print(f"Sorry room {room} is not found in our records. Please try a valid room number")

def display_status():
    for room, information in hotel_rooms.items():
        print(f"Status of room {room} is: {information["status"]}")

booking_room()
print(hotel_rooms)
checking_out()
print(hotel_rooms)
display_status()


# Task 2: E-commerce Product Search Feature
'''
Put your data handling and string manipulation skills to the test by creating a product search feature 
for an e-commerce platform.

Create a system that:
Holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
Handle cases where no matches are found.
'''

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20},
    "3": {"name": "Shirt", "category": "Clothing", "price": 50}
}

def product_by_name(search_name):
    product_results = []
    for product, details in products.items():
        if details["name"].lower() == search_name.lower():
            product_results.append((product, details))
    return product_results

search_name = input("What product would you like to search for? ")
results = product_by_name(search_name)
if results:
    print("The found matching product(s) are:")
    for product, details in results:
        print(f"Product {product}, Name: {details["name"]}, Category: {details["category"]}, Price: {details["price"]}")
else:
    print("Sorry, looks like there was no match.")
