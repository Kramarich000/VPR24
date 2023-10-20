init:
    # Определение персонажей игры.
    define b = Character('Борис', color="#3c00ff")
    define g = Character('Гоша', color="#ccff00e0")
    define p = Character('Поркшеян', color="#ff0000")
    define n = Character('Никита', color="#eeff00")
    define z = Character('Женя', color="#FFFF00")
    define a = Character('Арина', color="#ff008c")
    define a_s = Character('?Арина?', color="#FF0000")
    define r = Character('Рома', color="#ffffff")
    define s_s = Character('Серега', color="#26ff00")
    define d = Character('Ваня', color="#8000ff")
    define s = Character('Стас', color="#F4A460")
    define i = Character('Иван Васильевич', сolor="#1b2780")
    define v = Character('Все', color="#ffffff")
    define author = Character('Автор', color="#FFFFFF")
    define stud = Character('Студенты', сolor="#00eaff")

    # Для NVL:
    define nvl_p = Character("Поркшеян", color="#ff0000", kind=nvl)


    # Курсор
    define config.mouse = {"default" : [("gui/cursor.png", 0, 0)]}

    # Нестандартные позиции персонажей
    define left2 = Position(xalign=0.25)
    define right2 = Position(xalign=0.75)

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
    image WAKE_UP = "bg/WAKE_UP.jpg"
    image NA_ULIZE = "bg/NA_ULIZE.jpg"
    image BLACK_SCREEN = "bg/BLACK_SCREEN.jpg"
    image KABINET_DEKANA = "bg/KABINET_DEKANA.jpg"
    image 1_319 = "bg/1_319.jpg"
    image ODINOCHKA = "bg/ODINOCHKA.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_2 = "bg/PARA_2.jpg"
    image PARA_KOMP = "bg/PARA_KOMP.jpg"

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

    # Спрайты Ивана Васильевича:
    image IVAN_VASILIICH = "sprites/IVAN_VASILIICH/IVAN_VASILIICH.png"

    default HP = 5
    default uspevaemost = 0
    default karma = 10
    default soqiofob = 0
    
    python:
        renpy.music.register_channel("bgs", "sfx", loop = True)


