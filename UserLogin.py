users = {'Andy': '123456',
         'Bob': '654321',
         'Hely': '0000000'}  # Sample User and user dict store the user name and password
# In Case The password is wrong, there are 3 more times to rentry the PW, otherwise the account will be locked
ChanceForRentryPW = 3
while True:
    print('&'*50)
    print('Welcome To The System, Please Sign In To Continue!')
    print('&'*50)
    name = input('The User Name: ')
    if name in users:
        while ChanceForRentryPW >= 0:  # Check if the user are allow to keep renter the PW
            PW = input('Enter your Password: ')
            if users[name] == PW:
                print("Sign in Sucess!")
                break
            else:
                print(
                    'The Password does not match with the account, Please rentry, You have %d more chance' % ChanceForRentryPW)
                ChanceForRentryPW -= 1  # ,minus the re-try chance
        else:
            print(
                "Your account is been locked, Please contact customer services to unlock it")
        break
    else:
        NewUser_flag = input(
            'The user name does not exist, do you want to sign up ? Y/N?:')
        if NewUser_flag == 'Y':
            while True:
                name = input('Please Set Your User Name:')
                if name in users:
                    print(
                        "This user name is already existed! Please Use Other User Name")
                else:
                    password_for_NewUser = input('Please Set your Password:')
                    renter_new_password = input('Please renter your password:')
                    if password_for_NewUser == renter_new_password:
                        users[name] = password_for_NewUser
                        print(
                            'The account has been cerated! please re-start the program and log in your account if you still can not sign in!')
                        break
                    else:
                        print('Those two password does not match!')
        else:
            print("Goodbey!~")
            break
