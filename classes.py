class Card:
    def __init__(self,title,content):
        self.content=content
        self.title=title

    def passer(self):
        return f"\n{self.title}\n{self.content}\n"
    
class Prof:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone

    def passer(self):
        return f"\n{self.name}\n{self.age}\n{self.phone}\n"
