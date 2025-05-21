motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

#motorcycles [0] = 'ducati'
#print(motorcycles)

#using the append statement 

motorcycles.append ('ducati')
print(motorcycles)

cars = []

cars.append('rezvani')
cars.append('ferrari')
cars.append('lamborghini')

print(cars)

#using the insert statement

#motorcycles.insert(0,'ducati')
#print(motorcycles)

#using the del statement 

#del motorcycles[0]
#print(motorcycles)

#using the pop() statement 

#popped_motorcycles = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycles)

#last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}")

#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}")

#using the remove statement

#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
