# 1/2
# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5


# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)


# 2/2
# Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class
