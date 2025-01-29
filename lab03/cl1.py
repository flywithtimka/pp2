class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

if __name__ == "__main__":
    obj = StringManipulator()
    obj.getString()
    obj.printString()
