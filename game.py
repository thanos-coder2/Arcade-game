import pygame
import random

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Pac-Man intro music.mp3")
pygame.mixer.music.play(-1)

pygame.display.set_caption("Εργασια σχολης")

clock = pygame.time.Clock()
cell_size = 60

# map
game_map = [
    "########################",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "#----------------------#",
    "#----------------------#",
    "#----------------------#",
    "#----------------------#",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "#---##-------------##--#",
    "########################"
]

# σχεδιασμός map
def draw_map(screen, game_map):
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if tile == "#":
                pygame.draw.rect(
                    screen,
                    (0, 0, 255),
                    (x * cell_size, y * cell_size, cell_size, cell_size)
                )

# κλάση Pacman
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, game_map):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
            if game_map[new_y][new_x] != "#":
                self.x = new_x
                self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (
                self.x * cell_size + cell_size // 2,
                self.y * cell_size + cell_size // 2
            ),
            cell_size // 2 - 4
        )

# κλάση Enemy
class Enemy:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def move(self, game_map, player):
        dx = player.x - self.x
        dy = player.y - self.y

        if abs(dx) > abs(dy):
            step_x = 1 if dx > 0 else -1
            step_y = 0
        else:
            step_x = 0
            step_y = 1 if dy > 0 else -1

        new_x = self.x + step_x
        new_y = self.y + step_y

        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
            if game_map[new_y][new_x] != "#":
                self.x = new_x
                self.y = new_y

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x * cell_size,
                self.y * cell_size,
                cell_size,
                cell_size
            )
        )

# reset game
def reset_game():
    global player, enemy, game_over
    player = Pacman(1, 1)
    enemy = Enemy(len(game_map[0]) - 2, len(game_map) - 2)
    game_over = False

# δημιουργία αντικειμένων
player = Pacman(1, 1)
enemy = Enemy(len(game_map[0]) - 2, len(game_map) - 2)

#υψος και παχος αναλογα το μεγεθος της στυλης του map
WIDTH = len(game_map[0]) * cell_size
HEIGHT = len(game_map) * cell_size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# run game no stop game over
running = True
game_over = False
font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)

# main loop
# Ελέγχει συμβάντα, κινήσεις, σύγκρουση και σχεδίαση
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0, game_map)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0, game_map)
        if keys[pygame.K_UP]:
            player.move(0, -1, game_map)
        if keys[pygame.K_DOWN]:
            player.move(0, 1, game_map)

        if pygame.time.get_ticks() % 2 == 0:
            enemy.move(game_map, player)

        if player.x == enemy.x and player.y == enemy.y:
            game_over = True

    screen.fill((0, 0, 0))
    draw_map(screen, game_map)
    player.draw(screen)
    enemy.draw(screen)
    
    #game over με  και εμφανιση μυνηματος
    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2 - text.get_height() // 2)
        )

        restart_text = small_font.render(
            "ΠΑΤΗΣΕ ΤΟ SPACE ΓΙΑ RESTAST", True, (255, 255, 255)
        )
        screen.blit(
            restart_text,
            (WIDTH // 2 - restart_text.get_width() // 2,
             HEIGHT // 2 + 50)
        )

    pygame.display.update()
    clock.tick(10)

pygame.quit()
