import Tkinter # built-in Python graphics library
import random
import math

game_objects = []
delete-group = []

class Circle (object):
    def __init__(self, x, y):
        '''Create a new circle at the given x,y point with a random speed, color, and size.'''

        self.x = x
        self.y = y


        self.x_speed = random.randint(-5,5)
        self.y_speed = random.randint(-5,5)
        self.square = False

        # self.x_speed = x/20 -60
        # self.y_speed = y/20 -60
        # print("Noise")

        while(self.x_speed == 0 and self.y_speed == 0):
            self.x_speed = random.randint(-5,5)
            self.y_speed = random.randint(-5,5)
            # print("Zero found")
        # this creates a random hex string between #000000 and #ffffff
        # we draw it with an outline, so we'll be able to see it on a white background regardless
        self.color = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.size = random.randint(5,75) #size

    def update(self):
        '''Update current location by speed.'''

        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, canvas):
        '''Draw self on the canvas.'''

        canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black")


class Square (Circle):
    def __init__(self, x, y):
        # super().__init__(x, y)
        # Circle.__init__(x,y)
        super(Square, self).__init__(x,y) #< Stealing the circle's init
        self.square = True
        # super(Square, self).__init__(self, x,y)
        # super(self.__class__, self).__init__(x,y)


    def draw(self, canvas): # over writing inheritted draw function of super
        canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size,
                           fill=self.color, outline="black") #drawing a square instead
        # print("Square")


def addCircle(event):
    '''Add a new circle where the user clicked.'''
    # print (str(event.x)+", "+str(event.y))
    global game_objects
    game_objects.append(Circle(event.x, event.y))
    #(math.sqrt((event.x-300)**2 + (event.y-300)**2 )/2)
    # print(event.x event.y)
def addSquare(event):
    global game_objects
    game_objects.append(Square(event.x, event.y))

def reset(event):
    '''Clear all game objects.'''

    global game_objects
    game_objects = []


def draw(canvas):
    '''Clear the canvas, have all game objects update and redraw, then set up the next draw.'''

    canvas.delete(Tkinter.ALL)

    global game_objects
    for game_object in game_objects:
        game_object.update()
        game_object.draw(canvas) # <which still works because overwritten
        if (game_object.square == True):
            for collided in game_objects:
                if #inspace of
                delete-group.append(collided)

    game_objects.remove(collided)


    delay = 33 # milliseconds, so about 30 frames per second
    canvas.after(delay, draw, canvas) # call this draw function with the canvas argument again after the delay



# this is a standard Python thing: definitions go above, and any code that will actually
# run should go into the __main__ section. This way, if someone imports the file because
# they want to use the functions or classes you've defined, it won't start running your game
# automatically
if __name__ == '__main__':

    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=600, height=600)
    canvas.pack()

    # if the user presses a key or the mouse, call our handlers
    root.bind('<Key-r>', reset)
    # root.bind('<Button-1>', addCircle)
    # root.bind('<Button-2>', addSquare)

    root.bind('<Motion>', addCircle)
    root.bind('<Button-1>', addSquare)


    # start the draw loop
    draw(canvas)

    root.mainloop() # keep the window open
