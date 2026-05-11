from gamelib import *


#functions
def main_update():
    main.draw()

 
    if keys.Pressed[K_a]:
        main.x -= 10
    if keys.Pressed[K_d]:
        main.x += 10
    if keys.Pressed[K_w]:
        main.y -= 5
   
        
#main program
game = Game(1000,800,"Seek a Way Out")
bk = Animation("images/crystalcave.png", 6, game, 9600/5, 2160/2, 2)
bk.resizeTo(game.width, game.height + 50)
game.setBackground(bk)

def positionObjects(object):
    for i in range(len(object)):   
        x = randint(50, 750)
        y = -randint(100, 2000)
        s = randint(4, 5)
        object[i].moveTo(x, y)
        object[i].setSpeed(s, 180)
        object[i].visible = True 

'''
#platforms
platform1 = Image("images/platform(1).png", game)
platform1.resizeBy(-50)
platform1.moveTo(150, 190)

platform2 = Image("images/platform(2).png", game)
platform2.resizeBy(-50)
platform2.moveTo(430, 355)

platform3 = Image("images/platform(3).png", game)
platform3.resizeBy(-50)
platform3.moveTo(270, 350)

platform4 = Image("images/platform(4).png", game)
platform4.resizeBy(-50)
platform4.moveTo(400, 200)

platform5 = Image("images/platform(5).png", game)
platform5.resizeBy(-50)
platform5.moveTo(550, 350)

platform6 = Image("images/platform(6).png", game)
platform6.resizeBy(-50)
platform6.moveTo(700, 345)

platform7 = Image("images/platform(7).png", game)
platform7.resizeBy(-50)
platform7.moveTo(770, 500)

platform8 = Image("images/platform(8).png", game)
platform8.resizeBy(-50)
platform8.moveTo(470, 510)
'''

#platforms
platform1 = Image("images/platform(1).png", game)
platform1.resizeBy(-50)
#platform1.collisionBorder = "rectangle"
platform1.moveTo(125, 240)

platform2 = Image("images/platform(2).png", game)
platform2.resizeBy(-50)
#platform2.collisionBorder = "rectangle"
platform2.moveTo(365, 355)

platform3 = Image("images/platform(3).png", game)
platform3.resizeBy(-50)
#platform3.collisionBorder = "rectangle"
platform3.moveTo(145, 350)

platform4 = Image("images/platform(4).png", game)
platform4.resizeBy(-50)
#platform4.collisionBorder = "rectangle"
platform4.moveTo(400, 150)

platform5 = Image("images/platform(5).png", game)
platform5.resizeBy(-50)
#platform5.collisionBorder = "rectangle"
platform5.moveTo(550, 350)

platform6 = Image("images/platform(6).png", game)
platform6.resizeBy(-50)
#platform6.collisionBorder = "rectangle"
platform6.moveTo(700, 415)

platform7 = Image("images/platform(7).png", game)
platform7.resizeBy(-50)
#platform7.collisionBorder = "rectangle"
platform7.moveTo(795, 525)

platform8 = Image("images/platform(8).png", game)
platform8.resizeBy(-50)
platform8.moveTo(470, 605)

#crystal
crystal1 = Image("images/crystal1.png", game)
crystal1.moveTo(340, 550)
crystal1.resizeBy(-20)

crystal2 = Image("images/crystal2.png", game)
crystal2.moveTo(850, 480)
crystal2.resizeBy(-20)

crystal3 = Image("images/crystal3.png", game)
crystal3.moveTo(125, 310)
crystal3.resizeBy(-20)

crystal4 = Image("images/crystal4.png", game)
crystal4.moveTo(600, 310)
crystal4.resizeBy(-20)


#stone platforms
stone1 = Image("images/stoneplat1.png", game)
stone1.moveTo(400, 250)

stone2 = Image("images/stoneplat2.png", game)
stone2.moveTo(750, 410)

stone3 = Image("images/stoneplat3.png", game)
stone3.moveTo(500, 550)

stone4 = Image("images/stoneplat4.png", game)
stone4.moveTo(800, 650)

stone5 = Image("images/stoneplat5.png", game)
stone5.moveTo(500, 410)

stone6 = Image("images/stoneplat6.png", game)
stone6.moveTo(200, 400)

stone7 = Image("images/stoneplat6.png", game)
stone7.moveTo(750, 150)

#lava platforms

#short lava tile 
lava1 = Image("images/lavaplat1.png", game)
lava1.resizeBy(50)
lava1.moveTo(150, 650)

