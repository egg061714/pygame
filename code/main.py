import pygame
import sys
from pathlib import Path
from player import Player
# 初始化 pygame
pygame.init()

# 設定視窗大小
SCREEN_WIDTH = 760
SCREEN_HEIGHT = 800
playground = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame 基本範例")

parent_path = Path(__file__).parents[1]
print(parent_path)
image_path = parent_path/ 'resource'
icon_path = image_path/ 'icon.png'
pygame.display.set_caption("Pygame 基本範例")
icon =pygame.image.load(icon_path)
pygame.display.set_icon(icon)
background = pygame.Surface(screen.get_size())
background=background.convert()
background.fill((50,50,50))
# 遊戲時鐘（用來控制FPS）
fps=120
movingScale =600/fps
player =Player(playground=playground,sensitivity = movingScale)
clock = pygame.time.Clock()



# 遊戲主迴圈
running = True
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    player.update()
    screen.blit(player.image,player.xy)
    pygame.display.update()  # 更新畫面

    # 控制每秒幀數
    dt=clock.tick(fps)

# 結束
pygame.quit()
sys.exit()


