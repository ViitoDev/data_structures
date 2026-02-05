guest_list = []

while True:
    guest = input("Enter the new guest: ")
    if guest.lower() == "leave":
        break
    guest_list.append(guest)

print(guest_list)