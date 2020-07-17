import pymem
import pymem.process
import win32api, win32gui
import time
import sys

try:
    pm = pymem.Pymem("hl.exe")
except:
    error001()
else:
    hwDll = pymem.process.module_from_name(pm.process_handle, "hw.dll").lpBaseOfDll
    clientDll = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    hwnd = win32gui.FindWindow( None, 'Counter-Strike')
    if hwnd == 0:
        print("ERROR[001] Game Not Found.")
        time.sleep(5)
        sys.exit(0)

while True:
    activeWindow = win32gui.GetForegroundWindow()
    if activeWindow == hwnd:
        hp = pm.read_int(hwDll + 0x108AA8C)
        idGame = pm.read_int(hwDll + 0x135484)
        idChat = pm.read_int(hwDll + 0x643F1C)
        idLive = pm.read_int(clientDll + 0x1000FC)
        idJump = pm.read_int(hwDll + 0x122DF54)

        if win32api.GetAsyncKeyState(0x20):
            if idGame == 0 and idChat == 0 and idLive != 0:
                if idJump == 1:
                    pm.write_int(clientDll + 0x131424, 5)
                    time.sleep(0.010)
                    pm.write_int(clientDll + 0x131424, 4)
    else:
        time.sleep(1)