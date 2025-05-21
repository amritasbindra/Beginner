dc_superheros = ['robin', 'cyborg', 'beast boy', 'starfire', 'raven', 'tony stark', 'black widow', 'captain america'] 

print(dc_superheros)

del dc_superheros [5]

print(dc_superheros)

dc_superheros.append ('wonder woman')
print(dc_superheros)

dc_superheros.insert (1, 'batman')
print(dc_superheros)

dc_superheros.remove('black widow')
print(dc_superheros)

marvel_superheros = dc_superheros.pop(6)
print(dc_superheros)
print(marvel_superheros)

print(sorted(dc_superheros))
print(dc_superheros)

print(sorted(dc_superheros, reverse = True))
print(dc_superheros)

dc_superheros.reverse()
print(dc_superheros)

dc_superheros.sort(reverse=True)
print(dc_superheros)

dc_superheros.sort()
print(dc_superheros)
