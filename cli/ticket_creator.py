
import json

print("===Welcome To Campusflow Ticket Creator!===")


# 1. Load existing tickets
def load_tickets():
    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)

    except FileNotFoundError:
        tickets = []
        print("No tickets found.")

    except json.JSONDecodeError:
        print("Invalid tickets file.")
        raise SystemExit

    return tickets


# 2. Save tickets
def save_tickets(tickets):
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)


# 3. Validate ticket information
def validate_input(title, description):
    if not title.strip():
        return False

    elif not description.strip():
        return False

    else:
        return True


# 4. Collect ticket details
def get_ticket_details():
    title = input("Enter ticket title: ")
    description = input("Enter ticket description: ")

    return title, description


# 5. Generate ticket ID
def generate_ticket_id(tickets):
    if not tickets:
        return 1

    highest_id = max(ticket["id"] for ticket in tickets)

    return highest_id + 1


# 6. Create a ticket
def create_ticket(tickets):
    title, description = get_ticket_details()

    if not validate_input(title, description):
        print("Error: Title and description cannot be empty.")
        return False

    ticket = {
        "id": generate_ticket_id(tickets),
        "title": title.strip(),
        "description": description.strip()
    }

    tickets.append(ticket)

    save_tickets(tickets)

    print("Ticket created successfully!")
    print(ticket)

    return True


# 7. Main application
def main():
    tickets = load_tickets()

    # Create tickets.json if it doesn't exist
    save_tickets(tickets)

    while True:
        create_ticket(tickets)

        choice = input(
            "Would you like to create another ticket? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            print("Thank you for using CampusFlow!")
            break


# Start the application
main()
