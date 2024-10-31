import pygame
pygame.init()

# Window setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Input Handling")

# Controller setup
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")

        # Mouse input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"Mouse button pressed at ({x}, {y})")

        # Controller input
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Joystick button {event.button} pressed")

    # Refresh screen
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
