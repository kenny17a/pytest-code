# def custom_range(num):
#     pass
#
#
# def infinite_number_generator():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# gen = infinite_number_generator()
# print(next(gen))
#

class Automobile:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def speed(self):
        return "speeding on 120km/hr"


benz = Automobile("E-class", 2007)
audi = Automobile("audi civic", 2020)
print(benz.speed())
print(Automobile.speed(benz))

