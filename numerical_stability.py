
initial = 1000000000.00

adding = initial

for i in range(1,1000000):
    adding = adding + .000001

final = adding - initial
print(final)
