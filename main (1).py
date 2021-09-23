import curses
from random import randint
#setup fenetre

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#serpent/bouffe

snake = [(4, 10), (4, 9), (4, 8)]
bouffe = (10, 20)

win.addch(bouffe[0], bouffe[1], '@')

#code jeu

score=0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
  win.addstr(0, 2, 'Score ' + str(score) + ' ')
  win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) #vitesse par rapport longeur

  prev_key = key
  event=win.getch()
  key = event if event != -1 else prev_key   

  if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
    key = prev_key

  #nouv coordo serpent

  y = snake[0][0]
  x = snake[0][1]
  if key == curses.KEY_DOWN:
    y += 1
  if key == curses.KEY_UP:
    y -= 1
  if key == curses.KEY_LEFT:
    x -= 1
  if key == curses.KEY_RIGHT:
    x += 1
  
  snake.insert(0, (y, x))

  #si bord touché

  if y == 0: break
  if y == 19: break
  if x == 0: break
  if x == 59: break

  #si serpent se mord la queue

  if snake[0] in snake[1:]: break

  #si serpent mange

  if snake[0] == bouffe:
    score += 1
    bouffe = ()
    while bouffe == ():
      bouffe = (randint(1,18), randint(1, 58))
      if bouffe in snake:
        bouffe = ()
    win.addch(bouffe[0], bouffe[1], '@')
  else:
    last = snake.pop()
    win.addch(last[0], last[1], ' ')
  
  win.addch(snake[0][0], snake[0][1], '*')
    
    

curses.endwin()
print("Score Final : ",score)
print("Jeu fait par Yuri BAUSCH")