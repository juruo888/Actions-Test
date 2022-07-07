# Import
import pygame
import os
import sys
import random
import ctypes
import win32api
import win32con
import time
import subprocess
import datetime
import tkinter
import tkinter.messagebox
from PIL import Image, UnidentifiedImageError
from _tkinter import TclError
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "0"

# Constant
IMAGEDIR = "pictures"
SUPPORTEXTS = ["jpeg", "jpg", "png", "bmp"]
SCREENSIZE = (800, 750)
WHITE = (255, 255, 255, 27)
GRAY = (192, 192, 192)
sys_lang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans = (sys_lang == "0x804")
DEBUG = False
RESTART = True
BOMBTIME = "2022.7.7 12:00:00"

# Version
major = 1
minor = 1
releases = 0
build = 9
typenum = 1
x = 1

# Language
if IsZh_Hans:
    Lang_Title = "刮刮乐"
    Lang_Quit = "退出"
    Lang_About = "关于"
    Lang_About_Message = "本程序受 MIT 许可证保护\nCopyright © 2022 Class Tools Develop Team. All rights reserved.\nGithub 存储库：https://github.com/class-tools/ScratchOff\n\n"
    Lang_About_Insider = "Class Tools 机密\n以任何方式进行未经授权的使用或披露可能会招致惩戒处分，最严重的处罚可要求承担可能的民事与刑事责任。\n\n仅用于测试。版本号："
    Lang_About_Public = "仅用于测试。版本号："
    Lang_About_Releases = "版本号："
else:
    Lang_Title = "Scratch Off"
    Lang_Quit = "Quit"
    Lang_About = "About"
    Lang_About_Message = "This program uses MIT License\nCopyright © 2022 Class Tools Develop Team. All rights reserved.\nGithub Repository: https://github.com/class-tools/ScratchOff\n\n"
    Lang_About_Insider = "Class Tools Confidential\nUnauthorized use or disclosure in any way may result in disciplinary action, and the most serious punishment may require possible civil and criminal liability.\n\nOnly for test. Version: "
    Lang_About_Public = "Only for test. Version: "
    Lang_About_Releases = "Version: "

