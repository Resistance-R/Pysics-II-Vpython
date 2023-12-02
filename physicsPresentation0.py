from vpython import *

t = 0
dt = 0.001

#define background
backGround = box()
backGround.size = vec(100, 100, 1)

#define rigid
rigid = box()
rigid.size = vec(5, 5, 5)
rigid.pos = vec(-50, -50, 3)
rigid.color = vec(1, 0, 0)

#define rigid forces
rigid.velX = vec(10, 0, 0)
rigid.velY = vec(0, 10, 0)

#applicating pysics
while True:
    rate(1 / dt)
    rigid.pos += rigid.velX * dt + rigid.velY * dt

    t += dt