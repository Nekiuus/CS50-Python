#Enumerate
'''
sheep=["Erik","Miguel","Sergio"]

for i, sheep in enumerate(sheep):
    print(f"Sheep {i+1}: {sheep}") 
'''

def main():
    n=int(input("Enter the number of sheep: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * (i + 1))
    return flock
    #for i in range(1, n + 1):
        #yield f"🐑" * i

if __name__ == "__main__":
    main()