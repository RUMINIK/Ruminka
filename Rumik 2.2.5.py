class MyClass:
    def __init__(self, prop1=0, prop2=0):
        self.prop1 = prop1
        self.prop2 = prop2

    def __del__(self):
        print(f"Объект с prop1={self.prop1} и prop2={self.prop2} удален.")

obj1 = MyClass(5, 10)
print(f"obj1: prop1={obj1.prop1}, prop2={obj1.prop2}")
obj2 = MyClass()
print(f"obj2: prop1={obj2.prop1}, prop2={obj2.prop2}")

del obj1
del obj2