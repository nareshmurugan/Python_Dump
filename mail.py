import pyautogui as p
import time as t
import subprocess
subprocess.Popen(['C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'])
t.sleep(3)
p.doubleClick(x=664, y=623)
t.sleep(5)
p.click(x=573, y=538)
t.sleep(8)
p.click(x=99, y=258)
t.sleep(15)
p.typewrite("jothikarthi2015@gmail.com")
t.sleep(2)
p.click(x=679, y=448)
p.typewrite("jothikarthi2015@gmail.com")
t.sleep(5)
p.hotkey('ctrlleft','enter')


