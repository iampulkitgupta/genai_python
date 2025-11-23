chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"
        print(f"Inside kitchen {chai_type}")
    kitchen()

front_desk()
print(f"Outside {chai_type}")