import pygame
import random

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# font to display stats
font = pygame.font.Font(None, 24)

# player
player = pygame.Rect(100, 250, 20, 50)
is_jumping = False
jump_velocity = 0
gravity = 1

# obstacles
obstacles = []
obstacle_timer = 0

# stats
num_obstacles = 0
speed = 1
level = 1
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                # jump velocity is negative, so player goes upwards
                # because y-direction is inverted
                jump_velocity = -15

    # player jumping logic
    if is_jumping:
        player.y += jump_velocity
        jump_velocity += gravity
        if player.y >= 250:  # Ground
            player.y = 250
            is_jumping = False

    # spawn obstacles
    obstacle_timer -= 1
    if obstacle_timer < 0:
        obstacles.append(pygame.Rect(screen_width, 270, 30, 30))
        obstacle_timer = (45 + random.expovariate(1 / 25)) / speed
        # update score when obstacles are cleared
        score += 10 * speed

    # move obstacles
    for obstacle in obstacles[:]:
        obstacle.x -= 5 * speed
        if obstacle.right < 0:
            obstacles.remove(obstacle)
            num_obstacles += 1
            # update level based on number of obstacles jumped over
            if num_obstacles and not num_obstacles % (10 * level):
                level += 1
                speed = round(speed * 1.1, 1)

    # collision check
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False

    screen.fill((255, 255, 255))

    # draw stats - speed, num obstacles, level, score
    stats_text = "Speed: {}|Obstacles passed: {}|Level: {}|Score: {}".format(
        speed, num_obstacles, level, score
    )
    stats_lines = stats_text.split("|")
    for i, line in enumerate(stats_lines):
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (20, 20 * (i + 1)))

    # draw player and obstacles
    pygame.draw.rect(screen, (0, 0, 0), player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 0, 0), obstacle)
    pygame.display.flip()
    clock.tick(60)

print("Game over!")
print("Game statistics:")
print("\n".join(stats_text.split("|")))
