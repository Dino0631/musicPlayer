import os
# add_library('sound')


cwd = os.getcwd()
music_path = 'music'
fps = 60 #fps the game runs at

#time before mouse down is a hold
#if released before self time is up, it counts as a click
mouseClickTime = 0.1
keyPressTime = 0.2


#s to detect when pressed
startchar = ' ' #spacebar
endchar = '~' #tilde


#class used to store keystrokes, for up to 1 second
class Key:
    pressed = [] #record 1 second of data per key
    assoc = ''
    time = 0 #in seconds, max 1 second
    holdThreshold = 0
    def __init__(self, assoc='', MorKB=''):    #m for mouse button, k for key
        if MorKB=='m':
            holdThreshold = mouseClickTime
        elif MorKB=='k':
            holdThreshold = keyPressTime
        # key = assoc
        # for ( i=0 i<fps i++) 
        #     pressed.append(False)
           
    def pressedFor(startchar): 
        i=startchar
        while i<fps and pressed[i]:
            a = i-startchar
            i+=1
        return a/fps
    
    def holding():
        return self.pressedFor()>holdThreshold
    
    def clicking(): 
        timePressed = self.pressedFor(1)
        #System.out.prln(timepressed)
        #System.out.prln(timepressed>0)
        return timePressed<=holdThreshold and timePressed>0.0 and not self.pressed[0]
   
    def update(p):
        self.pressed.insert(0, p)
        self.pressed.pop()
   
mouseLeft = Key('mouseLeft', 'm')
mouseRight = Key('mouseRight', 'm')
mouseMiddle = Key('mouseMiddle', 'm')
allKeys = []

defaultcolor = color(255, 255, 255)
def setup():
    size(500, 500)#500(width)x500(height) grid
    frameRate(fps)
    background(defaultcolor)
    
    for k in range(startchar, endchar+1): 
        allKeys[c2i(k)] = Key(str(k), 'k') #+"" to make key
    filenames = os.listdir(os.path.join(cwd, music_path))
    c = color(255, 255, 255)
    print(c)


def playSong():
    a=1

def pauseSong():
    a=1

def shuffleSongs():
    a=1

funcs = {'play' : playSong, 'pause' : pauseSong, 'shuffle' : shuffleSongs}

                        
#class to represent a living Cell
class Button:
    function = ''
    text = ''
    def Button(f='', t=''):
        function = f
        text = t

    def checkUsed():
        if mouseLeft.clicking():
            return True
    def do():
             for k in funcs:
                     if f == k:
                             funcs[k]
                             break
             
#class to contain many Cell objects
class Elements: 
    elements = []
    def Elements(eles = []):
        elements = eles
     
    def checkUsed():
        for e in elements:
            if e.checkUsed():
                e.do()
    def clear():
        for j in range(0, w): 
            for i in range(0, w):
                grid[i][j].disInfect()
               
    def display():
        loadPixels()
        for j in range(0, h):
            for i in range(0, w):
                pixelGrid[i][j] = allStates[grid[i][j].value].c
                pixels[coordTo1d(i, j)] = pixelGrid[i][j]
            
#instance of culture, used in game
culture = Culture(wWidth, wHeight)


#convert 2d coordinates to 1d system pixels[] array
def coordTo1d(x, y): 
    return y*width+x #y rows down + x columns in

#converts ascii    TO a usable Index
def c2i(c):
    return c-32

#converts ascii TO a Key in allKeys
def c2k(c):
    return allKeys[c2i(c)]

def updateMouseKbState():
    if mousePressed:
        mouseLeft.update(mouseButton==LEFT)
        mouseRight.update(mouseButton==RIGHT)
    else: 
        mouseLeft.update(False)
        mouseRight.update(False)
    
    for c in range(startchar, endchar+1): 
        allKeys[c2i(c)].update(c2k(c).pressed[0]) #continue whether it was last detected as pressed or released
    

def spamState(c):
    b=""
    t = 0
    for i in range(fps-1, 0-1, -1): 
        x = (c2k(c).pressed[i])
        b+=x
        t+=x
    
    pr("clicking: ", b, t, mouseLeft.clicking(), "\n")

def inBounds( n,    type):    #type is 'x' or 'y' depending on if it is an x or y coord
    isIn = False
    if type=='x':
        isIn = n>=0 and n<wWidth
    elif type=='y':
        isIn = n>=0 and n<wHeight
    return isIn

def draw():
    rgb = []
    rgb.append(color(255, 0, 0))
    rgb.append(color(0, 255, 0))
    rgb.append(color(0, 0, 255))
    if mouseLeft.clicking():
        if inBounds(mouseX, 'x') and inBounds(mouseY, 'y'):
            if not culture.grid[mouseX][mouseY].isInfected(): 
                culture.grid[mouseX][mouseY].infect()
            
        
    

    #spamState('e')
    #press 'e' to infect cells adjacent to current infected cells
    #spamState('r')
    #press 'r' to 'r'eset the culture of cells


    #if(mouseLeft.clicking())
    #     saveFrame("C:\\Users\\Dino\\Documents\\Processing\\spread\\frames\\frame###.png") 
    #     background(0)
    #

    #TEST DEBUG COMMENTS


    #Cell bob = new Cell()
    #pr(bob.value)
    #pr('\n')

    #pr(mouseX, mouseY)
    #pr('\n')
    #pr("Value:")
    #pr(culture.grid[mouseX][mouseY].value)
    #pr('\n')


    #pr(a*60, '\n')
    #if(mouseLeft.clicking())
    #    background(0) 
    #elif(mouseLeft.holding())
    #    background(255)
    #


    #if (mouseLeft.holding()) 
    #    background(allStates[1].c)
    #else:
    #    background(allStates[0].c)
    #


    #loadPixels()
    #for( i=0i<width*heighti++)
    #    pixels[i] = rgb[i%3]
    #
    #updatePixels()


    #double a = mouseLeft.pressedFor()




def keyPressed():
    #pr(" pressed ", key, "")
    i = c2i(key)
    if i>=startchar and i<=endchar:
        allKeys[i].update(True)
    
    #the key(stored in key) is currently pressed


def keyReleased():
    #pr(" released ", key, "")
    i = c2i(key)
    if i>=startchar and i<=endchar: 
        allKeys[i].update(False)
    
    #the key(stored in key) is currently pressed