# Игра начинается здесь(пролог):
label start:
    scene PROLOG_OCEAN
    play music "music/neheart_-_snowfall_75941790.mp3"
    author "Что есть жизнь?"
    author "Жизнь - это дар, что бы познавать себя и знать, как сотворить прекрасное для своей души, которая способна жить, перемещаясь в любые измерения, где есть жизнь."
    author "А душа - это что?"
    author "Это вы и есть внутри себя. человек думает и чувствует внутри себя таким, какой он есть, но выразить это словами не может..."
    author "...боится что его не поймут другие. "
    author "А что такое судьба? И существует ли она?"
    author "Есть мнение, что человек не может изменить свою судьбу? Это правда!"
    author "Судьба не поддается влиянию и изменению. Вопрос в том предначертана ли судьба?"
    author "Ведь если бы это было так, то по факту мы с вами становимся марионетками в чей-то большой игре под названием судьба."
    author "Это как определенный сценарий, в котором нам как читателям все известно."
    author "Но..."
    stop music fadeout (2.0)
    play bgs "sounds/alarm-clock-beep-1_zjgin-vd.mp3"
    author "..."
    author "..."
    author "..."
    author "...Что?"
    show WAKE_UP
    with dissolve
    stop bgs
    play music "music/Мышь - Жвачка.mp3" fadein(2.0)
    "..."
    "Ой-ой-ой моя голова..."
    "8 УТРА ?"
    "..."
    "Понедельник..."
    "Так..."
    "ТВОЮ МАТЬ! У меня же сегодня учеба!"
    "Щас еще опоздаю и буду отчислен еще даже не придя ни на одну пару...бегом!"
    "Стас взял пропуск и вышел из общаги"
    hide WAKE_UP
    show NA_ULIZE
    with dissolve
    stop music
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    s "Быстрей быстрей идем на взлет!"
    s "Так 1 корпус..."
    s "..."
    s "Ага! Аудитория 384"
    s "Ну с Богом"
    stop bgs
    hide NA_ULIZE
    show BLACK_SCREEN
    with dissolve
    s "Так-с ну что же хех"
    hide BLACK_SCREEN
    show PROLOG_OCEAN
    with dissolve
    play music "music/neheart_Reidenshi_-_distorted_memories_75718831.mp3"
    s "Эм всем привет! Как вы поняли меня зовут Стас и это моя история"
    s "Недавно мне стукнуло 19 лет, так что родители сказали: либо ты учишься либо идешь в армию"
    s "Меня 2 вариант не устроил..."
    s "И по этой причине я сейчас здесь в Донском государственном техническом университете"
    s "Но я бы хотел начать с начала..."
    s "Я решил попробовать свои силы в рамках новой образовательной программы под названием: 'Школа X'"
    s "И вроде по началу мне даже нравилось: я ходил на пары, работал в команде, да и товарищи были рядом..."
    s "Но что-то не то..."
    s "..."
    s "Не клеилась моя учёба на 1 курсе"
    s "В один момент я решился поговорить со своим деканом.."
    stop music
    show KABINET_DEKANA
    play sound "sounds/stuk-v-dver-kostyashkami-paltsev.mp3"
    s "Иван Васильич можно?"
    show IVAN_VASILIICH
    with dissolve
    i "Проходи, присаживайся"
    s "Иван Васильич у меня к вам есть разговор"
    i "В чем дело?"
    s "Я хочу перевестись..."
    i "Почему? Тебя что-то не устраивает?"
    s "Ну нет, но...в общем да меня не устраивает мое текущее положение"
    i "Есть ли какая-то веская причина твоего решения?"
    s "Иван Васильевич, сейчас у меня сложный период в жизни"
    i "Может быть я могу чем-то помочь? У меня есть знакомый психолог хороший, можешь ему высказаться, тебе полегчает"
    s "Нет, простите со мной все в порядке, меня просто...."
    s "...напрягает что на меня давят родители и сейчас..."
    s "И сейчас я в сложной жизненной ситуации, пожалуйста войдите в мое положение прошу вас"
    i "Эх...Станислав ты хорошо учишься так что я сделаю исключение для тебя"
    s "Спасибо!"
    i "Я подготовлю документы"
    s "Хорошо, спасибо вам"
    hide IVAN_VASILIICH
    hide KABINET_DEKANA
    show PROLOG_OCEAN
    with dissolve
    play music "music/neheart_Reidenshi_-_distorted_memories_75718831.mp3"
    s "Итак, я оказался в группе ВПР24..."
    s "Не знаю верный ли был это выбор, но..."
    s "...уже выбора точно нет"
    s "Так что вперед и с песней!"
    s "Надеюсь, что со второго раза мне повезет!"
    author "А может и нет)"
    hide PROLOG_OCEAN
    stop music
    show NA_ULIZE
    with dissolve
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    s "Черт, надо спешить"
    s "Опаздываю"
    stop bgs
    show DGTU_BG_INSIDE
    with dissolve
    play bgs "sounds/turniket.mp3"
    s "Так пропуск, где же ты"
    s "Ага нашел!"
    s "Давай же долбанный турникет!"
    s "Есть!"
    s "3 этаж..."
    stop bgs
    play sound "sounds/dgtu_zvon.mp3"
    s "Твою мать быстрее на 1 же пару опаздывать..."
    show PARA_L
    s "Так это вроде тут"
    s "Заходим"
    stop sound
    jump DGTU_OUTSIDE

label DGTU_OUTSIDE:
    play bgs "sounds/zvuki-na-ulice-goroda.mp3"
    scene DGTU_BG_OUTSIDE
    show BLACK_SCREEN
    with dissolve
    "Тем временем...."
    hide BLACK_SCREEN
    with dissolve
    g "Боря быстрей мы сейчас опоздаем, нас Поркш убьёт"
    show GOGA_OUTSIDE at left2
    show BORYA_OUTSIDE at right2
    with dissolve
    b "Да иду я уже"
    g "О Ванек дарова"
    show DIVAN_SMILE at center
    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at right
    with dissolve
    d "Дарова че вы тут стоите?"
    g "Как-никак тебя ждем"
    d "А пара скоро?"
    d "Несколько минут еще"
    d "Да пофиг..."
    b "Ага пофиг у тебя мало того что долг, так еще и посещаемость хромает"
    g "Вот именно так что пойдем"
    d "Ладно...на ковер к Поркшу не особо хочется"
    hide DIVAN_SMILE
    hide NIKITA_OUTSIDE
    show NIKITA_OUTSIDE at left2
    with dissolve
    n "Всем здарова челики аче вы не на паре?"
    n "Пойдемте а то опоздаем"
    show ZHENYA_OUTSIDE at right2
    with dissolve
    z "Я уже устал 60 заказов в день, сдохну скоро"
    z "Староста пойдем уже"
    hide DIVAN_SMILE
    show ARINA_OUTSIDE at center
    with dissolve
    a "Да задолбали, не называйте меня старостой!"
    stop music fadeout(2.0)
    stop bgs fadeout(2.0)
    hide NIKITA_OUTSIDE
    hide BORYA_OUTSIDE
    hide ZHENYA_OUTSIDE
    hide ARINA_OUTSIDE
    show GOGA_OUTSIDE at center
    with dissolve
    g "Я думаю нам пора, пойдем"
    jump in_DGTU

