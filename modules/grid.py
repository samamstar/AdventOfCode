
class grid:
    def __init__(self):
        self.data = [[None]]

    def width(self):
        return len(self.data[0])

    def height(self):
        return len(self.data)

    def setPoint(self, x, y):
        if self.width() < x:
            self.setWidth(x)

    def setWidth(self, newWidth):
        if newWidth > self.width():
            for row in self.data:
                for i in range(newWidth - self.width()):
                    row.append(None)

        elif newWidth < self.width():
            for row in self.data:
                for i in range(newWidth - self.width()):
                    row.pop(len(row)-1)

    def setHeight(self, newHeight):
        if newHeight > self.height():
            for i in range(newHeight-self.height()):
                self.data.append([None] * self.width())

        elif newHeight < self.height():
            for i in range(self.height() - newHeight):
                self.data.pop(len(self.data)-1)
