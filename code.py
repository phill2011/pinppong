from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    # конструктор класса
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.init(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < height - 80:
            self.rect.y += self.speed

win_width = 1000
win_height = 800
display.set_caption("ПынгПонгг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
ship = Player(plarT, 5, win_height - 100, 80, 100, 10)
while run:

    for i in event.get():
        if i.type == QUIT:
            run = False
