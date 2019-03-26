from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

angle=1
x=0
forward =True

def road():
    glLoadIdentity()
    glBegin(GL_QUADS)
    glColor3f(.2, .2, .2)
    glVertex(-40, -2.5 * .25, -4)
    glVertex(-40, -2.5 * .25, 4)
    glVertex(10, -2.5 * .25, 4)
    glVertex(10, -2.5 * .25, - 4)
    glEnd()

def park(o):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glColor3f(0, .4, 0)
    glVertex(-80, -2.5 * .25, o*-22)
    glVertex(-80, -2.5 * .25, o*-5.78)
    glVertex(30, -2.5 * .25, o*-5.78)
    glVertex(30, -2.5 * .25, o*- 22)
    glEnd()

def sidewalk(X,o):
    glLoadIdentity()
    glTranslate(X, -2.2 * 0.25, o*-4.3)
    glScale(1, 0.25, .5)
    glutSolidCube(3)

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,.1,100)
    gluLookAt(8,9,10 ,0,0,0 ,0,1,0)

def wheel(X,Y,Z):
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(X,Y,Z)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, .5, 13, 14)

def torch(X,Y,Z):
    glLoadIdentity()
    glColor3f(sin(x*4),sin(x*4),0)
    glTranslate(X,Y,Z)
    glutSolidSphere(0.4,100,100)

def cir(r,xc,yc):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.025 * pi):
        x = xc+r * cos(theta)
        y = yc+r * sin(theta)
        glVertex(x, y)
    glEnd()

def c(X,y,z,l):
    glLoadIdentity()
    glTranslate(X-x, y, z)
    cir(l, 0, 0)

def cloud(o,h,u):
    glLoadIdentity()
    c(-7 + o, 3.2 + h, -20 + u, 1.5)
    c(-7 + o, 2.7 + h, -20 + u, 1.5)
    c(-5.5 + o, 2.7 + h, -20 + u, 1)
    c(-8.5 + o, 2.8 + h, -20 + u, 1)

def Draw():

    glClearColor(.53, .81, .92, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global forward
    glMatrixMode(GL_MODELVIEW)

    road()

    park(1)
    park(-.89)

    glColor3f(1,1,1)
    cloud(+11,+3,8)
    cloud(+5,1,6)
    cloud(-5, 2, 1)
    cloud(-22 ,-2, -8)
    cloud(-38, -2, -10)
    cloud(-65, -6, -18)
    cloud(-90, -6, -24)

    co = 1
    for i in range(-50,20,3):
        co*=-1
        glColor3f(co,co,co)
        sidewalk(i,1)
        sidewalk(i,-1)

    glLoadIdentity()
    glTranslate(-x, 0, 0)
    glColor3f(1,1,1)
    for i in range(-50,25,7):
        glBegin(GL_QUADS)
        glVertex(i, -2.5 * .25, -.1)
        glVertex(i, -2.5 * .25, .6)
        glVertex(i+4, -2.5 * .25, .6)
        glVertex(i+4, -2.5 * .25, - .1)
        glEnd()

    wheel(2.5 + x, -2.5 * 0.25, 2.5 * 0.5)
    wheel(-2.5 + x, -2.5 * 0.25, 2.5 * 0.5)
    wheel(2.5 + x, -2.5 * 0.25, -2.5 * 0.5)
    wheel(-2.5 + x, -2.5 * 0.25, -2.5 * 0.5)

    glLoadIdentity()
    glColor3f(0, .035, .315)
    glTranslate(x,0,0)
    glScale(1,0.25,.5)
    glutSolidCube(5)

    glLoadIdentity() #matrix of model view Of Translation opertaions
    glColor3f(0,0.152,.356)
    glTranslate(0+x,5*.25,0)
    glScale(.5,0.25,0.5)
    glutSolidCube(5)


    torch(2.5+x,0,-1.25)
    torch(2.5+x,0,.5)

    if x>5:
        forward=False
    if x<-13:
        forward=True
    if forward:
        x += 0.04
        angle -= 0.3
    else:
        x-=0.04
        angle +=0.3


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Car")
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
myInit()
glutMainLoop()