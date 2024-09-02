import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("wow game")
running = True

font_statistics = pygame.font.SysFont("Arial", 35)
wow_dog_image = pygame.image.load("wow-piesel-sprite-1-120-105.png")
player_position_x = screen.get_width() / 2 - wow_dog_image.get_width() / 2
player_position_y = screen.get_height() - wow_dog_image.get_height() - 150
speed = 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed += 1

    screen.fill("gray")
    # pygame.draw.circle(screen, "red", (player_position_x, player_position_y), 100)
    speed_text = font_statistics.render(f"Speed: {speed}", True, "Red")
    position_speed_text_x = screen.get_width() - speed_text.get_width()
    position_speed_text_y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position_x -= 5 * speed
    if keys[pygame.K_RIGHT]:
        player_position_x += 5 * speed
    if keys[pygame.K_UP]:
        player_position_y -= 5 * speed
    if keys[pygame.K_DOWN]:
        player_position_y += 5 * speed
    if speed == 5:
        speed = 1

    # print(speed)
    print(player_position_x)
    print(player_position_y)
    # print(screen.get_width()/2)
    # print(screen.get_height()/2)

    screen.blit(wow_dog_image, (player_position_x, player_position_y))
    screen.blit(speed_text, (position_speed_text_x, position_speed_text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
