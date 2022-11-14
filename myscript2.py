from rocket2 import Rocket, RocketBoard

# board = RocketBoard(3)
# board = RocketBoard(4)

rocket1 = Rocket(altitude=4)
rocket2 = Rocket()
print(RocketBoard.get_distance(rocket1, rocket2))
