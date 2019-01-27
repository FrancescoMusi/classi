import random 
import os, sys
import time

class Gold():
	def __init__(self):
		self.x = random.randint(0, field.x-1)
		self.y = random.randint(0, field.y-1)


class Player():
	def __init__(self, hp):
		self.x = random.randint(0, field.x-1)
		self.y = random.randint(0, field.y-1)

		self.cur_x = self.x
		self.cur_y = self.y
		self.cur_hp = hp
		self.max_hp = hp

	def printStatus(self):
		print("player hp: {}%".format(player.cur_hp))

	
	def move(self, direction):
		if direction == 'w' and player.cur_x >= 1:
			self.cur_x -= 1
		elif direction == 'a' and player.cur_y >= 1:
			self.cur_y -= 1
		elif direction == 's' and player.cur_x <= field.x-1:
			self.cur_x += 1
		elif direction == 'd' and player.cur_y <= field.y-1:
			self.cur_y += 1



class Enemy():
	def __init__(self, damage):
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)
		self.damage = damage

		
	def move(self):
		directions = 'wasd'
		direction = random.choice(directions)

		if direction == 'w' and monster.cur_x > 0:
			self.cur_x -= 1
		elif direction == 'a' and monster.cur_y > 0:
			self.cur_y -= 1
		elif direction == 's' and monster.cur_x < field.x-1:
			self.cur_x += 1
		elif direction == 'd' and monster.cur_y < field.y-1:
			self.cur_y += 1
	

	def attack(self, target):
		target.cur_hp -= monster.damage
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)

class Field():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def createField(self):
		self.graphic_field = []
		for i in range(self.x):
			self.graphic_field.append([])
			for x in range(self.y):
				self.graphic_field[i].append([' '])

	def printField(self, player):
		while True:
			if player.cur_x == monster.cur_x and player.cur_y == monster.cur_y or player.cur_x == gold.x and player.cur_y == gold.y:
				player.cur_x = random.randint(0, field.x-1)
				player.cur_y = random.randint(0, field.y-1)		
			else:
				break
	
		self.graphic_field[player.cur_x][player.cur_y] = ['P']
		self.graphic_field[monster.cur_x][monster.cur_y] = ['M']
		self.graphic_field[gold.x][gold.y] = ['G']

		for i in self.graphic_field:
			for x in i:
				print(x, end = '')
			print()

def printWin():
	os.system('cls')
	for i in range(3):
		print('===========')
		print('YOU WIN  :)')
		print('===========')
		print('reastart in {}...'.format(3-(i)))
		time.sleep(1)
		os.system('cls')

def printLose():
	os.system('cls')
	for i in range(3):
		print('===========')
		print('YOU LOSE  :)')
		print('===========')
		print('reastart in {}...'.format(3-(i+1)))
		time.sleep(1)
		os.system('cls')

#ISTANZE
field = Field(10, 10)
monster = Enemy(50)
player = Player(100)
gold = Gold()

os.system('cls')

while True:
	while True:
		field.createField()
		field.printField(player)
		player.printStatus()
		monster.move()

		#prende in input la direzione
		print()
		direction = input("Direction (wasd) - Q per uscire: ").lower()
		player.move(direction)

		if player.cur_x == monster.cur_x and player.cur_y == monster.cur_y:
			monster.attack(player)

		if player.cur_hp <= 0:
			printLose()
			break

		if player.cur_x == gold.x and player.cur_y == gold.y:
			printWin()
			break

		if direction == 'q':
			sys.exit()

		os.system('cls')