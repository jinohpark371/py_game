import sys
from implements import Basic, Block, Paddle, Ball
import config
import random

import pygame
from pygame.locals import QUIT, Rect, K_ESCAPE, K_SPACE


pygame.init()
pygame.key.set_repeat(3, 3)
surface = pygame.display.set_mode(config.display_dimension)

fps_clock = pygame.time.Clock()

paddle = Paddle()
ball1 = Ball()
BLOCKS = []
ITEMS = []
BALLS = [ball1]
life = config.life
start = False


def create_blocks():
    for i in range(config.num_blocks[0]):
        for j in range(config.num_blocks[1]):
            x = config.margin[0] + i * (config.block_size[0] + config.spacing[0])
            y = (
                config.margin[1]
                + config.scoreboard_height
                + j * (config.block_size[1] + config.spacing[1])
            )
            color_index = j % len(config.colors)
            color = config.colors[color_index]
            block = Block(color, (x, y))
            BLOCKS.append(block)


def tick():
    global life, BLOCKS, ITEMS, BALLS, paddle, ball1, start

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                start = True
            paddle.move_paddle(event)

    for ball in BALLS:
        if start:
            ball.move()
        else:
            ball.rect.centerx = paddle.rect.centerx
            ball.rect.bottom = paddle.rect.top

        for block in BLOCKS[:]:
            if block.alive and ball.rect.colliderect(block.rect):
                new_item = block.collide()  # 아이템 생성
                if new_item:
                    ITEMS.append(new_item)  # 생성된 아이템을 ITEMS 리스트에 추가
                ball.dir = 360 - ball.dir + random.randint(-5, 5)
                break  # 충돌한 블록 하나만 처리

        ball.collide_paddle(paddle)
        ball.hit_wall()
        if not ball.alive():
            BALLS.remove(ball)

    # 아이템 이동 및 충돌 처리
    for item in ITEMS[:]:
        item.move()
        if item.rect.colliderect(paddle.rect):
         if item.type == "red":
            life += 1  # 점수 추가
         elif item.type == "blue":
           
            
            # 공을 3개로 복제
            new_balls = []
            for ball in BALLS:
                # 두 개의 새 공 생성 (복제)
                ball1 = Ball(pos=(ball.rect.centerx, ball.rect.centery))
                ball1.dir = ball.dir + random.randint(-15, 15)
                
                ball2 = Ball(pos=(ball.rect.centerx, ball.rect.centery))
                ball2.dir = ball.dir - random.randint(-15, 15)
                
                new_balls.extend([ball1, ball2])
            BALLS.extend(new_balls)
            
         ITEMS.remove(item)
        elif item.rect.top > config.display_dimension[1]:
         ITEMS.remove(item)

def main():
    global life, BLOCKS, ITEMS, BALLS, paddle, ball1, start
    my_font = pygame.font.SysFont(None, 50)
    mess_clear = my_font.render("Cleared!", True, config.colors[2])
    mess_over = my_font.render("Game Over!", True, config.colors[2])
    create_blocks()

    while True:
        tick()
        surface.fill((0, 0, 0))
        paddle.draw(surface)

        for block in BLOCKS:
            block.draw(surface)

        for item in ITEMS:  # 아이템 그리기
            item.draw(surface)

        cur_score = config.num_blocks[0] * config.num_blocks[1] - len(BLOCKS)
        score_txt = my_font.render(f"Score : {cur_score * 10}", True, config.colors[2])
        life_font = my_font.render(f"Life: {life}", True, config.colors[0])

        surface.blit(score_txt, config.score_pos)
        surface.blit(life_font, config.life_pos)

        if len(BALLS) == 0:
            if life > 1:
                life -= 1
                ball1 = Ball()
                BALLS = [ball1]
                start = False
            else:
                surface.blit(mess_over, (200, 300))
        elif all(block.alive == False for block in BLOCKS):
            surface.blit(mess_clear, (200, 400))
        else:
            for ball in BALLS:
                ball.draw(surface)

        pygame.display.update()
        fps_clock.tick(config.fps)


if __name__ == "__main__":
    main()
