from init import *

# Main loop
run = True
while run:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Exit Controlg
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.QUIT]:
        run = False

    pygame.Surface.fill(window, (0, 0, 0))
    #Update Display
    pygame.display.update()
