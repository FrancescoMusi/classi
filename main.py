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
		while True:
			self.cur_x = random.randint(0, field.x-1)
			self.cur_y = random.randint(0, field.y-1)

			if self.cur_x != gold.x and self.cur_y != gold.y:
				break

		self.max_hp = hp
		self.cur_hp = hp

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
		while True:
			self.cur_x = random.randint(0, field.x-1)
			self.cur_y = random.randint(0, field.y-1)

			if self.cur_x != gold.x and self.cur_y != gold.y and self.cur_x != player.cur_x and self.cur_y != player.cur_y:
				break

		self.damage = damage

	def checkEnemyOnPlayer(self):
		while player.cur_x == self.cur_x and player.cur_y == self.cur_y:
			player.cur_x = random.randint(0, field.x-1)
			player.cur_y = random.randint(0, field.y-1)	
			return True


	def move(self):
		if self.cur_x > player.cur_x and self.cur_x > 0 and	self.cur_x-1 != ['G'] and	self.cur_x-1 != ['M'] and	self.cur_x-1 != ['B']:
			self.cur_x -= 1
		elif self.cur_y > player.cur_y and self.cur_y > 0 and	self.cur_y-1 != ['G'] and	self.cur_y-1 != ['M'] and	self.cur_y-1 != ['B']:
			self.cur_y -= 1
		elif self.cur_x < player.cur_x and self.cur_x < field.x-1 and	self.cur_x+1 != ['G'] and	self.cur_x+1 != ['M'] and	self.cur_x+1 != ['B']:
			self.cur_x += 1
		elif self.cur_y < player.cur_y and self.cur_y < field.y-1 and	self.cur_y+1 != ['G'] and	self.cur_y+1 != ['M'] and	self.cur_y+1 != ['B']:
			self.cur_y += 1
	 

	def attack(self, target):
		target.cur_hp -= self.damage
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)


class Boss(Enemy):
	def __init__(self, damage):
		self.cur_x = random.randint(0, field.x-1)
		self.cur_y = random.randint(0, field.y-1)
		self.damage = damage

		Enemy.__init__(self, damage)

	def move(self):
		# x>  y>
		if self.cur_x > player.cur_x and self.cur_y > player.cur_y and	self.cur_x-1 != ['G'] and	self.cur_x-1 != ['M'] and	self.cur_x-1 != ['B']:
			self.cur_x -= 1
			self.cur_y -= 1

		# x<  y>
		elif self.cur_y > player.cur_y  and self.cur_x < player.cur_x  and	self.cur_y-1 != ['G'] and	self.cur_y-1 != ['M'] and	self.cur_y-1 != ['B']:
			self.cur_y -= 1
			self.cur_x += 1

		# x>  y<
		elif self.cur_x > player.cur_x and self.cur_y < player.cur_y and	self.cur_x+1 != ['G'] and	self.cur_x+1 != ['M'] and	self.cur_x+1 != ['B']:
			self.cur_x -= 1
			self.cur_y += 1

		# x<  y<
		elif self.cur_y < player.cur_y  and self.cur_x < player.cur_x and  self.cur_y+1 != ['G'] and	self.cur_y+1 != ['M'] and	self.cur_y+1 != ['B']:
			self.cur_y += 1
			self.cur_x += 1

		#normal move
		elif self.cur_x > player.cur_x and self.cur_x > 0 and	self.cur_x-1 != ['G'] and	self.cur_x-1 != ['M'] and	self.cur_x-1 != ['B']:
			self.cur_x -= 1

		elif self.cur_y > player.cur_y and self.cur_y > 0 and	self.cur_y-1 != ['G'] and	self.cur_y-1 != ['M'] and	self.cur_y-1 != ['B']:
			self.cur_y -= 1

		elif self.cur_x < player.cur_x and self.cur_x < field.x-1 and	self.cur_x+1 != ['G'] and	self.cur_x+1 != ['M'] and	self.cur_x+1 != ['B']:
			self.cur_x += 1
			
		elif self.cur_y < player.cur_y and self.cur_y < field.y-1 and	self.cur_y+1 != ['G'] and	self.cur_y+1 != ['M'] and	self.cur_y+1 != ['B']:
			self.cur_y += 1
 




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
			self.graphic_field[player.cur_x][player.cur_y] = ['P']
			self.graphic_field[monster1.cur_x][monster1.cur_y] = ['M']
			self.graphic_field[monster2.cur_x][monster2.cur_y] = ['M']
			self.graphic_field[boss.cur_x][boss.cur_y] = ['B']
			self.graphic_field[gold.x][gold.y] = ['G']

			for y in self.graphic_field:
				for x in y:
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
		player.cur_hp = player.max_hp

#istanze
field = Field(10, 10)
gold = Gold()
player = Player(100)
monster1 = Enemy(50)
monster2 = Enemy(50)
boss = Boss(100)


#introduzione
os.system('cls')

print('''Ci  saranno  3 nemici,  denominati  con
\'M\' e \'B\'.
Il boss (B) ti uccide con un colpo solo
e può muoversi in diagonale.
Gli altri 2 mostri si possono muovere
solo a destra, sinistra, in alto oppure
in basso e ti uccidono con 2 colpi.
Il tuo obbiettivo è arrivare al tesoro (G).

Muoviti con \'w\', \'a\', \'s\', \'d\'.

-premi invio per continuare- ''')

input()

#mainloop
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



