
height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
bounces = int(input("Enter the number of times the ball is allowed to bounce: "))

bouncy = 0.6
distance = height


for i in range(bounces):
    height *= bouncy
    distance += 2 * height

print("The total distance traveled by the ball after " + str(bounces) + " bounces is " + str(distance) + " feet.")
