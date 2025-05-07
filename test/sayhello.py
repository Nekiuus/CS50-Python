def main():
    name=input("Enter a string: ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()