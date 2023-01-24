import pyautogui as pg
import time

time.sleep(2)
# print(pg.position())

pg.leftClick(1105,1039,1,3)
time.sleep(1)
pg.typewrite("https://web.telegram.org/k/#@IOTHIBOT")
time.sleep(1)
pg.press("enter")
time.sleep(1)
pg.leftClick(182,376,1,3)
time.sleep(1)

for i in range(10):
    pg.typewrite("Terima Kasih")
    pg.press("enter")
    time.sleep(1)

print("DONE!")