def noPicturesError():
    """No pictures error"""
    quit(1)
    printLog("ERROR", "Cannot read pictures file data.")
    if IsZh_Hans:
        if win32api.MessageBox(
            0,
            "无法读取图片数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            "错误",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    else:
        if win32api.MessageBox(
            0,
            "Cannot read pictures file data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            "Error",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    quit(3)

def noIconError():
    """No icon error"""
    quit(1)
    printLog("ERROR", "Cannot read icon.")
    if IsZh_Hans:
        if win32api.MessageBox(
            0,
            "无法读取图标。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            "错误",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    else:
        if win32api.MessageBox(
            0,
            "Cannot read icon.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            "Error",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    quit(3)

def noFontError():
    """No font error"""
    quit(1)
    printLog("ERROR", "Cannot read font data.")
    if IsZh_Hans:
        if win32api.MessageBox(
            0,
            "无法读取字体数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            "错误",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    else:
        if win32api.MessageBox(
            0,
            "Cannot read font data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            "Error",
                win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    quit(3)

def cannotWriteLogError():
    """Cannot write log error"""
    quit(1)
    if IsZh_Hans:
        if win32api.MessageBox(
            0,
            "无法写入日志。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            "错误",
                win32con.MB_ICONERROR | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    else:
        if win32api.MessageBox(
            0,
            "Cannot write log file.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            "Error",
                win32con.MB_ICONERROR | win32con.MB_YESNO) == 6:
            subprocess.run("start website/issues.url", shell=True)
    quit(4)

def resize(size):
    while True:
        if size[0] < 800 and size[1] < 800:
            size = (size[0] * 1.5, size[1] * 1.5)
        else:
            break
    while True:
        if size[0] > 800 and size[1] > 800:
            size = (size[0] * 0.5, size[1] * 0.5)
        else:
            break
    size = (int(size[0]), int(size[1]))
    return size

def readImageRandomly():
    """Random a image."""
    global SCREENSIZE, ONEIMAGE
    filenames = os.listdir(IMAGEDIR)
    filenames = [f for f in filenames if f.split(".")[-1] in SUPPORTEXTS]
    if len(filenames) == 1:
        ONEIMAGE = True
    else:
        ONEIMAGE = False
    imgpath = os.path.join(IMAGEDIR, random.choice(filenames))
    img = Image.open(imgpath)
    SCREENSIZE = img.size
    SCREENSIZE = resize(SCREENSIZE)
    return [pygame.transform.scale(pygame.image.load(
        imgpath), SCREENSIZE), imgpath[9:], img.size]

def printLog(logType, logContent):
    """Print log"""
    if logType != "DEBUG" or DEBUG:
        try:
            with open("log/latest.log", "a") as file:
                file.write(
                    time.strftime("[%Y.%m.%d %H:%M:%S] [") +
                    str(logType) +
                    "]: " +
                    str(logContent) +
                    "\n")
                print(" [" + logType + "]: " + logContent)
        except FileNotFoundError:
            cannotWriteLogError()

def getTime(log):
    """Get log time"""
    try:
        with open(log, "r") as file:
            firstLine = file.readline()
            time = ""
            for i in firstLine:
                if i == "]":
                    break
                try:
                    time += str(int(i))
                except ValueError:
                    continue
            return time
    except FileNotFoundError:
        return 1145141919810

def watermark():
    font20 = pygame.font.Font("font.ttc", 20)
    font15 = pygame.font.Font("font.ttc", 15)
    if typenum <= 4:
        text1 = font20.render("Class Tools 机密", True, (0, 0, 0))
        text2 = font15.render("以任何方式进行未经授权的使用或披露", True, (0, 0, 0))
        text3 = font15.render("可能会招致惩戒处分，最严重的处罚可", True, (0, 0, 0))
        text4 = font15.render("要求承担可能的民事与刑事责任。", True, (0, 0, 0))
        text5 = font15.render(
            "仅用于测试。版本号：" +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x),
            True,
            (0,
             0,
             0))
        screen.blit(text1, (43, 0))
        screen.blit(text2, (0, 30))
        screen.blit(text3, (0, 45))
        screen.blit(text4, (0, 60))
        screen.blit(text5, (0, 90))
    elif typenum <= 8:
        text = font15.render(
            "仅用于测试。版本号：" +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x),
            True,
            (0,
             0,
             0))
        screen.blit(text, (0, 0))

def Menu_About():
    """About in menu bar"""
    if typenum <= 4:
        tkinter.messagebox.showinfo(
            title=Lang_About,
            message=Lang_About_Message +
            Lang_About_Insider +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x))
    elif typenum <= 8:
        tkinter.messagebox.showinfo(
            title=Lang_About,
            message=Lang_About_Message +
            Lang_About_Public +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x))
    else:
        tkinter.messagebox.showinfo(
            title=Lang_About,
            message=Lang_About_Message +
            Lang_About_Releases +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x))

def Menu_Quit():
    """Quit in menu bar"""
    quit(2)

def init():
    global screen, root
    root = tkinter.Tk()
    root.title(Lang_Title)
    root.geometry(str(SCREENSIZE[0]) +
                  "x" +
                  str(SCREENSIZE[1]) +
                  "+" +
                  str(int(root.winfo_screenwidth() /
                          2 -
                          SCREENSIZE[0] /
                          2)) +
                  "+" +
                  str(int(root.winfo_screenheight() /
                          2 -
                          SCREENSIZE[1] /
                          2)))
    root.resizable(width=False, height=False)
    try:
        root.iconbitmap("SO.ico")
    except TclError:
        noIconError()
    embed = tkinter.Frame(root, width=SCREENSIZE[0], height=SCREENSIZE[1])
    embed.grid(columnspan=(600), rowspan=500)
    embed.pack(side=tkinter.LEFT)
    menubar = tkinter.Menu(root)
    root["menu"] = menubar
    menubar.add_command(label=Lang_About, command=Menu_About)
    menubar.add_command(label=Lang_Quit, command=Menu_Quit)
    os.environ["SDL_WINDOWID"] = str(embed.winfo_id())
    os.environ["SDL_VIDEODRIVER"] = "windib"
    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    screen = pygame.display.set_mode(SCREENSIZE)

def quit(quittype):
    """Quit the program."""
    if quittype == 1:
        pygame.quit()
    elif quittype == 2:
        root.destroy()
    elif quittype == 3:
        printLog("INFO", "Exiting ScratchOff.")
        sys.exit(0)
    elif quittype == 4:
        sys.exit(0)


# Create log
subprocess.run("md log > temp.txt 2> temp2.txt", shell=True)
subprocess.run("del temp.txt", shell=True)
subprocess.run("del temp2.txt", shell=True)
lastTime = getTime("log/latest.log")
if lastTime != 1145141919810:
    subprocess.run("cd log && ren latest.log " + lastTime + ".log", shell=True)
file = open("log/latest.log", "w")
file.close()
printLog("INFO", "Starting ScratchOff.")

# Timebomb
if typenum <= 12:
    if BOMBTIME != "1145141919810":
        now = datetime.datetime.now()
        bomb = datetime.datetime.strptime(BOMBTIME, "%Y.%m.%d %H:%M:%S")
        if now > bomb:
            printLog("INFO", "You use the program after the timeless.")
            quit(3)

# Warn
if typenum <= 4:
    if win32api.MessageBox(
        0,
        "此版本为内部版本，版本号：" +
        str(major) +
        "." +
        str(minor) +
        "." +
        str(releases) +
        "." +
        str(build) +
        "." +
        str(typenum) +
        "." +
        str(x) +
        "。\n以任何方式进行未经授权的使用或披露可能会招致惩戒处分，最严重的处罚可要求承担可能的民事与刑事责任。\n若以认真阅读这段文字，请点击否确认。",
        "警告",
            win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
        printLog("INFO", "You click yes.")
        quit(3)
elif typenum <= 8:
    if win32api.MessageBox(
        0,
        "此版本为测试版本，仅用于测试，版本号：" +
        str(major) +
        "." +
        str(minor) +
        "." +
        str(releases) +
        "." +
        str(build) +
        "." +
        str(typenum) +
        "." +
        str(x) +
        "。\n若以认真阅读这段文字，请点击否确认。",
        "警告",
            win32con.MB_ICONWARNING | win32con.MB_YESNO) == 6:
        printLog("INFO", "You click yes.")
        quit(3)


# Read image
while True:
    try:
        image = readImageRandomly()
    except FileNotFoundError:
        noPicturesError()
    except UnidentifiedImageError as errorMsg:
        subprocess.run(
            "del \"pictures\\" +
            str(errorMsg)[
                38:-
                1] +
            "\"",
            shell=True)
        printLog(
            "WARNING",
            "You have a unsupported picture, its name is: \"" +
            str(errorMsg)[
                38:-
                1] +
            "\". We delete the picture.")
        continue
    else:
        break
printLog("INFO", "Use image " + image[1] + ", image size: " + str(image[2]))
printLog("INFO", "Set screen size to " + str(SCREENSIZE))

# Init

init()
surface = pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)

# Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(1)
            quit(3)
    mouse_event_flags = pygame.mouse.get_pressed()
    if mouse_event_flags[0]:
        RESTART = False
        pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
        printLog("DEBUG", "Left button pressed, position: " +
                 str(pygame.mouse.get_pos()) + ".")
    elif mouse_event_flags[-1]:
        if not RESTART:
            printLog("INFO", "Right button pressed, game restart.")
            old = image
            while True:
                try:
                    image = readImageRandomly()
                except FileNotFoundError:
                    noPicturesError()
                except UnidentifiedImageError as errorMsg:
                    subprocess.run(
                        "del \"pictures\\" +
                        str(errorMsg)[
                            38:-
                            1] +
                        "\"",
                        shell=True)
                    printLog(
                        "WARNING",
                        "You have a unsupported picture, its name is: \"" +
                        str(errorMsg)[
                            38:-
                            1] +
                        "\". We delete the picture.")
                    continue
                if image[1] != old[1]:
                    break
                if ONEIMAGE:
                    printLog("WARNING", "You only have one image.")
                    break
            printLog("INFO", "Use image " +
                     image[1] + ", image size: " + str(image[2]))
            printLog("INFO", "Set screen size to " + str(SCREENSIZE))
            quit(1)
            quit(2)
            init()
            surface = pygame.Surface(SCREENSIZE).convert_alpha()
            surface.fill(GRAY)
            RESTART = True
    screen.blit(image[0], (0, 0))
    screen.blit(surface, (0, 0))
    try:
        watermark()
    except BaseException:
        noFontError()
    pygame.display.update()
    try:
        root.update()
    except TclError:
        quit(1)
        quit(3)
