from datetime import datetime


class Hello:
    hi = 'Hey there! This is the Hello base class :)'
    time = datetime.utcnow()

    def __init__(self, text):
        self.message = text

    def sayHi(self):
        print(Hello.hi)

    def getText(self):
        print(f'Content of the class: {self.message}')

    def showTime(self, name):
        print(f'Hey there {name} | Today is: {Hello.time}')

    @staticmethod
    def showText(object):
        print(f'{str(object)}')
