class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("yummy!!" + self.name + "is eating" + food)
	def description (self):
		print(self.name + "is" + self.age + "and loves the color" + self.favorite_color)


max = Animal("3aw_3aw", "shawarbo", 15,"black")
max.eat()