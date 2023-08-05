def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: ")
        
    print("Before calling e() : " + animal)
    e()
    print("After nested function: " + animal)


animal = "camel"    
d()
print("Global animal: " + animal)