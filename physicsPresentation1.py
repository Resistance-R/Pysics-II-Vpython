from vpython import *

t = 0
dt = 0.001

backGround = box()
backGround.size = vec(100, 100, 1)

rigid = box()
rigid.size = vec(5, 5, 5)
rigid.pos = vec(-50, -50, 3)
rigid.color = vec(1, 0, 0)

rigid.velX = vec(10, 0, 0)
rigid.velY = vec(0, 10, 0)

#first patch
attach_arrow(rigid, "velX", shaftwidth = 1, color = color.green)
attach_arrow(rigid, "velY", shaftwidth = 1, color = color.blue)
movingArrow = arrow(pos = rigid.pos, axis = rigid.velX + rigid.velY, shaftwidth = 1, color=color.yellow)

while True:
    rate(1 / dt)
    rigid.pos += rigid.velX * dt + rigid.velY * dt
    movingArrow.pos = rigid.pos #added

    t += dt