import webbrowser
import time

n = 3
print "This program will start in", time.ctime()
while n > 0:
    time.sleep(10)
    webbrowser.open("http://ya.ru")
    n -= 1