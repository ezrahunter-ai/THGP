room = ["Shirt",
    "Pants",
    "Shoes",
    "Toothbrush",
    "Phone Charger",
    "Laptop",
    "Headphones",
    "Book",
    "Water Bottle",
    "Hat"]
travel_bag = []

print("Items in the room:")
for i in range(len(room)):
    print(f"- {room[i]}")

def add_room(room_number):
    if room_number not in room:
        room.append(room_number)
        print(f"Room {room_number} added.")
    else:
        print(f"Room {room_number} already exists.")


def remove_room(room_number):
    if room_number in room:
        room.remove(room_number)
        print(f"Room {room_number} removed.")
    else:
        print(f"Room {room_number} does not exist.")