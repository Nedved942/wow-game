import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("wow game")
running = True

font_statistics = pygame.font.SysFont("Arial", 35)

wow_dog_image = pygame.image.load("wow-piesel-sprite-1-120-105.png").convert_alpha()
tree_nr_1_image = pygame.image.load("tree-sprite-1-90-110.png").convert_alpha()
background = pygame.image.load("wow-game-background-1-2000-720.png").convert()

start_player_position_x = screen.get_width() / 2 - wow_dog_image.get_width() / 2 - 300
start_player_position_y = screen.get_height() - wow_dog_image.get_height() - 40
dog_speed = 1
start_background_position = 0
background_scroll_speed = 3
jump = False
fall = False
start_jump_speed = 15
jump_power = 8
gravity = jump_power / 16
max_jump_height = 50 * jump_power

player_position_x = start_player_position_x
player_position_y = start_player_position_y
tree_nr_1_position_x = 1200
tree_nr_1_position_y = start_player_position_y
background_position = start_background_position
jump_speed = start_jump_speed

player_rect = wow_dog_image.get_rect()
tree_nr_1_rect = tree_nr_1_image.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                dog_speed += 1
            if event.key == pygame.K_SPACE and not jump and not fall:
                jump = True
                jump_speed = start_jump_speed

    # screen.fill("gray")
    # pygame.draw.circle(screen, "red", (player_position_x, player_position_y), 100)
    speed_text = font_statistics.render(f"Speed: {dog_speed}", True, "Red")
    position_speed_text_x = screen.get_width() - speed_text.get_width()
    position_speed_text_y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position_x -= 5 * dog_speed
    if keys[pygame.K_RIGHT]:
        player_position_x += 5 * dog_speed
    # if keys[pygame.K_UP]:
    #     player_position_y -= 5 * dog_speed
    # if keys[pygame.K_DOWN]:
    #     player_position_y += 5 * dog_speed
    if dog_speed == 5:
        dog_speed = 1

    if jump and jump_speed > 0:
        if player_position_y >= max_jump_height:
            player_position_y -= jump_speed
            jump_speed -= gravity
        else:
            jump = False
            fall = True
            jump_speed = 0

    if fall:
        if player_position_y <= start_player_position_y:
            player_position_y += jump_speed
            jump_speed += gravity
        else:
            fall = False

    # print(speed)
    print(player_position_x)
    print(player_position_y)
    # print(screen.get_width()/2)
    # print(screen.get_height()/2)
    # print(jump, fall)
    # print(jump_speed, gravity)

    background_width = background.get_width()
    background_position -= background_scroll_speed
    if abs(background_position) >= background_width:
        background_position = start_background_position

    tree_nr_1_position_x -= background_scroll_speed

    player_rect.topleft = (player_position_x, player_position_y)
    tree_nr_1_rect.topleft = (tree_nr_1_position_x, tree_nr_1_position_y)

    if player_rect.colliderect(tree_nr_1_rect):
        player_position_x -= 500

    screen.blit(background, (background_position, 0))
    screen.blit(background, (background_position + background_width, 0))
    screen.blit(wow_dog_image, (player_position_x, player_position_y))
    screen.blit(tree_nr_1_image, (tree_nr_1_position_x, tree_nr_1_position_y))
    screen.blit(speed_text, (position_speed_text_x, position_speed_text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
