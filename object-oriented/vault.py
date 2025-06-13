class Vault:
    def __init__(self, name, galleons=0, sickles=0, knuts=0):
       self.name = name
       self.galleons = galleons
       self.sickles = sickles
       self.knuts = knuts
       
    

    def __str__(self):
       return f"{self.name} has {self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts."
   
    def __add__(self, other):
       total_galleons = self.galleons + other.galleons
       total_sickles = self.sickles + other.sickles
       total_knuts = self.knuts + other.knuts
       return Vault(total_galleons, total_sickles, total_knuts)
       
def main():
    while True:
        choice = input("Do you want to create a vault? (yes/no): ").strip().lower()
        if choice == 'no':
            break
        elif choice != 'yes':
            print("Please enter 'yes' or 'no'.")
            continue
        name = input("Enter vault name: ")
        galleons = int(input("Enter number of galleons: "))
        sickles = int(input("Enter number of sickles: "))
        knuts = int(input("Enter number of knuts: "))
        vault = Vault(name, galleons, sickles, knuts)
        print(f"Vault created: {vault}")
      

potter = Vault("potter",10, 5, 3)
print(potter)  

weasley = Vault("weasley", 7, 2, 8)
print(weasley)

total = potter + weasley
print(total)



if __name__ == "__main__":
    main()
    print("Thank you for using the vault system!")
    print("Goodbye!")