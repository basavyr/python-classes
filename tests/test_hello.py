import sys
sys.path.append('../src/')
import hello
import platform

my_text=platform.system()
hl = hello.Hello(my_text)
hl.showTime(my_text)