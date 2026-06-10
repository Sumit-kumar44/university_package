from university.student import Student

#import test

def main():
    print('main func of main.py is called')
    print('name of the script:',__name__)
    #print('this is the main func where i will implement some logic')
    
    #example student
    students=[]
    students.append(Student("jalal", 1001))
    students.append(Student("kamal", 1002))

    for s in students:
        print(s)


if __name__ == "__main__":    

    main()    