label apelsin:
    scene APELSIN
    show ZHENYA_OUTSIDE
    with dissolve
    z "Гарик поймал..."
    play bgs "sounds/TELEPHONE_ZVONOK.mp3"
    z "Опа-а...Серега звонит"
    "Женя поднимает телефон и включает видеозвонок"
    stop bgs
    jump SEREGA_ZVONIT

label in_DGTU:
    scene DGTU_BG_INSIDE
    play bgs "sounds/turniket.mp3"
    show BORYA_OUTSIDE
    with dissolve
    b "Ух мы внутри"
    hide BORYA_OUTSIDE
    show GOGA_OUTSIDE
    with dissolve
    g "Ага давай быстрей а то опоздаем на пару"
    stop bgs fadeout(2.0)
    play sound "sounds/dgtu_zvon.mp3"
    hide GOGA_OUTSIDE
    show ZHENYA_OUTSIDE
    with dissolve
    z "Погодите я карту найти не могу"
    # Спрайт Арины
    a "Да пошли уже задолбал"
    stop sound fadeout(3.0)
    jump NA_PARE_PORKHA

label SEREGA_ZVONIT:
    scene SEREGA_ZVONOK
    play sound "sounds/ueban.mp3"
    s_s "АЛЕ идиот где ты?"
    z "А че уже пара началась?"
    s_s "Ты даун она уже 5 минут как идет бегом!"
    z "Ладно иду уже"
    jump NA_PARE_PORKHA

