from vpython import *

t = 0
dt = 0.001

#final patch
XForece = int(input("Enter the Force of Axis X: "))
YForece = int(input("Enter the Force of Axis Y: "))

backGround = box()
backGround.size = vec(100, 100, 1)

rigid = box()
rigid.size = vec(5, 5, 5)
rigid.pos = vec(-50, -50, 3)
rigid.color = vec(1, 0, 0)

#changed code
rigid.velX = vec(XForece, 0, 0)
rigid.velY = vec(0, YForece, 0)

attach_arrow(rigid, "velX", shaftwidth = 1, color = color.green)
attach_arrow(rigid, "velY", shaftwidth = 1, color = color.blue)
movingArrow = arrow(pos = rigid.pos, axis = rigid.velX + rigid.velY, shaftwidth = 1, color=color.yellow)

while True:
    rate(1 / dt)
    rigid.pos += rigid.velX * dt + rigid.velY * dt
    movingArrow.pos = rigid.pos

    t += dt