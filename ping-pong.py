from pygame import*

back = (200,255,255)

window = display.set_mode((700, 500))
window.fill(back)

clock= time.Clock()
FPS = 60
game = True

def update_1(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed

def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
