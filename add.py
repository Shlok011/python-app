class parent:
    def display(self):
        print("i m a parent")
class child(parent):
    def display(self):
        super().display()
        print("i m a child")
obj=child()
obj.display()
