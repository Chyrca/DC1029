#Serial experiments Lain DC1029
#Объявление персонажей игры
define ln = Character("Лэйн", color="#7f88db", image = 'lain')
define o = Character ("Бог", color="#edc5c5")
define b = Character ("Бикэ", color="#d9ac8d")

#добавим музычки!
define audio.mainmenu = "audio/music/duvet8bit.mp3"

#Игра начнется здесь...
label start:
#наказываем музыку играть тут
 play music mainmenu
#эта строка внизу отвечает за показ фона
 scene bg lain room1
 
#эта строка отвечает за вывод спрайта
 show lain sad 
 #далее идут строки диалога
 ln "Я хочу поговорить.."
 ln "..Но с кем?"
 show lain surprised
 b "ваф!"
 ln exhausted "Бикэ!! {w} Это мой плюшевый пёсик!.."
 scene lain_beko
 with pixellate
 ln "Ура! Теперь мне есть с кем поговорить!"
 ln "Я не одинока!"
 return