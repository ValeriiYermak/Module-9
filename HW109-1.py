def get_key_favorite(item: dict()): # я знаю що в мому списку знаходяться словники 
                                   # тому в якості аргументу для функції використовую словник
    print(f"Ітеруємся в об'єкті {item} ")

    if item['favorite']:
        print('---------------------------------------------------------------')
        print(f'item["favorite"] об"єкту {item["name"]} == {item["favorite"]} Добавляємо в new_contacts')
        print('---------------------------------------------------------------')
    return item['favorite'] if item['favorite'] == True else None

def get_favorites(contacts):
    new_contacts = filter(get_key_favorite,contacts)
    
    
    return list(new_contacts)


x = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
     {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False},
     {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True},
     {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False},
     {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]

get_favorites(x)