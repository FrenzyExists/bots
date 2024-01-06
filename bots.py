import pyautogui as auto
import time
import keyboard as kewb
import win32api
import win32con
import os

def click(x: int, y: int):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def pianoTileReflex():
    # https://lagged.com/en/g/piano-tiles
    gray = (74,  74,  86)

    while not kewb.is_pressed('q'):
        x, y = 1274, 470  # starting point
        for i in range(0, 4):
            for j in range(0, 4):
                if auto.pixel(x+i*100, y+j*100) == gray:
                    click(x+i*100, y+j*100)


def pianoTileTap():
    # https://lagged.com/en/g/magic-tiles
    black = (0, 0, 0)
    while not kewb.is_pressed('q'):
        x, y = (1240, 520)
        for i in range(0, 4):
            if auto.pixel(x+i*100+40, y) == black:
                click(x+i*100+40, y)


def rolling():
    # https://lagged.com/en/g/rolling
    red = (255, 0, 77)
    st = time.time()  # start time
    multiplier = 1
    while not kewb.is_pressed('q'):
        if auto.pixel(1400, 540) == red:
            if auto.pixel(1280, 416) == red or auto.pixel(1280, 768) == red:
                time.sleep(0.019*multiplier)
            click(1400, 540)
            time.sleep(abs(0.019+0.09*multiplier))
        et = time.time()
        # print(et - st)
        print(abs(0.019+0.09*multiplier))
        if et - st >= 19:
            multiplier = abs(multiplier - 0.056)
            st = time.time()


def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)


def stickmanTest():
    # force use of ImageNotFoundException
    auto.useImageNotFoundException()

    # img = auto.screenshot(region=(1540, 134, 320, 500))
    # img.save(imPath("test.png"))

    print("File exists?: ", os.path.exists(imPath("stickman.png")))
    while 1:
        time.sleep(0.7)
        try:
            # auto.locateOnScreen(imPath("stickman.png"), grayscale=True, confidence=0.6)
            auto.locateOnScreen(imPath("stickman.png"), region=(
                1540, 134, 320, 500), grayscale=True, confidence=0.6)
            print('image found')
        except auto.ImageNotFoundException:
            print('image not found')


print("""
Before running the script change the coordinates for things
to detect so it matches with your screen
1. Piano Reflex game: https://lagged.com/en/g/piano-tiles
2. Piano Tile Tap game: https://lagged.com/en/g/magic-tiles
3. Rolling game: https://lagged.com/en/g/rolling
      """)
a = input("choose which bot to try Ej. 3: ")
if int(a) == 1:
    time.sleep(2)
    pianoTileReflex()
elif int(a) == 2:
    time.sleep(2)
    pianoTileTap()
elif int(a) == 3:
    time.sleep(2)
    rolling()
else:
    print("Try again")
