import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balance the Bridge")

# Load Images
bg_img = pygame.image.load("level2/bridge_bg.png")  # Replace with downloaded background
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

platform_img = pygame.image.load("level2/platform.png")  # Replace with downloaded platform
platform_img = pygame.transform.scale(platform_img, (200, 40))

character_img = pygame.image.load("level2/character.png")  # Replace with downloaded character sprite
character_img = pygame.transform.scale(character_img, (50, 70))

weight_img = pygame.image.load("level2/weight.png")  # Replace with downloaded weight image
weight_img = pygame.transform.scale(weight_img, (30, 30))

wind_img = pygame.image.load("level2/wind.png")  # Replace with a transparent wind effect

# Game Variables
character_x, character_y = 100, 220  # Start position
platform_x, platform_y = 300, 250  # Bridge platform position
tilt_angle = 0  # Rotation of the platform
gravity = 1  # Simulated gravity
wind_force = 0  # Wind effect on tilt
weights = []  # Stores placed weights

# Fonts
font = pygame.font.Font(None, 36)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg_img, (0, 0))  # Draw Background

    keys = pygame.key.get_pressed()  # Get Player Input

    # Move Character
    if keys[pygame.K_LEFT] and character_x > 50:
        character_x -= 3
    if keys[pygame.K_RIGHT] and character_x < WIDTH - 50:
        character_x += 3

    # Drop Weight
    if keys[pygame.K_SPACE]:
        weights.append((character_x, character_y + 50))

    # Random Wind Effect
    if random.randint(1, 100) > 98:  # Wind appears randomly
        wind_force = random.choice([-2, 2])  # Left or right push

    # Apply Tilt Based on Weights
    total_weight = len(weights)
    tilt_angle = (total_weight * 2) + wind_force  # More weight = more tilt

    # Keep Tilt Within Limits
    if tilt_angle > 10:
        tilt_angle = 10
    if tilt_angle < -10:
        tilt_angle = -10

    # Draw Platform with Rotation
    rotated_platform = pygame.transform.rotate(platform_img, tilt_angle)
    screen.blit(rotated_platform, (platform_x, platform_y))

    # Draw Character
    screen.blit(character_img, (character_x, character_y))

    # Draw Weights
    for w in weights:
        screen.blit(weight_img, w)

    # Display Wind Indicator
    if wind_force != 0:
        screen.blit(wind_img, (WIDTH - 100, 20))

    # Display Info
    text = font.render(f"Tilt: {tilt_angle}° | Wind: {wind_force}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Refresh Screen
    clock.tick(60)  # Limit FPS

pygame.quit()
