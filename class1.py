class Hello():
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print(self.name,"안녕하세요")
    def goodbye(self):
        print("(저승으로)안녕히가세요")
a = Hello("에바 초호기")
a.greeting()
a.goodbye()
b = Hello("에바 개(씹사기캐)호기")
b.greeting()
b.goodbye()
c = Hello('10사(기캐)도')
c.greeting()
c.goodbye()