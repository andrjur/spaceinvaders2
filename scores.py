import pygame.font


class Scores():
    """ счёт """

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (125, 15, 10)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()

    def image_score(self):
        """ из текста в графику """
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (15, 18, 25))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """  отрисуем """
        self.screen.blit(self.score_img, self.score_rect)
