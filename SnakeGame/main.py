import random
import pygame
from pygame.locals import *
import sys
from main_menu import Main_menu
import time
from update_user import update_user

pygame.init()

FramePerSec = pygame.time.Clock()
clock = pygame.time.Clock()

WIDTH = 599
HEIGHT = 599
RHEIGHT = 629
BLOCK = int(30)  # the size of every square
LEVEL = 0
SPEED = 10
SCREEN = pygame.display.set_mode((WIDTH, RHEIGHT))

snake_color = (32, 32, 32)
background_color = (33, 181, 250)
f1_color = (82, 237, 65)
f2_color = (82, 237, 65)
f3_color = (82, 237, 65)
text_color = (255, 234, 0)
head_color = (255, 0, 0)
border_color = (128, 128, 128)

score_font = pygame.font.SysFont("Arial", 15)


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Snake:
	def __init__(self, snake_pos):
		self.body = snake_pos

	def draw(self):
		# draw body part
		for body in self.body[1:]:
			pygame.draw.rect(
				SCREEN,
				snake_color,
				pygame.Rect(
					body.x * BLOCK,
					body.y * BLOCK,
					BLOCK,
					BLOCK,
				)
			)
		head = self.body[0]  # draw head
		pygame.draw.rect(
			SCREEN,
			head_color,
			pygame.Rect(
				head.x * BLOCK,
				head.y * BLOCK,
				BLOCK,
				BLOCK,
			)
		)

	def move(self, dx, dy):
		# Move body
		for idx in range(len(self.body) - 1, 0, -1):
			self.body[idx].x = self.body[idx - 1].x  # position body[i] = body[i-1]
			self.body[idx].y = self.body[idx - 1].y
		# Move head
		self.body[0].x += dx
		self.body[0].y += dy

		# Check whether snake leaves the playing area
		if self.body[0].x > WIDTH // BLOCK:
			self.body[0].x = 0
		elif self.body[0].x < 0:
			self.body[0].x = WIDTH // BLOCK
		elif self.body[0].y < 0:
			self.body[0].y = WIDTH // BLOCK
		elif self.body[0].y > HEIGHT // BLOCK:
			self.body[0].y = 0

	def check_collision_food(self, food):
		if food.pos.x == self.body[0].x and food.pos.y == self.body[0].y:
			return True
		else:
			return False

	def check_collision_border(self, borders):
		for pos in borders:
			if pos.x == self.body[0].x and pos.y == self.body[0].y:
				return True

		return False

	def check_collision_snake(self):
		for pos in self.body[1:]:
			if self.body[0].x == pos.x and self.body[0].y == pos.y:
				return True
		return False



