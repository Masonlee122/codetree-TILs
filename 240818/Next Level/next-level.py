class Character :
    def __init__(self):
        self.id = "codetree"
        self.lv =10    


c1 = Character()

id_, lv_ = input().split()

c2 = Character()
c2.id = id_
c2.lv = lv_

print(f"user {c1.id} lv {c1.lv}")
print(f"user {c2.id} lv {c2.lv}")