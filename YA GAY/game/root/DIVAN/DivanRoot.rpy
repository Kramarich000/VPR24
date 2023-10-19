label DIVAN_ROOT_START:
    scene ODINOCHKA
    play sound "sounds/dgtu_zvon.mp3"
    "~ Наконец-то конец пары ~"
    show ZHENYA_OUTSIDE at right2
    show BORYA_OUTSIDE at left2
    show DIVAN_SMILE 
    with dissolve
    d "Хей, пацаны, погнали по пивку вдарим. Пятница как никак"
    z "Иди нахуй, мне прогу надо учить и вообще я бросил"
    b "Я тоже не могу. Я в Шахты еду"
    hide DIVAN_SMILE
    show DIVAN_CRY
    with dissolve
    d "..."
    d "Ну и пошли нахуй черти. Со мной Стас пойдет"
    hide DIVAN_CRY
    show DIVAN_SMILE
    with dissolve
    d "Ты же пойдешь?"
    menu:
        d "Ты же пойдешь?"
        "Да, погнали":
            d "Ура! Я в тебе не сомневался"
            d "В 18:00 жду на апеле"
            d "Ну а я и сейчас пойду"
            d "Парни, вы со мной?"

            menu:
                d "Парни, вы со мной?"

                "Пойти с ними":
                    hide DIVAN_SMILE
                    hide BORYA_OUTSIDE
                    hide ZHENYA_OUTSIDE
                    with dissolve
                    "~ Бля ~"
                    "~ И нахуй я согласился с ним бухать идти ~"
                    "~ Не просто так ведь... ~"
                    z "ЕБЛАН, ТЫ ГДЕ?!"
                    s "ИДУ! ЩА ПОССАТЬ СГОНЯЮ И БУДУ!"
                    "~ Так вот ~"
                    "~ Не просто так ведь Боря наврал что едет в Шахты ~"
                    "~ Посмотрим что из этого выйдет ~"
                    jump DIVAN_ROOT_APELSIN

                "Уйти в общагу":
                    s "Не, сорян"
                    s "У меня в есть одно дельце в общаге"
                    hide DIVAN_SMILE
                    show DIVAN_SERIOUS
                    with dissolve
                    d "Ну ладно"
                    d "Погнали"
                    hide DIVAN_SERIOUS
                    hide BORYA_OUTSIDE
                    hide ZHENYA_OUTSIDE
                    with dissolve
                    "~ Да-м... Весело. ~"
                    jump DIVAN_ROOT_PRE_OBSHAGA
            
        "Нет, прости, у меня тоже дела":
            hide DIVAN_SMILE
            show DIVAN_CRY
            with dissolve
            d "Кидала!"
            hide DIVAN_CRY
            with dissolve
            "~ Ваня ушел ~"
            v "..."
            z "БЛЯ ЕБЛАН"
            hide ZHENYA_OUTSIDE
            show BORYA_OUTSIDE at center
            with dissolve
            z "Меня подожди!"
            b "..."
            s "..."
            b "Ладно, идем в общагу"
            hide BORYA_OUTSIDE
            with dissolve
            jump DIVAN_ROOT_OBSHAGA

    return
        
    