label NA_PARE_PORKHA:
    scene PARA_L
    show BLACK_SCREEN
    with dissolve
    "В это время в 1-384..."
    hide BLACK_SCREEN
    show VPORKSHEYAN
    with dissolve
    play music "sounds/DELTA_SHTRIX.mp3"
    "~ Блин как скучно... ~"
    "~ Как они его лекции слушают только? ~"
    "..."
    "~ О опоздал кто-то ~"
    p "Пара уже 10 минут идет вы где ходите?"
    v "Простите за опоздание! Виталий Маркосович!"
    p "Чтобы это было в последний раз"
    p "Иначе следующего раза не будет"
    "Слава Богу я не опоздал..."
    p "Так продолжаем..."
    "..."
    "..."
    "..."
    "~ Не я не могу уже...скууука ~"
    menu:
        "Что делать?"
        "Уснуть":
            p "Чтобы продемонстрировать вам..."
            $ uspevaemost -= 1
            show BLACK_SCREEN 
            with dissolve
            "..."
            "..."
            "..."
            play sound "sounds/dgtu_zvon.mp3"
            hide VPORKSHEYAN
            hide BLACK_SCREEN
            show PARA_L
            with dissolve
            s "Ой что уже все что-ли?"
            s "Так нужно бы \"своих\" для начала найти. Познакомиться хоть"
            stop bgs fadeout(1.0)
        "Внимательно слушать":
            $ uspevaemost += 1
            p "{b}Теория вероятностей{/b} — это наука, которая изучает мир случайностей и пытается их предсказать. Здесь встречаются такие понятия, как «события» и «вероятности», у которых, в свою очередь, есть свои свойства и операции — о них мы поговорим чуть позже."
            nvl_p "Проще всего продемонстрировать, как работает теория вероятностей, на примере подбрасывания монетки. В этом случае у нас есть два варианта: орёл или решка, а значит, шанс выпадения каждой из сторон одинаковый и составляет 50\%."
            nvl_p "Но как убедиться, что это действительно так? Например, я могу подбросить монетку десять раз, и мне магическим образом девять раз подряд выпадет орёл и один раз решка. Значит ли это, что шанс выпадения орла — 90\%? Конечно, нет — и у этого есть научное объяснение."
            nvl_p "Дело в том, что теория вероятностей рассматривает случайные события в рамках бесконечности. Иными словами, если мы будем подбрасывать монетку бесконечное количество раз, то шансы выпадения орла или решки будут приближаться к 50\%."
            nvl_p "Такая же логика работает и для других случайных явлений — например, шанс выпадания числа 5 на игральном кубике равен 1 к 6, а вероятность того, что молния ударит в одно и то же место дважды — примерно 1 к 500."
            nvl_p "Теория вероятностей помогает нам предсказывать шанс возникновения различных событий, когда ответ не такой однозначный и на события влияет множество факторов."
            nvl_p "Мы упомянули слова «событие» и «вероятность», но не рассказали, что они вообще значат в контексте теории вероятностей. Давайте разбираться."
            nvl_p "{b}Событие{/b} — это всё, что может произойти, когда мы совершаем какое-то действие. Например, если мы бросаем монетку, то событие — это выпадение орла или решки. Чтобы обозначать события, используют заглавные буквы латинского алфавита. Например, для орла можем выбрать букву A, а для решки — B."
            nvl_p "Существует много разных видов и классификаций событий, но в этой статье мы остановимся на основных четёрых:"
            nvl_p "{b}Достоверные{/b} — те, которые точно произойдут. Если бросить стакан на пол, то с вероятностью 100\% он полетит вниз."
            nvl_p "{b}Невозможные{/b} — те, которые никогда не произойдут. Если бросить тот же стакан на пол, то он никогда не полетит вверх."
            nvl_p "Мораль: не стоит бросать стаканы на пол, если, конечно, вы не на МКС"
            stud "Ахахахах"
            nvl_p "Случайные — те, которые могут произойти, а могут и не произойти. Например, если мы бросаем игральный кубик, то не можем с уверенностью сказать, что выпадет число 2."
            nvl_p "Несовместимые — те, которые исключают друг-друга. Например, при подбрасывании монетки может выпасть либо орёл, либо решка — оба одновременно они выпасть не могут."
            nvl_p "Если собрать все несовместимые события вместе, они будут называться полной группой событий. Это множество событий, одно из которых обязательно случится, если мы совершаем действие, а другие — не произойдут никогда. Например, когда мы бросаем игральный кубик, может выпасть только одна из сторон."
            nvl_p "А теперь поговорим про непосредственно вероятность"
            nvl_p "Вероятность — это число, которое обозначает шанс возникновения события. Например, вероятность выигрыша в лотерею может составлять 1 к 1 000 000."
            nvl_p "Мы записывали значения вероятностей в процентах и отношениях, но математикам удобнее располагать их в диапазоне от 0 до 1. Если вероятность равна 0, то событие никогда не произойдёт, а если 1 — точно произойдёт. Всё, что посередине, — это случайные события."
            nvl_p "Самый простой способ вычислить вероятность — поделить число благоприятных событий на общее число возможных событий."
            nvl_p "Например, если всего в колоде 36 карт, а мы хотим достать короля пик, то вероятность этого события равна 1/36, или 0,03. Если бы нас устроил любой из королей, то вероятность была бы равна 4/36 — то есть 0,1."
            nvl_p "К формулам мы ещё вернёмся, а пока отметим, что вероятность — это не всегда точное предсказание, а лишь оценка шанса возникновения события. Как следует из закона больших чисел, если шанс выпадения орла и решки равен 50\%, это не означает, что они будут выпадать по очереди."
            nvl_p "Ещё вероятность может быть условной — или зависеть от другого события. Например, если мы хотим вытащить любой туз из колоды карт, шанс равен 4/36."
            nvl_p "Но если до этого кто-то уже вытащил одного туза, то вероятность будет равна 3/35. Это потому, что в колоде стало на одну карту меньше и количество благоприятных событий тоже уменьшилось."
            nvl_p "С определениями закончили — теперь давайте узнаем, как событиями можно управлять..."
            hide VPORKSHEYAN
            with dissolve
            "бла бла бла"
            "..."
            play sound "sounds/dgtu_zvon.mp3"
            s "Неужели, я думал усну епт"
            s "Так нужно бы 'своих' для начала найти. Познакомиться хоть"
            stop sound fadeout(2.0)
    jump POSLE_PARI_PORKHA

