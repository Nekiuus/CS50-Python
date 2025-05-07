
name= input("Enter your name: ")

match name:
   case "Harry" | "Hermione" | "Ron":
      print("Griffindor")
   case "Draco":
      print("Slytherin")
   case _:
      print("Unknown house")

