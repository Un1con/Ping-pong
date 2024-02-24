from pygame import *
import random

init()
win_width = 600
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))

clock = time.Clock()
fps = 60
game = True

font = font.Font(None, 60)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speedX, player_speedY, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speedX = player_speedX
        self.speedY = player_speedY
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
        
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speedY
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speedY
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speedY
        
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speedY

#platforms
            
right_platform = Player("right_platform.png", 550, 200, None, 10, 20, 100)
left_platform = Player("left_platform.png", 50, 200, None, 10, 20, 100)

#ball direction

ball_direction_x = random.randint(-5, 5)
ball_direction_y = random.randint(-5, 5)

if ball_direction_x == 0:
    ball_direction_x = 5

if ball_direction_y == 0:
    ball_direction_y = 5

#ball

ball = GameSprite("ball.png", 300, 230, ball_direction_x, ball_direction_y, 30, 30)

#score

left_score = 0
right_score = 0


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

    r_score = font.render("{}".format(right_score), True, (0, 0, 0))
    window.blit(r_score, (520, 20))

    l_score = font.render("{}".format(left_score), True, (0, 0, 0))
    window.blit(l_score, (70, 20))

    #ball
    ball.reset()

    ball.rect.y += ball_direction_y
    ball.rect.x += ball_direction_x

    if ball.rect.y <= 0:
        ball_direction_y = abs(ball_direction_y)
    
    if ball.rect.y >= win_height - 30:
        ball_direction_y = -ball_direction_y

    if ball.rect.colliderect(left_platform.rect):

        ball_direction_x = abs(ball_direction_x) + 0.5

        
    if ball.rect.colliderect(right_platform.rect):

        a = random.randint(1, 2)

        ball_direction_x = -ball_direction_x - 0.5

        if a == 1:

            ball_direction_y = abs(ball_direction_y)
        else:

            ball_direction_y = -ball_direction_y

    if ball.rect.x <= 20:

        right_score += 1

        ball.rect.x = 300
        ball.rect.y = 230
        ball_direction_x = abs(ball_direction_x) - 3

        if ball_direction_x == 0:
            ball_direction_x = 2
    
    if ball.rect.x >= 580:

        left_score += 1

        ball.rect.x = 300
        ball.rect.y = 230
        ball_direction_x = -ball_direction_x + 3

        if ball_direction_x >= 0:
            ball_direction_x = -2

    

    clock.tick(fps)
    display.update()
