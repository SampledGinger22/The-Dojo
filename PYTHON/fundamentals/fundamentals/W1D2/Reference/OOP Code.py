#Encapulation
# class CoffeeM:
#     def __init__(self,name):
#         self.name = name
#         self.water_temp = 200
#     def brew_now(self,beans):
#         print(f"Using {beans}!")
#         print("Brew now brown cow!")
#         def clean(self):
#         print("Cleaning!")

#inheritance
# class CappuccinoM( CoffeeM ):
#     def __init__(self,name):
#         super().__init__(name)
#         self.milk = "whole"
#     def make_cappuccino(self,beans):
#         super.brew_now(beans)
#         print("Frothy!!!")

#Polymorphism
# class CappuccinoM( CoffeeM ):
#     def __init__(self,name):
#         super().__init__(name)
#         self.milk = "whole"
#     def make_cappuccino(self,beans):
#         super.brew_now(beans)
#         print("Frothy!!!")
#     def clean(self):
#         print("Cleaning the froth!

#abstraction
# class Barista:
#     def __init__(self,name):
#         self.name = name
#         self.cafe = CoffeeM("Cafe")
#     def make_coffee(self, beans):
#         self.cafe.brew_now(beans)


# class Parent:
#     def method_a(self):
#         print("invoking PARENT method_a!")
# class Child(Parent):
#     def method_a(self):
#         print("invoking CHILD method_a!")
# dad = Parent()
# son = Child()
# dad.method_a()
# son.method_a() #notice this overrides the Parent method!

# print(dad.method_a)
# print(son.method_a)







