a = 96

def num():
    # a = 10 , local variable
#     print(f"Statement 1 , {a}") , error , a is refrenced before assignment
    global a # making a into global variable
    a = 10
    print(f"Statement 2 , {a}")
   

print(f"Statement 1 , {a}")
num()
print(f"Statement 3 , {a}")