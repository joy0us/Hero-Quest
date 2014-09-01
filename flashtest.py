import pygcurse,pygame,time
win = pygcurse.PygcurseWindow(40,25)

while True:
    win.fill('#', fgcolor='red',bgcolor='black')
    time.sleep(0.05)
    win.fill('#',fgcolor='green',bgcolor='white')
    time.sleep(0.05)
