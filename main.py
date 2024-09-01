import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("wow game")
running = True

font_statistics = pygame.font.SysFont("Arial", 50)
player_position_x = screen.get_width() / 2
player_position_y = screen.get_height() / 2
speed = 1
position_speed_text_x = screen.get_width() - 300
position_speed_text_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed += 1

    screen.fill("gray")
    pygame.draw.circle(screen, "red", (player_position_x, player_position_y), 100)
    speed_text = font_statistics.render(f"Speed: {speed}", True, "Red")

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
    print(speed)

    screen.blit(speed_text, (position_speed_text_x, position_speed_text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
