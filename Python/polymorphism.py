class Document:
    def __init__(self,name):
        self.name=name
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Pdf(Document):
    def show(self):
        return 'Show Worlds.pdf contents!'
class Word(Document):
    def show(self):
        return 'Show Student.doc Contents!'
class Xl(Document):
    def show(self):
        return 'Show Family.xls contents!'
doc=[Pdf('Document1'),Pdf('Document2'),Word('Document3'),Xl('Document4')]

for d in doc:
   print(d.name+':'+d.show())