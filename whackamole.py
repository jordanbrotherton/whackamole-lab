import pygame
import random

def draw_grid(screen):
    for i in range(20):
        pygame.draw.line(screen, 0, (i * 32, 0), (i * 32, 512), 1)
    for i in range(16):
        pygame.draw.line(screen, 0, (0, i * 32), (640, i * 32), 1)

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if(mouse_x // 32 == x and mouse_y // 32 == y):
                        x = random.randrange(0,20)
                        y = random.randrange(0,16)
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32,y * 32)))
            draw_grid(screen)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
