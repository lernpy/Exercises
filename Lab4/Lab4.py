options_list = [
    'Choose one option:',
    '1. Create User',
    '2. Show list of Users',
    '3. Delete user from List',
    '4. Authorization',
    '5. Exit',
]

users = []

user = {
        'name': '',
        'surname': '',
        'age': '',
        'address': '',
        'email': '',
        'password': '',
    }


def create_user(user: dict) -> None:
    users.append(user)
    print('User created!')

def get_user_by_name(name: str) -> dict | None:
    for user in users:
        if user.get('name') == name:
            return user
    print('User not found!')

def get_user_by_email(email: str) -> dict | None:
    for user in users:
        if user.get('email') == email:
            return user
    print ("It's ok, your email is unique!")

def delete_user(name: str) -> None:
    user = get_user_by_name(name)
    if user is None:
        return None
    users.remove(user)
    print('User successfully deleted!')

def is_password_valid(password):
    return f'The password shold be longer, than {password}'



while True:
    print(*options_list, sep='\n')
    option = input('Enter a number of option: ')
    if option == '1':
        name = input('Enter a name: ')
        surname = input('Enter a surname: ')
        age = input('Enter an age: ')
        address = input('Enter an address: ')
        email = input('Enter an e-mail: ')
        password = input('Enter a password: ')
        
        user = {
            'name': name,
            'surname': surname, 
            'age': age,
            'address': address,
            'email': email,
            'password': password,
        }
        create_user(user)

    elif option == '2':
        print('List of users:')
        for user in users:
            for key, value in user.items():
                print (f' {key}: {value}')
            print ('')
    
    elif option == '3':
        name = input('Enter a name: ')
        delete_user(name)

    elif option == '4':
        print("Authorization")
        email = input('Enter an email: ')
        get_user_by_email(email)
        password = input('Enter a password: ')
        while len(password)> 8:
            print ('You are successfully authorizated!')
            break
        else:
            print(is_password_valid(password))
            
    elif option == '5':
        print("Good bye!")
        break

    else:
        print("The option is not found!")