def get_favorites(contacts):
    new_contacts = filter(lambda x: x['favorite'] == True,contacts)
    return list(new_contacts)