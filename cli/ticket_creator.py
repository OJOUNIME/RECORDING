import json
print("===Welcome To Campusflow Ticket Creator!===")

def load_tickets():
    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)

    except FileNotFoundError:
        tickets = []
        print("No tickets found")

    except json.JSONDecodeError:
        print("invalid tickets")
        raise SystemExit

    return tickets

tickets = load_tickets()
print(tickets)

def save_tickets(tickets):
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

save_tickets(tickets)
print("Tickets saved!")

def validation_input(title, description):
    pass