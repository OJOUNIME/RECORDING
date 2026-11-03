import json
import os

def load_tickets():
    if not os.path.exists("tickets.json"):
        return []

    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)
            return tickets
    except:
        print("Error reading file, starting with a clean list.")
        return []
    

def save_tickets(tickets_list):
    try:
        with open("tickets.json", "w") as file:
            json.dump(tickets_list, file, indent=4)
    except: 
        print("Error: could not save your ticket.")

def generate_unique_id(existing_tickets):
    if len(existing_tickets) == 0:
        return 1
