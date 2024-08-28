class goa:
    name=""
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoying the beach")

ragu=goa()
kumar=goa()

ragu.name="ragu"
print(ragu.name)
ragu.party()

class laptop:
    def __init__(self):
        self.price=0
    def display(self):
        print("display ",self.price)

hp=laptop()

hp.display()