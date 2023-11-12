
def Handler_command_decorator(func):
    def wrapper(command):
        command = command.lower()
        return func(command)
    return wrapper

def input_error(func):
    def wrapper(*args):
        try:
           return func(*args)
        except IndexError:
            print("Enter name and phone number.")
            return
        except ValueError:
            print('ValueError')
            return
        except KeyError:
            print('This subscriber is not available.')
            return
    return wrapper

def add_name_phone_decorator(func):
    def wrapper(*args):
        help_number_message = """
    Номер телефону складається з коду країни(+38) і 10 цифр після неї.
    Номер телефону не може містити літер.
    Номер телефону може містити "+", "-", " ", "(", ")".
    приклади написання номеру:
        +38(050)40-40-400
        +380504040400
        38(050)40-40-400
        380504040400
        38 (050) 40 40 400
        38 050 40 40 400
        (050)-40-40-400
        050-40-40-400
        0504040400
        050-40 40-400
        Спробуйте ще раз...
        """
        args[0][0] = args[0][0].capitalize()
        if args[0][0].isalpha():
            pass
        else:
            print("The name can only consist of letters\nTry again.")
            return
        phone = ' '.join(args[0][1:])
        correct_phone = str(phone)
        correct_phone = correct_phone.replace('(','')
        correct_phone = correct_phone.replace(')','')
        correct_phone = correct_phone.replace('-','')
        correct_phone = correct_phone.replace(' ','')
        correct_phone = correct_phone.replace('*','')
        correct_phone = correct_phone.replace('#','')
        correct_phone = correct_phone.replace('_','')
        if len(correct_phone) == 10:
            correct_phone = '+38' + correct_phone
        if len(correct_phone) == 12:
            correct_phone = '+' + correct_phone
        if len(correct_phone) < 10 or len(correct_phone) > 13:
            print('Не коректно представлений номер')
            print(help_number_message)
            return
        if correct_phone.startswith('+') and correct_phone[1:].isdigit():
            args[0][1] = correct_phone
        else:
            print(f'The number {correct_phone} contains extra characters/letters')
            print(help_number_message)
            return
        return func(*args)
    return wrapper
is_active = True

def hello_human():
    print('How can I help you?')

@input_error
@add_name_phone_decorator
def add_name_phone(*args):
    new_contact = {args[0][0]:args[0][1]}
    print(f'Contact {new_contact} added: ')
    CONTACTS.append(new_contact)

@input_error
@add_name_phone_decorator
def new_phone_number(*args):
    print('Write changed name and phone number:')
    for item in CONTACTS:
        if item[args[0][0]]:
            item[args[0][0]] = args[0][1]
@input_error
def return_phone_number(*args):
    name = args[0][0].capitalize()
    print(name)
    for item in CONTACTS:
        if item[name]:
            print(item[name])

def show_list_phone_number():
    print('List of your phone numbers: ')
    for item in CONTACTS:
        print(item)

def stop_work():
    print('Good Bye!')
    global is_active
    is_active = False

def help_help(*args):
    print(f"{args} ")
    print(len(args[0]))
    if len(args[0]) == 0:
        print(len(args[0]))
    elif len(args[0]) == 1:
        command = args[0][0]
        if command in HELP:
            print(HELP[command])
    elif len(args[0]) > 1:
        command = args[0][0] + ' ' + args[0][1]
        if command in HELP:
            print(HELP[command])
    
        
HELP = {"add": "This comand help you to add a new name and phone to your Phone list.",
        "change": "This comand help you to change a new phone number of exist abonent in your Phone list.",
        "phone": "This comand show you phone number of exist abonent from your Phone list.",
        "show all": "This comand show you all Names and Phone Numbers of exist abonent from your Phone list.",
        "good bye": "This comand help you to exit from this Bot.",
        "close": "This comand help you to exit from this Bot.",
        "exit": "This comand help you to exit from this Bot.",
}

# Функції
OPERATIONS = {
    "help": help_help,
    "hello": hello_human,
    "add": add_name_phone,
    "change": new_phone_number,
    "phone": return_phone_number,
    "show all": show_list_phone_number,
    "good bye": stop_work,
    "close": stop_work,
    "exit": stop_work,
}

CONTACTS = []

#Handler
@Handler_command_decorator
def get_handler(command):
    return OPERATIONS[command]
def start_script(): # Вічний цикл
    while is_active:
        request = input('Enter the comand, please:  ').lower()
        command_parts = request.split()
        if command_parts[0] == 'hello':
            command = command_parts[0]
            handler = get_handler(command)
            handler()
        if command_parts[0] == 'add':
            command = command_parts[0]
            arguments = command_parts[1:]
            handler = get_handler(command)
            handler(arguments)
        
        if command_parts[0] in ['exit','close']:
            command = command_parts[0]
            handler = get_handler(command)
            handler()
        if command_parts[0] == 'good' and command_parts[1] == 'bye':
            command = command_parts[0] + ' ' + command_parts[1]
            handler = get_handler(command)
            handler()
        if command_parts[0] == 'show' and command_parts[1] == 'all':
            command = command_parts[0] + " " + command_parts[1]
            handler = get_handler(command)
            handler()
        if command_parts[0] == 'change':
            command = command_parts[0]
            arguments = command_parts[1:]
            handler = get_handler(command)
            handler(arguments)
        if command_parts[0] == 'phone':
            command = command_parts[0]
            arguments = command_parts[1:]
            handler = get_handler(command)
            handler(arguments)
        if command_parts[0] == 'help':
            command = command_parts[0]
            if len(command_parts) > 1:
                arguments = command_parts[1:]
            else:
                arguments = []
            handler = get_handler(command)
            handler(arguments)
if __name__ == "__main__":
    start_script()