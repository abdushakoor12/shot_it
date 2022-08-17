import os
from io import BytesIO
import win32clipboard
from PIL import Image


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


os.system('cmd /c "adb exec-out screencap -p > \"temp_screenshot.png\""')
filepath = 'temp_screenshot.png'
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

os.remove("temp_screenshot.png")

send_to_clipboard(win32clipboard.CF_DIB, data)