import sys
sys.path.append('../src/')
import hello

my_text='Darwin'
hl = hello.Hello(my_text)
hl.showTime(my_text)