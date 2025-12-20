def hello_world(i):
    print("hellow world")
    if i == 5:        
        return
    hello_world(i+1)
        

hello_world(1)