label POSLE_PARI_PORKHA:
    scene KORIDOR 
    with dissolve
    play music "sounds/Universitet.mp3"
    "~ Выйдя из аудитории я увидел нескольких ребят ~"
    show GOGA_OUTSIDE
    show ZHENYA_OUTSIDE at right
    show BORYA_OUTSIDE at left
    with dissolve
    menu:
        "Что делать?"
        "Подойти к ним":
            g "Капец пара душная"
            z "Согласен лучше бы дома поспал"
            b "Аче я в ДГТУ в куртке ?"
            "Я не нашел другого спрайта...сорян..."
            z "У нас 10 минут еще есть"
            hide GOGA_OUTSIDE
            with dissolve
            show DIVAN_SMILE at center
            with dissolve
            d "О! Получается мы с Женей идем курить?!"
            z "Погнали!"
            hide ZHENYA_OUTSIDE 
            with dissolve
            hide DIVAN_SMILE
            with dissolve
            "Женя с Ваней ушли на апель"
            show GOGA_OUTSIDE with dissolve
            g "Идем, иначе опоздаем"
            s "Эй, ребят вы ВПР24?"
            g "Да, а что ты хотел?"
            s "О значит мне по адресу, меня зовут Станислав, можно просто - Стас"
            g "А нам Серега говорил что новенький седня должен был прийти"
            g "Меня если что Гоша зовут"
            g "Это Борис"
            b "Дарова я да"
            g "А это Ва..."
            g "О..."
            g "Они уже свалили"
            g "..."
            g "Ууу нам в 8 корпус... Идем скорее, иначе опоздаем"
            stop music fadeout(2.0)
            jump WITH_PAZANI
        "Лучше пройду мимо":
            "~ Думаю что не стоит подходить, а то обознаюсь еще ~"
            $ soqiofob += 1
            stop music fadeout(2.0)
            jump ODIN

label ODIN:
    scene ODINOCHKA
    play music "sounds/Universitet.mp3"
    "~ Так-с аудитория 8- ~"
    "~ Ага, нашел! Вроде не опоздал ~"
    show GOGA_OUTSIDE at right2
    show BORYA_OUTSIDE at left2
    with dissolve
    "~ Хм, у этих ребят видимо, пара здесь же, может стоило подойти к ним? ~"
    "..."
    "~ Только их вроде было четверо ... ~"
    "..."
    "~ В любом случае времени на это уже нет ~"
    "~ Пора в аудиторию ~"
    jump ODIN_NA_PARU

    return

label WITH_PAZANI:
    scene PARA_KOMP
    play music "sounds/Universitet.mp3"
    show GOGA_OUTSIDE at left2
    show BORYA_OUTSIDE at right2
    with dissolve
    g "Ну вроде успели"
    s "А что у нас сейчас?"
    g "Какая-то херня. Карен потом придумает"
    b "Кайф"
    jump SECOND_PARA

label ODIN_NA_PARU:
    scene PARA_KOMP
    play music "sounds/Universitet.mp3"
    "Стас вошел в аудиторию"
    "В ней он снова увидел этих ребят"
    show GOGA_OUTSIDE at left2
    show BORYA_OUTSIDE at right2
    with dissolve
    g "О привет ты новенький"
    s "да"
    b "Нам Серега говорил что у нас опять новенький"
    #крч тут развить максимально стеснительный диалог
    jump SECOND_PARA

label SECOND_PARA:
    scene PARA_KOMP
    play music "sounds/Universitet.mp3"
    show GOGA_OUTSIDE at left
    show BORYA_OUTSIDE at left2
    show Какой-то_Препод at right
    with dissolve
    "Какой-то Препод" "Так, ребята. Все на места. Пара началась"
    return

label DEATH_BAD:
    scene HELL
    play bgs "sounds/HELL_KRIK.mp3"
    author "Пизда тебе"
    "БЛЯТЬ ЧТО ГДЕ Я?"
    "..."
    "..."
    "..."
    "..."
    "..."
    show ARINA_SUCCUB
    a_s "Ну привет"
    " - Концовка: Вечность с Ариной - "
    return

label DEATH_GOOD:
    scene PARADISE
    author "ТЫ ЕБЛАН ВСЕ HP ПРОЕБАЛ"
    return
