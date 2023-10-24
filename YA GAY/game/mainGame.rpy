init:
    # Определение персонажей игры.
    define b = Character('Борис', color="#3c00ff", callback=name_callback, cb_name="b")
    define g = Character('Гоша', color="#ccff00e0", callback=name_callback, cb_name="g")
    define p = Character('Поркшеян', color="#ff0000", callback=name_callback, cb_name="p")
    define n = Character('Никита', color="#eeff00", callback=name_callback, cb_name="n")
    define z = Character('Женя', color="#FFFF00", callback=name_callback, cb_name="z")
    define a = Character('Арина', color="#ff008c", callback=name_callback, cb_name="a")
    define a_s = Character('?Арина?', color="#FF0000", callback=name_callback, cb_name="a_a")
    define s_s = Character('Серега', color="#26ff00", callback=name_callback, cb_name="s_s")
    define d = Character('Ваня', color="#8000ff", callback=name_callback, cb_name="d")
    define s = Character('Стас', color="#F4A460", callback=name_callback, cb_name=None)
    define i = Character('Иван Васильевич', сolor="#1b2780", callback=name_callback, cb_name="i")
    define v = Character('Все', color="#ffffff", callback=name_callback, cb_name=None)
    define author = Character('Автор', color="#FFFFFF", callback=name_callback, cb_name=None)
    define stud = Character('Студенты', сolor="#00eaff", callback=name_callback, cb_name=None)
    define o_v = Character('Ольга Владимировна', color="#fb6b1dff", callback=name_callback, cb_name="o_v")

    # Для NVl'a:
    define nvl_1 = Character(None, kind=nvl)

    #  Теги для анимированного текста
    #  дефолт: b - жирный, i - курсив, \n - конец строки, u - подчеркивание, color=#FFFFFF - задать цвет, cps - скорость вывода текста
    #  bt - текст волной (bt = 20 амплитуда высоты букв)
    #  fi - плавное появление текста (fi = 1-10-100, 1 параметр хз чо делает, 2 параметр время появления, 3 параметр расстояние)
    #  sc - дрожащий текст (sc = 20 задать дрожание)
    #  rotat - вращение текста (rotat = 20 скорость вращение текста задает) 
    #  explode - взрыв текста (explode = 5 задать время через которое произойдет взрыв(в секундах))
    #  explodehalf - сильный взрыв текста (explode = 0-2 центр и время разрыва)
    #  glitch - глючный текст (glitch = 50% процент глюка)
    #  gradient - цвет1-цвет2 (градиент текст) 
    
    # Курсор
    define config.mouse = {"default" : [("gui/cursor.png", 0, 0)]}

    # Нестандартные позиции персонажей
    define left2 = Position(xalign=0.25)
    define right2 = Position(xalign=0.75)

    define slowdissolve = Dissolve(1.0)

    # Задники:
    image DGTU_BG_INSIDE = "bg/DGTU_BG_INSIDE.jpg"
    image DGTU_BG_OUTSIDE = "bg/DGTU_BG_OUTSIDE.jpg"
    image PARA_L = "bg/PARA_L.jpg"
    image APELSIN = "bg/APELSIN.jpg"
    image PARADISE = "bg/RAI.jpg"
    image SEREGA_ZVONOK = "bg/SEREGA_ZVONOK.jpg"
    image KORIDOR = "bg/KORIDOR.jpg"
    image HELL = "bg/HELL.jpg"
    image PROLOG_OCEAN = "bg/PROLOG_OCEAN.jpg"
    image NA_ULIZE = "bg/NA_ULIZE.jpg"
    image BLACK_SCREEN = "bg/BLACK_SCREEN.jpg"
    image KABINET_DEKANA = "bg/KABINET_DEKANA.jpg"
    image 1_319 = "bg/1_319.jpg"
    image ODINOCHKA = "bg/ODINOCHKA.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_KOMP = "bg/PARA_KOMP.jpg"
    image OBSHAGA = "bg/OBSHAGA.jpg"
    image OBSHAGA_KUHNYA = "bg/OBSHAGA_KUHNYA.jpg"
    image OBSHAGA_VHOD = "bg/OBSHAGA_VHOD.jpg"

    # Спрайты боряна:
    image BORYA_OUTSIDE = At("sprites/BORYA/BORYA_OUTSIDE.png", sprite_highlight("b"))
    # Спрайты Гоги:
    image GOGA_OUTSIDE = At("sprites/GOGA/GOGA_OUTSIDE.png", sprite_highlight("g"))
    # Спрайты Поркша:
    image VPORKSHEYAN = At("sprites/PORKSH/VPORKSHEYAN.png", sprite_highlight("p"))
    # Спрайты Никиты:
    image NIKITA_OUTSIDE = At("sprites/NEKIT/NIKITA_OUTSIDE.png", sprite_highlight("n"))
    # Спрайты Арины:
    image ARINA_OUTSIDE = At("sprites/ARINA/ARINA_OUTSIDE.png", sprite_highlight("a"))
    image ARINA_SUCCUB = At("sprites/ARINA/ARINA_SUCCUB.png", sprite_highlight("a_a"))
    # Спрайты Жени:
    image ZHENYA_OUTSIDE = At("sprites/ZHENYA/ZHENYA_OUTSIDE.png", sprite_highlight("z"))
    # Спрайты Сереги:
    image SEREGA = At("sprites/SEREGA/SEREGA.png", sprite_highlight("s_s"))
    # Спрайты Вани:
    image DIVAN_SERIOUS = At("sprites/DIVAN/DIVAN_SERIOUS.png", sprite_highlight("d"))
    image DIVAN_CRY = At("sprites/DIVAN/DIVAN_CRY.png", sprite_highlight("d"))
    image DIVAN_SMILE = At("sprites/DIVAN/DIVAN_SMILE.png", sprite_highlight("d"))

    # Спрайты Ивана Васильевича:
    image IVAN_VASILIICH = At("sprites/IVAN_VASILIICH/IVAN_VASILIICH.png", sprite_highlight("i"))

    default HP = 5
    default uspevaemost = 0
    default karma = 10
    default sociofob = 0
    
    python:
        # Звуковой канал:
        renpy.music.register_channel("bgs", "sfx", loop = True)
        # Открывание/закрывание глаз:
        opened = ImageDissolve("gui/eye.png", 2.0, 20, reverse=False) 
        closed = ImageDissolve("gui/eye.png", 2.0, 20, reverse=True)
        import os 
        usID = os.environ.get("USERNAME")
    
# Удобства ради теперь сцены будут наименоваться с использованием префиксов
# Название сцены должно указываться в формате представленном ниже:
# DXP_НАЗВАНИЕ_СЦЕНЫ, где X - номер дня, а P - буквенный код части дня
# Если в части дня только одна сцена - название сцены не указывается

# Все коды частей дня (Буквенный код - Название файла - Расшифровка):
# M - Morning - утро
# PX - Para_X - Пара Х, где Х - номер пары
# TX - Timeout_X - Перерыв Х, где Х - номер пары после которой перерыв
# BT - BigTimeout - Большой перерыв
# E - Evening - вечер
# N - Night - Ночь

# По подобному принципу можно создать свои собственные теги 
# В такой ситуации НЕОБХОДИМО ПРОКОМЕНТИРОВАТЬ ЕГО ПЕРЕД НАЧАЛОМ СЦЕНЫ

# Игра начинается здесь(пролог):
label start:
    jump D1M_PROLOG
