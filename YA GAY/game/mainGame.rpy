init:
    # Определение персонажей игры)
    define b = Character('Борис', color="#3c00ff")
    define g = Character('Гоша', color="#ccff00e0")
    define p = Character('Поркшеян', color="#ff0000")
    define n = Character('Никита', color="#eeff00")
    define z = Character('Женя', color="#FFFF00")
    define a = Character('Арина', color="#ff008c")
    define a_s = Character('?Арина?', color="#FF0000")
    define s_s = Character('Серега', color="#26ff00")
    define d = Character('Ваня', color="#8000ff")
    define s = Character('Стас', color="#F4A460")
    define i = Character('Иван Васильевич', сolor="#1b2780")
    define v = Character('Все', color="#ffffff")
    define author = Character('Автор', color="#FFFFFF")
    define stud = Character('Студенты', сolor="#00eaff")
    define o_v = Character('Ольга Владимировна', color="#fb6b1dff")
    define k_p = Character('Константин Алексеевич', color="#a6ff00")

    # Для NVl'a:
    define nvl_1 = Character(None, kind=nvl)

    #  Теги для анимированного текста
    #  дефолт: b - жирный, i - курсив, \n - конец строки, u - подчеркивание, color=#FFFFFF - задать цвет, cps - скорость вывода текста, size - размер текста
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
    image PARA_KOMP = "bg/PARA_KOMP.jpg"
    image OBSHAGA = "bg/OBSHAGA.jpg"
    image OBSHAGA_KUHNYA = "bg/OBSHAGA_KUHNYA.jpg"
    image OBSHAGA_VHOD = "bg/OBSHAGA_VHOD.jpg"
    image PARA_INFA = "bg/PARA_INFA.jpg"
    image CHILL = "bg/CHILL.jpg"
    image TIME = "bg/TIME.jpg" 
    image BALKON_OBSHAGA = "bg/BALKON_OBSHAGA.jpg"

    # Спрайты боряна:
    image BORYA_OUTSIDE = "sprites/BORYA/BORYA_OUTSIDE.png"
    # Спрайты Гоги:
    image GOGA_OUTSIDE = "sprites/GOGA/GOGA_OUTSIDE.png"
    # Спрайты Поркша:
    image VPORKSHEYAN = "sprites/PORKSH/VPORKSHEYAN.png"
    # Спрайты Никиты:
    image NIKITA_OUTSIDE = "sprites/NEKIT/NIKITA_OUTSIDE.png"
    # Спрайты Арины:
    image ARINA_OUTSIDE = "sprites/ARINA/ARINA_OUTSIDE.png"
    image ARINA_SUCCUB = "sprites/ARINA/ARINA_SUCCUB.png"
    # Спрайты Жени:
    image ZHENYA_OUTSIDE = "sprites/ZHENYA/ZHENYA_OUTSIDE.png"
    # Спрайты Сереги:
    image SEREGA = "sprites/SEREGA/SEREGA.png"
    # Спрайты Вани:
    image DIVAN_SERIOUS = "sprites/DIVAN/DIVAN_SERIOUS.png"
    image DIVAN_CRY = "sprites/DIVAN/DIVAN_CRY.png"
    image DIVAN_SMILE = "sprites/DIVAN/DIVAN_SMILE.png"

    # Спрайты лысика:
    image KIBERPRIZRAK = "sprites/KIBERPRIZRAK/KIBERPRIZRAK.png"

    # Спрайты Ивана Васильевича:
    image IVAN_VASILIICH = "sprites/IVAN_VASILIICH/IVAN_VASILIICH.png"

    # Статы:
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
