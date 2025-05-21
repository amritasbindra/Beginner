guests = ['korra', 'kyoshi', 'ruko', 'wan']

print(f"You have been invited to the water tribe dinner Avatar {guests[0].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[1].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[2].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[3].title()}!")

print(f"Avatar {guests[2].title()} can't make it to the dinner")

del guests[2]
guests.insert (2,'yangchen')

print(f"You have been invited to the water tribe dinner Avatar {guests[0].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[1].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[2].title()}!")
print(f"You have been invited to the water tribe dinner Avatar {guests[3].title()}!")

print("I have invited more people so we need a bigger venue!")

guests.insert (0, 'katara')
guests.insert (1, 'sokka')
guests.append ('aang')

print(guests)

print(f"You have been invited to the Earth Kingdom dinner {guests[0].title()}!")
print(f"You have been invited to the Earth Kingdom dinner {guests[1].title()}!")
print(f"You have been invited to the Earth Kingdom dinner Avatar {guests[2].title()}!")
print(f"You have been invited to the Earth Kingdom dinner Avatar {guests[3].title()}!")
print(f"You have been invited to the Earth Kingdom dinner Avatar {guests[4].title()}!")
print(f"You have been invited to the Earth Kingdom dinner Avatar {guests[5].title()}!")
print(f"You have been invited to the Earth Kingdom dinner Avatar {guests[6].title()}!")

print("Sorry guys, I can only invite 2 people. I couldn't afford dinner at the Earth Kingdom")

print(guests)

print(f"You've been uninvited {guests.pop(0).title()} lol")
print(f"You've been uninvited {guests.pop(1).title()} lol")
print(f"You've been uninvited {guests.pop(2).title()} lol")
print(f"You've been uninvited {guests.pop(3).title()} lol")
print(f"You've been uninvited {guests.pop().title()} lol")

print(guests)

del guests [0]

print(guests)

del guests [0]

print(guests)
