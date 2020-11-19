import numpy as np
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT   =10   # pixels
MAZE_H =11  # grid height
MAZE_W =11 # grid width
class Maze(tk.Tk, object):    
    def __init__(self):
        super(Maze, self).__init__()
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
        self._build_maze()
    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1, fill = 'black')
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1,fill = 'black')
        origin = np.array([10, 10])
        oval_center = origin + UNIT * 9
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 9
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 8
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 7
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 6
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 5
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 4
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 3
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + UNIT * 1
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin 
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *4, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, 0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *9, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')

        oval_center = origin + np.array([UNIT *8, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *8, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *7, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *6, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *5, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *2, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *3, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *1])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *0, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *7])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *2])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *3])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *4])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *5])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *6])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *8])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        oval_center = origin + np.array([UNIT *1, UNIT *9])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 0.45, oval_center[1] - 0.45,
            oval_center[0] + 0.45, oval_center[1] + 0.45,
            fill='black')
        
        
        self.canvas.pack()
if __name__ == "__main__":
    env = Maze()
    env.mainloop()
