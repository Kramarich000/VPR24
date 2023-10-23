label D1T1:
    scene KORIDOR 
    with dissolve
    play music "sounds/Universitet.mp3"
    "~ Выйдя из аудитории я увидел нескольких ребят ~"
    "~ Хм, по-моему, вон тот что слева сидел прямо передо мной ~"
    "~ Может стоит подойти, познакомиться с ними? ~"
    show GOGA_OUTSIDE
    show ZHENYA_OUTSIDE at right
    show BORYA_OUTSIDE at left
    with dissolve
    window hide
    menu:
        "Подойти к ним":
            $ sociofob -= 1
            window show
            g "Капец пара душная"
            z "Согласен лучше бы дома поспал"
            b "Аче я в ДГТУ в куртке ?"
            "Я не нашел другого спрайта...сорян..."
            z "У нас 10 минут еще есть"
            z "А кстати в каком корпусе следующая пара?"
            g "В этом же"
            hide GOGA_OUTSIDE
            with dissolve
            show DIVAN_SMILE at center
            with dissolve
            d "10 минут и 1 корпус...{w}хм..."
            d "О! Получается мы с Женей идем курить?!"
            z "Да ты гений 2+2 сложил.Погнали!"
            hide ZHENYA_OUTSIDE 
            with dissolve
            hide DIVAN_SMILE
            with dissolve
            "Женя с Ваней ушли на апельсин"
            show GOGA_OUTSIDE with dissolve
            g "Идем, иначе опоздаем"
            "~ Сейчас ~"
            s "Эй, ребят вы ВПР24?"
            g "Да, а что ты хотел?"
            "~ А вот это уже интересно ~"
            s "О значит мне по адресу, меня зовут Станислав, можно просто - Стас"
            g "А нам Серега говорил что новенький сегодня должен был прийти"
            g "Меня, если что, Гоша зовут"
            g "Это Борис"
            b "Здарова это я, да"
            g "А это Ва..."
            g "О..."
            g "Они же свалили"
            g "..."
            g "Hам в 1-3XX... Идем скорее, иначе опоздаем, а у нас на матлогику опаздывать нежелательно"
            s "Пойдем"

        "Лучше пройду мимо":
            window show
            "~ Думаю что не стоит подходить, а то обознаюсь еще ~"
            $ sociofob += 1

    stop music fadeout(2.0)
    jump D1P2_PERED_PAROY