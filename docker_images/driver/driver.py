def main():
    display_menu()
    choice = ''
    while(choice != 'q'):
        choice = input("Please enter a number or 'q': ")
        match int(choice):
            case 1:
                print("running hadoop")
            case 2:
                print('running spark')
            case 3:
                print('running hadoop')
            case 4:
                print("sonar qube")
    
def display_menu(): 
    print("Welcome to Big Data Processing Application")
    print("Please enter a number to run an application:")
    print("1) Apache Hadoop")
    print("2) Apache Spark")
    print("3) Jupyter Notebook")
    print("4) SonarQube and SonarScanner")
    
if __name__ == "__main__":
    main()