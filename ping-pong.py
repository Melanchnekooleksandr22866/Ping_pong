from pygame import *

back = (200, 255, 255)

init()
window = display.set_mode((900, 600))
window.fill(back)

font.init()
font_obj = font.SysFont("Arial", 36)

clock = time.Clock()
FPS = 60
game = True

def draw_midline():
    midline_width = 10
    midline_color = (255, 255, 255)
    midline_pos = (window.get_width() // 2 - midline_width // 2, 0)
    draw.rect(window, midline_color, (midline_pos[0], midline_pos[1], midline_width, window.get_height()))

class Player(sprite.Sprite):
    def __init__(self, image_path, x, y, speed, controls):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.controls = controls

    def update(self):
        keys = key.get_pressed()
        if self.controls == "letters":
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            elif keys[K_s] and self.rect.y < 595 and self.rect.bottom < 595:
                self.rect.y += self.speed
        elif self.controls == "Arrows":
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            elif keys[K_DOWN] and self.rect.y < 595 and self.rect.bottom < 595:
                self.rect.y += self.speed

class Ball(sprite.Sprite):
    def __init__(self, image_path, x, y, speed_x, speed_y):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y = -self.speed_y

    def check_collision(self, player_group):
        if sprite.spritecollide(self, player_group, False):
            self.speed_x = -self.speed_x

players = sprite.Group()
player1 = Player("player.png", 50, 300, 5, "letters")
player2 = Player("player_2.png", 850, 300, 5, "Arrows")
players.add(player1, player2)

ball = Ball("ball.png", 450, 300, 5, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    players.update()
    ball.update()
    ball.check_collision(players)

    if ball.rect.right < 0:
        message = font_obj.render("Player 2 wins!", True, (0, 255, 0))
        window.blit(message, (625, 300))
        message = font_obj.render("Player 1 loses!", True, (255, 0, 0))
        window.blit(message, (50, 300))
        display.update()
        time.delay(2000)
        game = False
    elif ball.rect.left > 950:
        message = font_obj.render("Player 2 loses!", True, (255, 0, 0))
        window.blit(message, (625, 300))
        message = font_obj.render("Player 1 wins!", True, (0, 255, 0))
        window.blit(message, (50, 300))
        display.update()
        time.delay(2000)
        game = False

    window.fill(back)
    draw_midline()
    players.draw(window)
    window.blit(ball.image, ball.rect)

    display.update()
    clock.tick(FPS)

quit()
