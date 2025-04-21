import pygame
import sys

# 初始化 pygame
pygame.init()

# 設定視窗大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame 基本範例")



# 遊戲時鐘（用來控制FPS）
fps=120
clock = pygame.time.Clock()



# 遊戲主迴圈
running = True
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()  # 更新畫面

    # 控制每秒幀數
    dt=clock.tick(fps)

# 結束
pygame.quit()
sys.exit()
