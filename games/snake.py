import pygame
import random
from core.sound import play_click, play_lose


class SnakeGame:
    def __init__(self, username):
        self.username = username

    def start(self):
        pygame.init()

        width, height = 600, 400
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("🐍 Snake Game")

        clock = pygame.time.Clock()

        snake = [(100, 100)]
        direction = (10, 0)

        food = (random.randrange(0, width, 10),
                random.randrange(0, height, 10))

        score = 0
        font = pygame.font.SysFont("Arial", 20)

        paused = False   # ✅ NEW

        running = True

        while running:
            screen.fill((30, 30, 47))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_p:   # ✅ PAUSE KEY
                        paused = not paused

                    if not paused:
                        play_click()
                        if event.key == pygame.K_UP:
                            direction = (0, -10)
                        elif event.key == pygame.K_DOWN:
                            direction = (0, 10)
                        elif event.key == pygame.K_LEFT:
                            direction = (-10, 0)
                        elif event.key == pygame.K_RIGHT:
                            direction = (10, 0)

            if not paused:   # ✅ STOP GAME WHEN PAUSED
                head = (snake[0][0] + direction[0],
                        snake[0][1] + direction[1])
                snake.insert(0, head)

                if head == food:
                    score += 1
                    food = (random.randrange(0, width, 10),
                            random.randrange(0, height, 10))
                else:
                    snake.pop()

                if (head in snake[1:] or
                    head[0] < 0 or head[0] >= width or
                    head[1] < 0 or head[1] >= height):
                    play_lose()
                    running = False

            # Draw snake
            for segment in snake:
                pygame.draw.rect(screen, (0, 255, 0),
                                 (*segment, 10, 10))

            # Draw food
            pygame.draw.rect(screen, (255, 0, 0),
                             (*food, 10, 10))

            # Score
            score_text = font.render(f"Score: {score}",
                                     True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # ✅ SHOW PAUSE TEXT
            if paused:
                pause_text = font.render("PAUSED (Press P)",
                                         True, (255, 255, 0))
                screen.blit(pause_text, (200, 180))

            pygame.display.flip()
            clock.tick(10)

        pygame.quit()
        return
