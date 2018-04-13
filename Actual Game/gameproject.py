
#Lucious Droplet Inc.
#Amnesia
#JC,FL,YF
#A virus navagating through a maze to infect Peter to win the game. You use the >^<v keys to move your character.

#game object
from gamelib import*
game = Game(800,600,"Amnesia")

lose = Image("trump.jpg",game)
lose.resizeTo(800,600)
'''
bkmusic = Sound(".wpl",1)


lose2 = Image("lose.jpg",game)
'''
play = Image("play.png",game)

howto = Image("howto.png",game)

win = Image("win.jpg",game)
win.resizeTo(800,600)

bk = Image("sos.gif",game)
bk.resizeTo(800,600)

bk2= Image("bk2.jpg",game)
bk2.resizeTo(800,600)
instruction = Image("instruction.png",game)

bk3 = Image("bk.jpg",game)
bk3.resizeTo(800,600)
peter = Image("peter.jpg",game)
peter.resizeBy(-80)

virus= Image("virus.png",game)
virus.resizeBy(-96)

cell = Image("whitecell.png",game)
cell.resizeBy(-96)
#Start Screen
instruction.moveTo(210,500)
howto.moveTo(200,400)

while not game.over:
    game.processInput()
    '''
    bkmusic.play()
    '''

    bk3.draw()
    howto.draw()
    instruction.draw()
    play.draw()
    if play.collidedWith(mouse) and mouse.LeftButton:
        game.over=True
    game.update(30)
game.over=False
#lEVEL 1
peter.moveTo(750,300)
virus.moveTo(170,560)
cell.moveTo(0,500)

while not game.over:
    game.processInput()

    bk2.draw()
    bk.draw()
    peter.draw()
    virus.draw()
    cell.draw()

    cell.moveTowards(virus,3)
    
    if keys.Pressed[K_ESCAPE]:
        game.quit()

    if keys.Pressed[K_UP]:
        virus.y -=5
    if keys.Pressed[K_DOWN]:
        virus.y +=5
    if keys.Pressed[K_RIGHT]:
        virus.x +=5
    if keys.Pressed[K_LEFT]:
        virus.x -=5

    if virus.collidedWith(peter):
        win.draw()
        game.over=True

    if cell.collidedWith(virus):
        lose.draw()
        game.over=True
    game.update(30)

