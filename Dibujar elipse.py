import pyautogui as pa
import math

d=0.2

pa.hotkey('win', 'r')
pa.write('mspaint.exe', interval=0.2)
pa.press('enter', interval=0.2)
pa.hotkey('win', 'up')

pasos=32
radianes=(math.pi*2)/pasos
paso=0
radioX=200
radioY=100

cx=(pa.size().width/2)
cy=(pa.size().height/2)
pa.moveTo(cx,cy)

while paso<2*math.pi:

    dx=radioX*math.cos(paso)
    dy=radioY*math.sin(paso)

    px=cx-dx
    py=cy-dy

    pa.dragTo(px,py)

    print(cx,cy,px,-py,math.degrees(paso))

    paso=paso+radianes