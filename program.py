print('Enter "L" for login and "C" to close app')
closeApp =input('Login or close app: ')



if(closeApp == 'L'):
    username=input('Enter your username: ')
    password = input('enter your password: ')
    with open('staff.txt') as file:




        contents = file.read()
        
        if (username and password) in contents:
            print ('Login successful')
            ques = input(print('Do you want to create new account orcheck details or logout'))
        else:
            print ('Error! please try again')
        

    



    

