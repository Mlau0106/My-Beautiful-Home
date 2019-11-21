#game file
from gamelib import*

#variables
game = Game(800,600,"Basketball Game")

bk = Image("basketcourt.jpg",game)
bk.resizeTo(800,600)

basketball = Image("basketball.png",game)
basketball.resizeBy(-80)

#essential game loop
while not game.over:
    game.processInput()
    bk.draw()
    basketball.draw()
    basketball.moveTo(mouse.x,mouse.y)
    game.update(120)

game.quit()




