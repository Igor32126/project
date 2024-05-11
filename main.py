from classes import*
from menu import*

"""ПРИКЛАД"""
in_menu = True
def start_game():
    global in_menu
    in_menu = False

start_text = pg.font.Font(None, 50).render("Start", True, (0,0,0))
bt_start = Button(250,250, 200, 100, (255,255,255), start_text, start_game)
"""ПРИКЛАД"""

while play:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            play = False
            
    """ПРИКЛАД"""
    if in_menu:
        bt_start.update()
        bt_start.draw()
    if not in_menu:
        win.fill((0,0,0))
    """ПРИКЛАД"""

    pg.display.update()
    clock.tick(30)


    """
    1) Створити класи Player та Enemy
    2) У settings потрібно встановити всі налаштування (картинки і тд)
    3) Створити об'єкти гравця та ворогів (додати у список/група спрайтів)
    4) Відмалювання в циклі гравця, фону, ворогів
    5) Перевірка зіткнення з ворогами та перевірка знищення
    6) Магазин -> ставити на паузу, створити кнопки, змінні
    """