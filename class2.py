class God():
    def __init__(self,name,age,country,height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"저의 이름은{self.name}이고,국적은{self.country}이며,나이는{self.age}살,키는{self.height}cm입니다")
a = God("김현우",20,"대한민국",180)
a.introduce()
b = God("사쿠라 신지",18,"일본",170)
b.introduce()
c = God("루카스",10,"미국",130)
c.introduce()
d = God("김정은",50,"조선민주주의인민공화국",170)
d.introduce()
e = God("시진핑",60,"중국",170)
e.introduce()