#HW_P3: Python Programming Challenges for Customer Service Data Handling

# Task 1: Customer Service Ticket Tracker
'''
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Develop a program that:

- Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
- Implement functions to:
    - Open a new service ticket.
    - Update the status of an existing ticket.
    - Display all tickets or filter by status.
- Initialize with some sample tickets and include functionality for additional ticket entry.
'''

service_tickets = {
    "Ticket001": {
        "Customer": "Alice", 
        "Issue": "Login problem", 
        "Status": "open"},
    "Ticket002": {
        "Customer": "Bob", 
        "Issue": "Payment issue", 
        "Status": "closed"},
    "Ticket003": {
        "Customer": "Chris", 
        "Issue": "Payment issue", 
        "Status": "open"}
}

def new_ticket(ticket, customer, issue):
    if ticket not in service_tickets:
        service_tickets[ticket] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"{ticket} has been opened.")
    else:
        print("Seems this is an invalid ticket, please enter a valid ticket input.")

def update_status(ticket, status):
    if ticket in service_tickets:
        service_tickets[ticket]["Status"] = status
        print(f"{ticket} has a status update of {status}")
    else:
        print("Can not find ticket, please enter a valid ticket input.")
    
def display_tickets(service_tickets):
    for ticket, details in service_tickets.items():
        # for info, status in details.items():
        print(f"{ticket}: Status is {details["Status"]}, Customer is {details["Customer"]} with the issue of \"{details["Issue"]}\"")

new_ticket("Ticket004", "Daniella", "Forgot Password")
print(service_tickets)

update_status("Ticket001", "closed")
print(service_tickets)

display_tickets(service_tickets)
