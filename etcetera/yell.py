def main():
    yell('this','is','success')

def yell(*words):
    uppercased= [word.upper() for word in words]
    
    #uppercased= map(str.upper, words)
    '''
    uppercased=[]
    for word in words:
        uppercased.append(word.upper())
        '''
    print(*uppercased)

if __name__ == "__main__":
    main()
