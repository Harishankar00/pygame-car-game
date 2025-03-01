import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Animation with Adjustable Friction")

# Load background image
bg_img = pygame.image.load("background.png")  # Replace with downloaded background
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# Load car image
car_img = pygame.image.load("car.png")  # Replace with downloaded car sprite
car_img = pygame.transform.scale(car_img, (80, 40))  # Resize for better scaling

# Car properties
car_x = WIDTH // 2
car_y = HEIGHT - 100  # Adjust height to sit on the road
speed = 0
force = 0  # Set force manually
friction = 0.05  # Adjustable friction
max_speed = 12

# Fonts
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg_img, (0, 0))  # Draw background

    keys = pygame.key.get_pressed()  # Get key inputs

    # Adjust friction manually
    if keys[pygame.K_i]:  # Increase friction
        friction = min(friction + 0.005, 0.2)  # Limit max friction
    if keys[pygame.K_d]:  # Decrease friction
        friction = max(friction - 0.005, 0)  # Limit minimum friction

    # Apply force manually
    if keys[pygame.K_1]:
        force = 1
    if keys[pygame.K_2]:
        force = 2
    if keys[pygame.K_3]:
        force = 3
    if keys[pygame.K_4]:
        force = 4
    if keys[pygame.K_5]:
        force = 5
    if keys[pygame.K_6]:
        force = 6
    if keys[pygame.K_7]:
        force = 7
    if keys[pygame.K_8]:
        force = 8
    if keys[pygame.K_9]:
        force = 9

    # Movement logic
    if keys[pygame.K_LEFT]:
        speed -= force * 0.2  # Apply force to move left
    if keys[pygame.K_RIGHT]:
        speed += force * 0.2  # Apply force to move right

    # Apply friction (smooth deceleration)
    if speed > 0:
        speed -= friction
    elif speed < 0:
        speed += friction

    # Stop if speed is very small
    if abs(speed) < friction:
        speed = 0

    # Limit speed
    speed = max(-max_speed, min(max_speed, speed))

    # Move the car
    car_x += speed

    # Keep car within screen bounds
    if car_x < 0:
        car_x = 0
        speed = 0
    elif car_x > WIDTH - 80:
        car_x = WIDTH - 80
        speed = 0

    # Draw the car
    screen.blit(car_img, (car_x, car_y))

    # Display speed, force, and friction
    info_text = f"Speed: {round(speed, 1)} | Force: {force} | Friction: {round(friction, 3)}"
    text = font.render(info_text, True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Refresh screen
    clock.tick(60)  # 60 FPS

pygame.quit()
