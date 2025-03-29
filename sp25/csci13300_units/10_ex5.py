import pygame
import random

pygame.init()
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# font to display score (length)
font = pygame.font.Font(None, 24)

# create snake
snake = [(300, 300)]
direction = (0, -20)  # direction - initially upwards
food = (random.randrange(0, screen_width, 20), random.randrange(0, screen_height, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    # move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # check food collision
    if snake[0] == food:
        food = (
            random.randrange(0, screen_width, 20),
            random.randrange(0, screen_height, 20),
        )
    else:
        snake.pop()

    # check game over (wall collision)
    if (
        snake[0][0] < 0
        or snake[0][0] >= screen_width
        or snake[0][1] < 0
        or snake[0][1] >= screen_height
    ):
        print("Wall collision detected, game over!")
        running = False

    # check game over (self-collision)
    if snake[0] in snake[1:]:
        print("Self-collision detected, game over!")
        running = False

    screen.fill((0, 0, 0))

    # draw score (length)
    text_surface = font.render("Length: {}".format(len(snake)), True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))

    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
    pygame.display.flip()
    clock.tick(10)

print("Game over!")
print("Game stats:")
print("Length:", len(snake))
