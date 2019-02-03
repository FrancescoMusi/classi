import random 
import os, sys
import time

class Gold():
	def __init__(self):
		self.x = random.randint(0, field.x-1)
		self.y = random.randint(0, field.y-1)

	def checkGoldOnPlayer(self):
		while player.cur_x == self.x and player.cur_y == self.y:
			player.cur_x = random.randint(0, field.x-1)
			player.cur_y = random.randint(0, field.y-1)	
			return True



class Player():
	def __init__(self, hp):
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)

		self.cur_hp = hp
		self.max_hp = hp

	def printStatus(self):
		print("player hp: {}%".format(player.cur_hp))

	
	def move(self, direction):
		if direction == 'w' and player.cur_x >= 1:
			self.cur_x -= 1
		elif direction == 'a' and player.cur_y >= 1:
			self.cur_y -= 1
		elif direction == 's' and player.cur_x < field.x-1:
			self.cur_x += 1
		elif direction == 'd' and player.cur_y < field.y-1:
			self.cur_y += 1



class Enemy():
	def __init__(self, damage):
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)
		self.damage = damage

	def checkEnemyOnPlayer(self):
		while player.cur_x == self.cur_x and player.cur_y == self.cur_y:
			player.cur_x = random.randint(0, field.x-1)
			player.cur_y = random.randint(0, field.y-1)	
			return True


	def move(self):
		if self.cur_x > player.cur_x and self.cur_x > 0 and	self.cur_x-1 != ['G']:
			self.cur_x -= 1
		elif self.cur_y > player.cur_y and self.cur_y > 0 and	self.cur_y-1 != ['G']:
			self.cur_y -= 1
		elif self.cur_x < player.cur_x and self.cur_x < field.x-1 and	self.cur_x+1 != ['G']:
			self.cur_x += 1
		elif self.cur_y < player.cur_y and self.cur_y < field.y-1 and	self.cur_y+1 != ['G']:
			self.cur_y += 1
	

	def attack(self, target):
		target.cur_hp -= self.damage
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

	def printField(self):
		while True:
			self.graphic_field[player.cur_x][player.cur_y] = ['P']
			self.graphic_field[monster1.cur_x][monster1.cur_y] = ['M']
			self.graphic_field[monster2.cur_x][monster2.cur_y] = ['M']
			self.graphic_field[boss.cur_x][boss.cur_y] = ['B']
			self.graphic_field[gold.x][gold.y] = ['G']

			self.counter = 0 
			for i in self.graphic_field:
				if i != [' ']:
					self.counter += 1

			if self.counter >= 4:
				for y in self.graphic_field:
					for x in y:
						print(x, end = '')
					print()
				break




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
monster1 = Enemy(50)
monster2 = Enemy(50)
boss = Enemy(100)

player = Player(100)
gold = Gold()

os.system('cls')

while True:
	while True:
		field.createField()
		field.printField()
		player.printStatus()
		monster1.move()
		monster2.move()
		boss.move()


		#prende in input la direzione
		print()
		direction = input("Direction (wasd) - Q per uscire: ").lower()
		player.move(direction)

		if monster1.checkEnemyOnPlayer() or monster2.checkEnemyOnPlayer():
			monster1.attack(player)

		if boss.checkEnemyOnPlayer():
			boss.attack(player)

		if player.cur_hp <= 0:
			printLose()
			break

		if gold.checkGoldOnPlayer():
			printWin()
			break

		if direction == 'q':
			sys.exit()

		os.system('cls')