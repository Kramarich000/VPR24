label DIVAN_ROOT_START:
    scene ODIN
    play sound "sounds/dgtu_zvon.mp3"
    "~ Наконец-то конец пары ~"
    show ZHENYA at right2
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
        
    