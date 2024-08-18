class Code:
    def __init__(self,name="codetree",code='50'):
        self.name = name
        self.code = code
    
    def print(self):
        print(f'product {self.code} is {self.name}')

c1 =Code()
name, code =input().split()

c2 = Code(name,code)

c1.print()
c2.print()