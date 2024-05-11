import pygame as pg

pg.init()

win_width = 500
win_height = 500

win = pg.display.set_mode((win_width, win_height))

play = True

clock = pg.time.Clock()

score = 0

level = 1


game_state = {
    "level": level,
    "score": score
}