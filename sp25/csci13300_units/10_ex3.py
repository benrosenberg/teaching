import pygame

# use random to generate initial direction of ball
import random

# initialize pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# use clock to keep track of frames
clock = pygame.time.Clock()

# font to display score with
font = pygame.font.Font(None, 300)

# Game objects
paddle_length = 100
paddle_width = 20
paddle_right = pygame.Rect(
    screen_width - 50, screen_height // 2, paddle_width, paddle_length
)
paddle_left = pygame.Rect(50, screen_height // 2, paddle_width, paddle_length)
ball = pygame.Rect(screen_width // 2, screen_height // 2, 15, 15)

# choose a random direction out of the 4 diagonal ones to have the ball start moving
directions = [[4, 4], [4, -4], [-4, -4], [-4, 4]]
ball_speed = random.choice(directions)

# keep track of points for left and right players
points = {"left": 0, "right": 0}

# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # paddle movement
    keys = pygame.key.get_pressed()

    # left paddle: use W/S keys to move paddle
    if keys[pygame.K_w] and paddle_left.top > 0:
        # move_ip: move in-place
        paddle_left.move_ip(0, -5)
    if keys[pygame.K_s] and paddle_left.bottom < screen_height:
        paddle_left.move_ip(0, 5)

    # right paddle: use W/S keys to move paddle
    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.move_ip(0, -5)
    if keys[pygame.K_DOWN] and paddle_right.bottom < screen_height:
        paddle_right.move_ip(0, 5)

    # ball movement and collision
    ball.move_ip(ball_speed)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] *= -1
    # need to restart if ball goes out of bounds
    if ball.left <= 0 or ball.right >= screen_width:
        # if ball goes out of bounds on left, then right gets 1 point
        if ball.left <= 0:
            points["right"] += 1
        # if ball goes out of bounds on right, then left gets 1 point
        if ball.right >= screen_width:
            points["left"] += 1
        # reset ball location to center
        # easiest to just recreate ball
        ball = pygame.Rect(screen_width // 2, screen_height // 2, 15, 15)
        # reset ball direction randomly
        ball_speed = random.choice(directions)

    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        # just invert x-direction if either paddle is touched
        ball_speed[0] *= -1

    # drawing
    screen.fill((0, 0, 0))

    # display score with big numbers on either side
    text_surface = font.render(
        "{}    {}".format(points["left"], points["right"]), True, (100, 100, 100, 0.5)
    )
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)

    pygame.draw.rect(screen, (255, 255, 255), paddle_left)
    pygame.draw.rect(screen, (255, 255, 255), paddle_right)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    pygame.display.flip()
    clock.tick(60)