lava2 = Image("images/lavaplat2.png", game)
lava2.resizeBy(50)
lava2.moveTo(150, 250)

#lava3 = Image("images/lavaplat3.png", game)
#lava3.resizeBy(50)
#lava3.moveTo(700, 250)

lava4 = Image("images/lavaplat4.png", game)
lava4.resizeBy(50)
lava4.moveTo(850, 450)

#lava5 = Image("images/lavaplat5.png", game)
#lava5.resizeBy(50)
#lava5.moveTo(400, 250)

#long lava tile 
lava6 = Image("images/lavaplat6.png", game)
lava6.resizeBy(80)
lava6.moveTo(400, 750)

lava6_2 = Image("images/lavaplat6 - 2.png", game)
lava6_2.resizeBy(80)
lava6_2.moveTo(600, 750)
#long lava tile 

#lava7 = Image("images/lavaplat7.png", game)
#lava7.resizeBy(50)
#lava7.moveTo(700, 550)

#lava8 = Image("images/lavaplat8.png", game)
#lava8.resizeBy(50)
#lava8.moveTo(700, 550)

#long lava tile 
lava9 = Image("images/lavaplat9.png", game)
lava9.resizeBy(80)
lava9.moveTo(400, 550)

lava9_2 = Image("images/lavaplat9 - 2.png", game)
lava9_2.resizeBy(80)
lava9_2.moveTo(600, 550)

lava10 = Image("images/lavaplat10.png", game)
lava10.resizeBy(80)
lava10.moveTo(400, 350)

lava10_2 = Image("images/lavaplat10 - 2.png", game)
lava10_2.resizeBy(80)
lava10_2.moveTo(600, 350)

lava11 = Image("images/lavaplat11.png", game)
lava11.resizeBy(80)
lava11.moveTo(400, 150)

lava11_2 = Image("images/lavaplat11 - 2.png", game)
lava11_2.resizeBy(80)
lava11_2.moveTo(600, 150)


#level 2 gif
waterfall = Animation("images/waterfall1.png", 8, game, 2055/5, 1024/2, 2)
waterfall.resizeBy(-50)
waterfall.moveTo(400, 470)

waterfall2 = Animation("images/waterfall2.png", 8, game, 1345/5, 1024/2, 2)
waterfall2.resizeBy(-55)
waterfall2.moveTo(600, 200)

#level 3 gif
risinglava = Animation("images/lava.png", 3, game, 2723/3, 564, 3)
risinglava.resizeBy(15)
risinglava.y = 1200
risinglava.setSpeed(1, 360)

flame = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
flame.collisionBorder = "rectangle"
flame.resizeBy(-40)
flame.moveTo(550, 700)

flame2 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
flame2.collisionBorder = "rectangle"
flame2.resizeBy(-40)
flame2.moveTo(300, 500)

flame3 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
flame3.collisionBorder = "rectangle"
flame3.resizeBy(-40)
flame3.moveTo(600, 305)

flame4 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
flame4.collisionBorder = "rectangle"
flame4.resizeBy(-40)
flame4.moveTo(370, 305)

flame5 = Animation("images/flame.png", 49, game, 460/5, 1470/10, 3)
flame5.collisionBorder = "rectangle"
flame5.resizeBy(-40)
flame5.moveTo(700, 500)


#start screen image
title = Image("images/seekawayout.png", game)
title.y = 100

story = Image("images/story.png", game)
story.y = 350
story_off = Image("images/story.png", game)
story_on = Image("images/story2.png", game)

storyText = Image("images/storytext.png", game)
storyText.visible = False
storyText.resizeTo(game.width, game.height)

play = Image("images/play.png", game)
play.y = 650
play_off = Image("images/play.png", game)
play_on = Image("images/play2.png", game)

howtoplay = Image("images/howtoplay.png", game)
howtoplay.y = 500
howtoplay_off = Image("images/howtoplay.png", game)
howtoplay_on = Image("images/howtoplay2.png", game)

howtoText = Image("images/howtotext.png", game)
howtoText.visible = False
howtoText.resizeTo(game.width, game.height)


#end screen image
gameover = Image ("images/gameover.png", game)
gameover.resizeBy(50)
gameover.y = 100

youdied = Image ("images/youdied.png", game)
youdied.resizeBy(40)
youdied.y = 400

gameexit = Image ("images/exit.png", game)
gameexit.resizeBy(-50)
gameexit.y = 600

gameexit2 = Image ("images/exit2.png", game)
gameexit2.resizeBy(-50)
gameexit2.y = 600


youwon = Image ("images/youwon.png", game)
youwon.resizeBy(50)
youwon.y = 100

