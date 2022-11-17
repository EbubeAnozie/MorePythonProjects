# define the class Bike
class Bike:

    def _init_(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")


# creating a coupple of instance
red_bike = Bike('Red', 'Carbon fibre')
blue_bike = Bike('Blue', 'Steel')

print(red_bike.color)
print(red_bike.frame_material)
print(blue_bike.color)
print(blue_bike.frame_material)

red_bike.brake()
