class Bomb:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

    def print(self):
        print(f'code : {self.code}')
        print(f'color : {self.color}')
        print(f'second : {self.second}')


code, color, second = input().split()
a= Bomb(code,color,second)
a.print()