def get_emails(list_contacts):
    
    new_list_contact = []

    for i in map(get_email, list_contacts):
        new_list_contact.append(i)
    return new_list_contact
        
def get_email(contact):
    return contact['email']

                
get_emails({
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
    "email": "nulla.ante@vestibul.coff.uk",
    "email": "numfglla.ante@vestibul.co.uk",
    "email": "nulla.ante@vestfhgibul.co.uk",
})      

# list_contacts = {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
#     "email": "nulla.ante@vestibul.coff.uk",
#     "email": "numfglla.ante@vestibul.co.uk",
#     "email": "nulla.ante@vestfhgibul.co.uk",
# }