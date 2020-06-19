import sys
sys.path.append('src/')
sys.path.append('../src/')
import platform

import hello

my_text=platform.system()
hl = hello.Hello(my_text)
hl.showTime(my_text)