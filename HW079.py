def normal_name(list_name):
    
    new_name = []
    for name in list_name:
        new_name.append(name.title())
        new_name_map = map(normal_name, list_name)
    return(new_name)