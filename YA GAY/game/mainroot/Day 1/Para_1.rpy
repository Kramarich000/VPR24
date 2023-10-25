label D1P1:
    scene PARA_L
    show BLACK_SCREEN
    with dissolve
    "В это время в 1-384..."
    hide BLACK_SCREEN
    show VPORKSHEYAN
    with dissolve
    p "Сегодня мы разберем понятие теории вероятностей и разберем базовые понятия внутри этой темы, это необходимо чтобы составить первоначальное представление о..."
    "~ Как же скучно... ~"
    "~ Как они его лекции слушают только? ~"
    window hide
    pause
    window show
    play sound "sounds/half-bathroom-door-knock_zy6lmond.mp3"
    "~ А? ~"
    "~ О опоздал кто-то ~"
    p "Пара уже 10 минут идет вы где ходите?"
    v "Простите за опоздание, Виталий Маркосович!"
    p "Чтобы это было в последний раз"
    p "{glitch}{sc}{color=#ff0000}{b}Иначе следующего раза не будет{/b}{/color}{/sc}{/glitch}"
    "Слава Богу я не опоздал..."
    p "Так, продолжаем..."
    p "...сущности теории вероятностей и понять какую роль она играет в нашей жизни..."
    p "Я сейчас там болтунов выгоню отсюда!"
    p "Поэтому приготовьтесь, так сказать, переключить свое мышление..."
    window hide
    pause
    pause
    pause
    window show
    "~ Не я не могу уже... Cкууука ~"
    window hide
    menu:
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
        "Внимательно слушать":
            play music "sounds/DELTA_SHTRIX.mp3"
            $ uspevaemost += 1
            p "Так записываем"
            nvl_1 "{b}Теория вероятностей{/b} — это наука, которая изучает мир случайностей и пытается их предсказать. Здесь встречаются такие понятия, как «события» и «вероятности», у которых, в свою очередь, есть свои свойства и операции — о них мы поговорим чуть позже." with dissolve
            nvl_1 "Проще всего продемонстрировать, как работает теория вероятностей, на примере подбрасывания монетки. В этом случае у нас есть два варианта: орёл или решка, а значит, шанс выпадения каждой из сторон одинаковый и составляет 50\%."
            nvl_1 "Но как убедиться, что это действительно так? Например, я могу подбросить монетку десять раз, и мне магическим образом девять раз подряд выпадет орёл и один раз решка. Значит ли это, что шанс выпадения орла — 90\%? Конечно, нет — и у этого есть научное объяснение."
            nvl clear # так можно nvl чистить
            nvl_1 "Дело в том, что теория вероятностей рассматривает случайные события в рамках бесконечности. Иными словами, если мы будем подбрасывать монетку бесконечное количество раз, то шансы выпадения орла или решки будут приближаться к 50\%."
            nvl_1 "Такая же логика работает и для других случайных явлений — например, шанс выпадания числа 5 на игральном кубике равен 1 к 6, а вероятность того, что молния ударит в одно и то же место дважды — примерно 1 к 500."
            nvl_1 "Теория вероятностей помогает нам предсказывать шанс возникновения различных событий, когда ответ не такой однозначный и на события влияет множество факторов."
            nvl_1 "Мы упомянули слова «событие» и «вероятность», но не рассказали, что они вообще значат в контексте теории вероятностей. Давайте разбираться."
            nvl_1 "{b}Событие{/b} — это всё, что может произойти, когда мы совершаем какое-то действие. Например, если мы бросаем монетку, то событие — это выпадение орла или решки. Чтобы обозначать события, используют заглавные буквы латинского алфавита. Например, для орла можем выбрать букву A, а для решки — B."
            nvl clear
            nvl_1 "Существует много разных видов и классификаций событий, но на этой лекции мы остановимся на основных четырёх:"
            nvl_1 "{b}Достоверные{/b} — те, которые точно произойдут. Если бросить стакан на пол, то с вероятностью 100\% он полетит вниз."
            nvl_1 "{b}Невозможные{/b} — те, которые никогда не произойдут. Если бросить тот же стакан на пол, то он никогда не полетит вверх."
            nvl_1 "Мораль: не стоит бросать стаканы на пол, если, конечно, вы не на МКС"
            stud "Ахахахах"
            nvl_1 "{b}Случайные{/b} — те, которые могут произойти, а могут и не произойти. Например, если мы бросаем игральный кубик, то не можем с уверенностью сказать, что выпадет число 2."
            nvl_1 "{b}Несовместимые{/b} — те, которые исключают друг-друга. Например, при подбрасывании монетки может выпасть либо орёл, либо решка — оба одновременно они выпасть не могут."
            nvl clear
            nvl_1 "Если собрать все несовместимые события вместе, они будут называться полной группой событий. Это множество событий, одно из которых обязательно случится, если мы совершаем действие, а другие — не произойдут никогда. Например, когда мы бросаем игральный кубик, может выпасть только одна из сторон."
            nvl_1 "А теперь поговорим про непосредственно вероятность"
            nvl_1 "{b}Вероятность{/b} — это число, которое обозначает шанс возникновения события. Например, вероятность выигрыша в лотерею может составлять 1 к 1 000 000."
            nvl_1 "Мы записывали значения вероятностей в процентах и отношениях, но математикам удобнее располагать их в диапазоне от 0 до 1. Если вероятность равна 0, то событие никогда не произойдёт, а если 1 — точно произойдёт. Всё, что посередине, — это случайные события."
            nvl_1 "Самый простой способ вычислить вероятность — поделить число благоприятных событий на общее число возможных событий."
            nvl_1 "Например, если всего в колоде 36 карт, а мы хотим достать короля пик, то вероятность этого события равна 1/36, или 0,03. Если бы нас устроил любой из королей, то вероятность была бы равна 4/36 — то есть 0,1."
            nvl clear
            nvl_1 "К формулам мы ещё вернёмся, а пока отметим, что вероятность — это не всегда точное предсказание, а лишь оценка шанса возникновения события. Как следует из закона больших чисел, если шанс выпадения орла и решки равен 50\%, это не означает, что они будут выпадать по очереди."
            nvl_1 "Ещё вероятность может быть условной — или зависеть от другого события. Например, если мы хотим вытащить любой туз из колоды карт, шанс равен 4/36."
            nvl_1 "Но если до этого кто-то уже вытащил одного туза, то вероятность будет равна 3/35. Это потому, что в колоде стало на одну карту меньше и количество благоприятных событий тоже уменьшилось."
            nvl_1 "С определениями закончили — теперь давайте узнаем, как событиями можно управлять..."
            window hide
            pause   
            stop music fadeout(2.0)        
            play sound "sounds/dgtu_zvon.mp3"
            p "Так, старосты мне списки отсутствующих и все свободны"
            hide VPORKSHEYAN
            with dissolve
            s "Неужели{w}, я думал усну"
    s 'Так нужно бы "своих" для начала найти. Познакомиться хоть' 

    stop sound fadeout(5.0)
    jump D1T1