class Food:
	def __init__(self):
		self.pos = None
		self.weight = None
		self.spawn_time = None
		self.color = None

	def draw(self):
		if self.weight == 1:
			self.color = f1_color
		elif self.weight == 2:
			self.color = f2_color
		elif self.weight == 3:
			self.color = f3_color

		pygame.draw.rect(
			SCREEN,
			self.color,
			pygame.Rect(
				self.pos.x * BLOCK,
				self.pos.y * BLOCK,
				BLOCK,
				BLOCK,
			)
		)

	def new_pos(self, snake_list, border_list):
		while True:
			x, y = random.randint(0, WIDTH // BLOCK), random.randint(0, HEIGHT // BLOCK)
			pos = Point(x, y)
			if (pos not in border_list) and (pos not in snake_list):
				return pos

	def create_new(self, snake_list, border_list, cur_time):
		self.weight = random.randint(1, 3)
		self.pos = self.new_pos(snake_list, border_list)
		self.spawn_time = cur_time

class Border:
	def __init__(self, lvl):
		self.lvl = lvl
		self.border_list = []

	def load_border(self):
		path = "/Users/nurstanduisengaliyev/Documents/Python/pp2-22B031491/tsis10/SnakeGame/levels/" + str(self.lvl) + ".txt"
		with open(path, 'r') as f:
			border_rows = f.readlines()

		for i, line in enumerate(border_rows):
			for j, value in enumerate(line):
				if value == '#':
					self.border_list.append(Point(j, i))

	def draw(self):
		for i in self.border_list:
			pygame.draw.rect(SCREEN, border_color, (i.x * BLOCK, i.y * BLOCK, BLOCK, BLOCK))

def get_string_body(body):
	str1 = str(body[0].x) + ", " + str(body[1].y)
	for pos in body[1:]:
		# "x, y; x2, y2; x3, y3
		str1 += "; " + str(pos.x) + ', ' + str(pos.y)
	return str1

def draw_text(score, lvl):
	txt_sur1 = score_font.render(f"Score = {score}", True, (0, 0, 0))
	txt_sur2 = score_font.render(f"Level = {lvl}", True, (0, 0, 0))
	SCREEN.blit(txt_sur1, (15, (HEIGHT // BLOCK + 1) * BLOCK + 5))
	SCREEN.blit(txt_sur2, (WIDTH - 100, (HEIGHT // BLOCK + 1) * BLOCK + 5))

def runGame(username, lvl, score, snake_pos, direction):
	pygame.display.set_caption("SnakeGame")
	# now, with currect state, we will state our game
	# 0 - left, 1 - right, 2 - up, 3 - down
	# created borders
	dx, dy = 0, 0
	if direction == 0:
		dx, dy = -1, 0
	if direction == 1:
		dx, dy = 1, 0
	if direction == 2:
		dx, dy = 0, -1
	if direction == 3:
		dx, dy = 0, 1
	# 0 - left, 1 - right, 2 - up, 3 - down
	# created dx, dy
	snake = Snake(snake_pos)
	border = Border(lvl)
	border.load_border()
	food = Food()
	food.create_new(snake.body, border.border_list, time.time())
	is_started = False
	pause = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				# closing the window, so we should insert into table current state
				cur_dir = None
				if dx == -1:
					cur_dir = 0
				if dx == 1:
					cur_dir = 1
				if dy == -1:
					cur_dir = 2
				if dy == 1:
					cur_dir = 3
				update_user(username, lvl, score, get_string_body(snake.body), cur_dir)
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					pause = not pause
				if event.key == K_UP and dy != 1:
					dx, dy = 0, -1
					is_started = True
				elif event.key == K_DOWN and dy != -1:
					dx, dy = 0, 1
					is_started = True
				elif event.key == K_LEFT and dx != 1:
					dx, dy = -1, 0
					is_started = True
				elif event.key == K_RIGHT and dx != -1:
					dx, dy = 1, 0
					is_started = True

		if pause == True:
			continue
		SPEED = min(9 * pow(1.30, score/4), 25)
		tail_pos = None
		if is_started:
			tail_pos = Point(snake.body[-1].x, snake.body[-1].y)
			snake.move(dx, dy)

		if is_started and (snake.check_collision_snake() or snake.check_collision_border(border.border_list)):
			# Lost the game should insert into database (0, 0, )
			cur_dir = None
			if dx == -1:
				cur_dir = 0
			if dx == 1:
				cur_dir = 1
			if dy == -1:
				cur_dir = 2
			if dy == 1:
				cur_dir = 3
			body_pos = f"{WIDTH // 30 // 2}, {HEIGHT // 30 // 2}; {WIDTH // 30 // 2 + 1}, {HEIGHT // 30 // 2}"
			update_user(username, 0, 0, body_pos, 0)
			pygame.quit()
			sys.exit()


		if is_started and snake.check_collision_food(food):
			score += food.weight
			snake.body.append(tail_pos)
			food.create_new(snake.body, border.border_list, time.time())

		if time.time() - food.spawn_time >= 4:
			food.create_new(snake.body, border.border_list, time.time())


		SCREEN.fill(background_color)
		pygame.draw.rect(SCREEN, (250, 250, 250), pygame.Rect(0, (HEIGHT // BLOCK + 1) * BLOCK, WIDTH, BLOCK))
		draw_text(score, lvl)
		food.draw()
		border.draw()
		snake.draw()
		pygame.display.update()

		if score >= 9 and lvl < 2:  # next level
			lvl += 1
			score = 0
			border = Border(lvl)
			border.load_border()
			pause = False
			is_started = False
			dx, dy = -1, 0
			# username, lvl, score, snake_pos, direction
			body_pos = get_snake_pos(f"{WIDTH // 30 // 2}, {HEIGHT // 30 // 2}; {WIDTH // 30 // 2 + 1}, {HEIGHT // 30 // 2}")
			snake = Snake(body_pos)
			food.create_new(snake.body, border.border_list, time.time())
			cur_dir = None
			if dx == -1:
				cur_dir = 0
			if dx == 1:
				cur_dir = 1
			if dy == -1:
				cur_dir = 2
			if dy == 1:
				cur_dir = 3
			update_user(username, lvl, score, get_string_body(snake.body), cur_dir)


		clock.tick(SPEED)


# lvl, score, body_pos, direction

def get_snake_pos(a):
	l1 = a.split(';')
	positions = []
	for pos in l1:
		x, y = pos.split(',')
		positions.append(Point(int(x), int(y)))

	return positions

def main():
	mainMenu = Main_menu(WIDTH, RHEIGHT)
	cur_state = mainMenu.runGame(SCREEN)
	snake_pos = get_snake_pos(cur_state[3])
	username = cur_state[0]
	lvl = cur_state[1]
	score = cur_state[2]
	direction = cur_state[4]
	runGame(username, lvl, score, snake_pos, direction)

if __name__ == "__main__":
	main()
