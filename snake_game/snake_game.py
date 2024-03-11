import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 640
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initial position and movement delta for the snake
x, y = 200, 200
delta_x, delta_y = 20, 0  # Changed delta to be a multiple of 20 for alignment with grid

# Initial position of the food
food_x, food_y = random.randint(0, width - 20) // 20 * 20, random.randint(0, height - 20) // 20 * 20

# List to store the positions of the snake's body parts
body_list = [(x, y)]

# Clock to control the game's speed
clock = pygame.time.Clock()

# Variable to track whether the game is over
game_over = False

# Font for displaying text
font = pygame.font.SysFont("Arial", 30)

# Function to update the snake's position and handle collisions
def update_snake():
    global x, y, food_x, food_y, game_over

    # Update snake's position
    x = (x + delta_x) % width
    y = (y + delta_y) % height

    # Check for collisions with the snake's body
    if (x, y) in body_list:
        game_over = True
        return

    # Add the new head position to the body list
    body_list.append((x, y))

    # Check if the snake eats the food
    if food_x == x and food_y == y:
        # Generate new food position
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randint(0, width - 20) // 20 * 20, random.randint(0, height - 20) // 20 * 20
    else:
        # Remove the tail of the snake
        body_list.pop(0)

    # Clear the screen
    game_screen.fill((0, 0, 0))

    # Display score
    score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))
    game_screen.blit(score, (0, 0))

    # Draw the food
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 20, 20])

    # Draw the snake's body
    for i, j in body_list:
        pygame.draw.rect(game_screen, (255, 255, 255), [i, j, 20, 20])

    # Update the display
    pygame.display.update()

# Main game loop
while True:
    # Check for game over condition
    if game_over:
        game_screen.fill((0, 0, 0))
        score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))
        game_screen.blit(score, (0, 0))
        text = font.render("Game Over", True, (255, 255, 255))
        game_screen.blit(text, (width // 2 - 100, height // 2 - 10))
        pygame.display.update()
        time.sleep(3)  # Wait for 3 seconds before quitting
        pygame.quit()
        quit()

    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if delta_x != 20:  # Prevent reversing direction
                    delta_x = -20
                    delta_y = 0
            elif event.key == pygame.K_RIGHT:
                if delta_x != -20:  # Prevent reversing direction
                    delta_x = 20
                    delta_y = 0
            elif event.key == pygame.K_UP:
                if delta_y != 20:  # Prevent reversing direction
                    delta_x = 0
                    delta_y = -20
            elif event.key == pygame.K_DOWN:
                if delta_y != -20:  # Prevent reversing direction
                    delta_x = 0
                    delta_y = 20
            else:
                continue

    # Update snake's position
    update_snake()

    # Control game speed
    clock.tick(10)  # Adjust the number to change the game's speed

# Clean up
pygame.quit()
