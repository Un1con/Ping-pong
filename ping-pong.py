from pygame import *
 

win_width = 600
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))

clock = time.Clock()
fps = 60
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
        
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#platforms

right_platform = Player("right_platform.png", 550, 200, 10, 20, 100)
left_platform = Player("left_platform.png", 50, 200, 10, 20, 100)

#ball

ball = GameSprite("ball.png", 300, 230, 10, 30, 30)

#ball directions (nothing in there yet)

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((200, 255, 255))

    #platforms
    right_platform.reset()
    right_platform.update_r()
    left_platform.reset()
    left_platform.update_l()

    #ball
    ball.reset()
    

    clock.tick(fps)
    display.update()
