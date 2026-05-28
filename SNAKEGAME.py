import pygame
import sys
import random

# Khởi tạo pygame
pygame.init()
background_color = (33, 33, 33) # Màu nền
snake_color = (0, 255, 0) # Màu rắn
food_color = (255, 0, 0) # Màu mồi
text_color = (255, 255, 255) # Màu chữ

# Thiết lập cửa sổ game
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Thiết lập thời gian và khởi tạo rắn
clock = pygame.time.Clock()
snake_size = 20
snake_speed = 13
font = pygame.font.SysFont(None, 30)

# Hàm vẽ rắn
def draw_snake(snake, snake_size):
    for segment in snake:
        pygame.draw.rect(screen, snake_color, [segment[0], segment[1], snake_size, snake_size])

# Hàm vẽ điểm số
def draw_score(score):
    score_text = font.render("Score: " + str(score), True, text_color)
    screen.blit(score_text, [0, 0])

# Hàm chạy trò chơi
def game():
    global x, y, x_change, y_change
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0
    game_over = False
    game_close = False

    # Khởi tạo vị trí và độ dài ban đầu của rắn
    snake = [[x, y]]
    snake_length = 1

    # Khởi tạo vị trí mồi
    food_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:
        while game_close:
            screen.fill(background_color)
            game_over_text = font.render("Game Over! Press Q-Quit or C-Play Again", True, text_color)
            screen.blit(game_over_text, [width // 6, height // 2])
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size

        x += x_change
        y += y_change

        # Kiểm tra xem rắn có chạm vào tường không
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Cập nhật vị trí mới của rắn (thêm đầu mới)
        snake_head = [x, y]
        snake.insert(0, snake_head)

        # Kiểm tra xem rắn có ăn được mồi không
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
            food_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
            snake_length += 1
        else:
            # Nếu không ăn mồi, xóa đốt cuối cùng (đuôi) để giữ nguyên độ dài
            if len(snake) > snake_length:
                snake.pop()

        # Kiểm tra xem rắn có cắn vào thân không
        for segment in snake[1:]:
            if segment == snake_head:
                game_close = True

        # Vẽ lại màn hình
        screen.fill(background_color)
        draw_snake(snake, snake_size)
        pygame.draw.rect(screen, food_color, [food_x, food_y, snake_size, snake_size])
        draw_score(snake_length - 1)
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()