import pygame
import sys
from bullets import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):
    """ обработка событий """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            if event.key == pygame.K_a:
                gun.mleft = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False


def update(bgcolor, screen, stats, sc, gun, inos, bullets):
    """  обновление экрана """
    screen.fill(bgcolor)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    """  обновление пули после верха экрана """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        stats.score += 5
        sc.image_score()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, gun, inos, bullets):
    """ пушку задрали """
    if stats.life > 0:
        stats.life -= 1
        bullets.empty()
        gun.create_gun()
        # for alive_ino in inos.sprites():
        #     alive_ino.rect.y -= 350
        # inos.empty()
        # create_army(screen, inos)

        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(ststs, screen, gun, inos, bullets):
    """  обновление приш """
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        print(8765)
        gun_kill(ststs, screen, gun, inos, bullets)

    inos_check(ststs, screen, gun, inos, bullets)


def inos_check(stats, screen, gun, inos, bullets):
    """  конец """
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break


def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    screen_width = 400
    number_ino_x = (screen_width - 2*ino_width) // ino_width

    for row_number in range(3):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width * (ino_number+1)
            ino.y = ino_height * (row_number+1)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height * (2*row_number+1)
            inos.add(ino)
