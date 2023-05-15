#Serial experiments Lain DC1029
#Объявление персонажей игры
define ln = Character("Лэйн", color="#7f88db", image = 'lain')
define b = Character ("Бикэ", color="#d9ac8d")
define n = Character(None, kind=nvl)

#добавим музычки!
define audio.mainmenu = "audio/music/11111_xYTmt9Cq.mp3"

#Игра начнется здесь...
label start:
#наказываем музыку играть тут
 play music mainmenu
 
 
 image menu_slideshow:
  "gui/main_bg/bg menu1.png" with dissolve
  pause 1
  "gui/main_bg/bg menu2.png" with dissolve 
  pause 1
  "gui/main_bg/bg menu3.png" with dissolve
  pause 1
  repeat
#эта строка внизу отвечает за показ фона
 scene bg lain room1
 
#эта строка отвечает за вывод спрайта
 show lain sad_2 
 #далее идут строки диалога
 ln """Я хочу поговорить..
 
 . . Но с кем?
 """
 "И в этот же миг из-за угла выходит пёсик"
 show lain surprised_2
 b "ваф!"
 ln exhausted_2 "Бикэ!! {w} Это мой плюшевый пёсик!.."
 scene lain_beko
 with pixellate
 ln "Ура! Теперь мне есть с кем поговорить!"
 ln "Я не одинока!"
 pause 0.5
 scene black with fade
#Здесь мы вызывваем меню одноимённой командой 
#если хотиv выбор без текста в текст боксе то ничего не пишем, а если хотим то пишем в  таких скобках "" 
menu:
 "{color=#4B0082}Проснись{/color}":
  jump son
#jump отвечает за переход к развилкам
#return - окончание выборов
return
label son:
 window hide
 n """ {color=#808080} Лейн просыпается от кошмара, в холодном поту, со сбитым дыханием.
 
 {color=#808080}Ей все еще видится, что ее руки в крови и проводах. 
 
 {color=#808080}Она смотрит на свое рабочее место, после чего рывком кидается к нему. 
 
 {color=#808080}Она судорожно перебирает платы, провода и находит свою плюшевую игрушку. 
 
 {color=#808080}Лейн облегченно выдыхает, все еще содрогаясь от ужаса. 
 
 {color=#808080}«Теперь я могу начать заново....» {/color}"""
 nvl clear
 nvl hide
 scene sleepy_lain with fade
 ln """.. Что?
 
 Я . . Исчезну?
 
 Почему все мои связи пропадают?
 """
 "Неспеша покинув кровать она направляется к двери, прислонив ухо к ней"