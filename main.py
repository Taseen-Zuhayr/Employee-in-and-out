class toyfactory:
    def __init__(self):
        print("A new toy is made!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    def __del__(self):
        print("A toy is destroyed!!!!!!!!!!!!!!!!!!!!!!!!!")

def make_toy():
    print("Making toy!!!!!!!!!!!!!!!!!!!!!!!")
    toy = toyfactory()
    print("Toy is ready!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return toy

print("Starting the toy factory!!!!!!!!!!!!!!!!!!!!!!!")
toy = make_toy()
print("Factory is closing!!!!!!!!!!!!!!!!!!!!")