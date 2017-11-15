def ex1():
	class Animal(object):
		def __init__(self,sound,name,age,favorite_color):
			self.sound = sound
			self.name = name
			self.age = age
			self.favorite_color = favorite_color
		def eat(self,food):
			print("yummy!!" + self.name + "is eating " + food)
		def description (self):
			print(self.name + "is " + self.age + " and loves the color " + self.favorite_color)

		def make_sound(self,sound,x):
			
			print("wof ")*x

	Max = Animal("3aw_3aw", "shawarbo ", "15" ,"black")
	Max.eat("banana")
	Max.description()
	Max.make_sound("wof",8)



def ex3():
	class Person(object):
		def __init__(self,name,age,city,gender,food,sport):
			self.name = name
			self.age = age
			self.city = city
			self.gender = gender
			self.food = food
			self.sport = sport
		def eat(self):
			print(self.name + "likes " + "to eat "+self.food)
		def play(self):
			print(self.name + "likes to play " + self.sport)

	wadi = Person("wadi ","15","beitawa","boi","banana","football")
	wadi.eat()
	wadi.play()



class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		print(self.lyrics)
		for sing_me_a_song in range(1):
			print("Roses are red,")
			print("violets are blue,")
			print("i wrote this poem for you.")
			for i in lyrics:
				print(i)
flower_song = Song(["Roses are red,",
		"violets are blue,",
		"i wrote this poem for you."])
	
flower_song.sing_me_a_song()
