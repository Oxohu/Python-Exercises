names = ['Faridah', 'Mujibah', 'Muhsinah', 'Hakeem']
print(names[0].lower())
print(names[1])

welcome_message = f" hi {names[2]}, it's nice to meet you"
print(welcome_message)

cars = ["honda", "Toyota", "Ferarri", "BMW"]
print(f" I would love to own a {cars[3].lower()}")
guest_list = ['aisha', 'Ruqayyah', 'Khadijah', 'Abdullah']
print(guest_list)
guest_list.pop()
guest_list.append('fatimah')
guest_list.insert(1, 'Mariam')
guest_list.pop(0)
print(guest_list)

if names in guest_list > 2:
    print("you can only invite two people to the party")
    guest_list.pop()
else:
    print(f"{guest_list[0]}, you are invited to the party")