gameplay = Image ("images/gameplay.png", game)
gameplay.resizeBy(-20)
gameplay.y = 400

#firework = Animation ("images/firework.png", 20, game, 2000/ 5, 1600/4, 3)
#firework.resizeBy(200)

stalactites = []
for i in range(20):
    stalactite = Image("images/stalactites.png", game)
    stalactite.resizeBy(-90)
    stalactites.append(stalactite)
positionObjects(stalactites)

startbk = Image("images/startscreenbk.webp", game)
startbk.resizeTo(game.width, game.height)
game.setBackground(startbk)

while not game.over:
    game.processInput()
    
    startbk.draw()
    title.draw()
    story.draw()
    play.draw()
    howtoplay.draw()
    storyText.draw()
    howtoText.draw()


    if mouse.collidedWith(story, "rectangle"):
        story.setImage(story_on.image)
    else:
        story.setImage(story_off.image)


    if mouse.collidedWith(play, "rectangle"):
        play.setImage(play_on.image)
    else:
        play.setImage(play_off.image)

    if mouse.collidedWith(howtoplay, "rectangle"):
        howtoplay.setImage(howtoplay_on.image)
    else:
        howtoplay.setImage(howtoplay_off.image)


    if mouse.collidedWith(story,"rectangle") and mouse.LeftClick:
        storyText.visible = True

    if mouse.collidedWith(howtoplay,"rectangle") and mouse.LeftClick:
        howtoText.visible = True

    if keys.Pressed[K_SPACE]:
        storyText.visible = False
        howtoText.visible = False


    if mouse.collidedWith(play, "rectangle") and mouse.LeftClick:
       game.over = True

    game.update(30)
game.over = False
    

#level 1 
while not game.over:
  game.processInput()
  bk.draw()

  crystal1.draw()
  crystal2.draw()
  crystal3.draw()
  crystal4.draw()
  platform1.draw()
  platform2.draw()
  platform3.draw()
  platform4.draw()
  platform5.draw()
  platform6.draw()
  platform7.draw()
  platform8.draw()
  

  for i in range(len(stalactites)):
      stalactites[i].move()

  if stalactites[i].y > game.height + 100 and stalactites[i].visible:
        stalactites[i].visible = False

  
  
  game.update(30)
game.over = False

bk2 = Image("images/level2.png", game)
bk2.resizeTo(game.width, game.height)
game.setBackground(bk2)

    
#level 2 
while not game.over:
    game.processInput()
    bk2.draw()

    stone1.draw()
    stone2.draw()
    stone3.draw()
    stone4.draw()
    stone5.draw()
    stone6.draw()
    stone7.draw()
    waterfall.draw()
    waterfall2.draw()
    
    for i in range(len(stalactites)):
      stalactites[i].move()

    if stalactites[i].y > game.height + 100 and stalactites[i].visible:
        stalactites[i].visible = False
    

    game.drawText("level 2", 10, 5)
    game.update(30)
game.over = False

bk3 = Image("images/level3.png", game)
bk3.resizeTo(game.width, game.height)
game.setBackground(bk3)

#level 3
while not game.over:
    game.processInput()
    bk3.draw()

    lava1.draw()
    lava2.draw()
    #lava3.draw()
    lava4.draw()
    #lava5.draw()
    lava6_2.draw()
    lava6.draw()
    #lava7.draw()
    lava9_2.draw()
    lava9.draw()
    lava10_2.draw()
    lava10.draw()
    lava11_2.draw()
    lava11.draw()

    flame.draw()
    flame2.draw()
    flame3.draw()
    flame4.draw()
    flame5.draw()
    #risinglava.move()
    

    if risinglava.top < lava11.bottom:
        risinglava.setSpeed(0, 360)


    game.update(30)
game.over = False

endbk = Image("images/endscreenbk.webp", game)
endbk.resizeTo(game.width, game.height)
game.setBackground(endbk)

while not game.over:
    game.processInput()
    endbk.draw()
    youwon.draw()
    gameplay.draw()
    gameexit2.draw()
    #firework.draw()

    
    if keys.Pressed[K_SPACE]:
        game.over = True 
    


    game.update(30)
game.over = False


endbk2 = Image("images/endscreenbk2.png", game)
endbk2.resizeTo(game.width, game.height)
game.setBackground(endbk2)


while not game.over:
    game.processInput()
    endbk2.draw()
    gameover.draw()
    youdied.draw()
    gameexit.draw()

    if keys.Pressed[K_SPACE]:
        game.over = True 



    game.update(30)
game.quit()


