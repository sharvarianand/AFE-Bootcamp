# First 10 km = rs 11/km next 90 km = rs 10/km after rs 9/km

distance = int(input("Enter the distance in km :"))
cost = 0
if (distance <= 10):
    cost = 10*11
elif(distance >10 and distance<=100):
    cost+= 10*(distance-10)
elif(distance>100):
    cost+= (distance-100)*9

print(f"The total cost = {cost}")            



