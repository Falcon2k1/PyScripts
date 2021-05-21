#! python3
import pyautogui as pag
import sys
from time import sleep
import secrets.daily_report_secrets

# Important screen coords info:
# Address Bar: X:205 Y:60
# Graph SS range:
# X: 243, Y: 164 to X: 1486, Y: 706
# Outlook new mail button: X:63, Y:86
# TTC Button: 98 / 313
# TTA: 98 / 356
# TTS: 98 / 395
# Core Measurements: 98 / 435
# Monthly Utilization: 98 / 596
# Outlook: 3405/229
# New Message: 3277/283

screenWidth, screenHeight = pag.size()
ssX1 = 243
ssY1 = 170
ssX2 = 1486
ssY2 = 706

ssList = [
    (98, 313, True),
    (98, 356, True),
    (98, 395, True),
    (98, 435, False),
    (98, 596, True)]

pag.PAUSE = 1
pag.FAILSAFE = True


def checkScreenSize():
    if screenWidth != 3440:
        print("Incorrect screen size found, shutting down. This is designed for fullscreen 1440x3440.")
        sys.exit()

def openReportingPage():
    pag.hotkey("winleft","1")
    pag.click(205, 60)
    pag.write("aka.ms/ceosocreporting")
    pag.press('enter')
    pag.hotkey('winleft','left')

def snipArea():
    pag.moveTo(ssX1, ssY1)
    pag.hotkey('shiftleft', 'winleft', 's')
    pag.dragTo(ssX2, ssY2,duration=1)

def init():
    pag.moveTo(3405, 229)
    pag.moveTo(3277, 283)
    pag.click()
    pag.hotkey('winleft', '1')

def paste():
    pag.hotkey('alt', 'tab')
    pag.press('enter')
    pag.hotkey('ctrl', 'v')
    pag.hotkey('alt', 'tab')


checkScreenSize()
init()
#openReportingPage()
#openOutlookMsg()

for x in ssList:
    pag.moveTo(x[0], x[1])
    pag.click()
    sleep(2)
    if x[2] == True:
        snipArea()
        paste()
