import pygame
import sys
from pathlib import Path
from player import Player
from missile import MyMissile 
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

keyCountX = 0
keyCountY = 0
Missiles=[]
launchMissile = pygame.USEREVENT+1
# 遊戲主迴圈
running = True



while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyCountX += 1
                player.to_the_left()
            if event.key == pygame.K_d:
                keyCountX += 1
                player.to_the_right()
            if event.key == pygame.K_s:
                keyCountY += 1
                print(keyCountY)
                player.to_the_bottom()
            if event.key == pygame.K_w:
                keyCountY += 1
                player.to_the_top()
            if event.key == pygame.K_SPACE:
                m_x = player.x+20
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player._x + 80
                Missiles.append(MyMissile(playground,(m_x, m_y),movingScale))
                pygame.time.set_timer(launchMissile,400)           
            



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                if keyCountX == 1:
                    keyCountX = 0
                    player.stop_x()
                else:
                    keyCountX -= 1
            if event.key == pygame.K_s or event.key == pygame.K_w:
                if keyCountY == 1:
                    keyCountY = 0
                    player.stop_y()
                else:
                    keyCountY -= 1
            
            if event.key == pygame.K_SPACE:
                pygame.time.set_timer(launchMissile,0)


        if event.type == launchMissile:
                m_x = player.x+20
                m_y = player.y
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))
                m_x = player._x + 80
                Missiles.append(MyMissile(xy=(m_x, m_y), playground=playground, sensitivity=movingScale))


    screen.blit(background,(0,0))
    Missiles = [item for item in Missiles if item.available]
    for m in Missiles: 
        m.update()
        screen.blit(m.image,m.xy)
    player.update()
    screen.blit(player.image,player.xy)
    pygame.display.update()  # 更新畫面

    # 控制每秒幀數
    dt=clock.tick(fps)

# 結束
pygame.quit()
sys.exit()


