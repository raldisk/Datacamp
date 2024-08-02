class Player:
    MAX_POSITION = 10

    # Define a constructor
    def __init__(self, position):
        # Check if position is less than the class-level attribute value
        if position <= Player.MAX_POSITION:
            self.position = position

        # If not, set equal to the class-level attribute
        else:
            self.position = Player.MAX_POSITION


# Create a Player object, p, and print its MAX_POSITITON
p = Player(6)
print(p.MAX_POSITION)
