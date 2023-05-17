def create_user(collection):

    """
    A) crear

    """
    username=input("Ingrese nombre: ")
    edad=int(input("edad: "))
    email=input("email: ")
    user=dict(username=username,edad=edad,email=email)
    collection.insert_one(user)

def get_user(collection):
    
    """
    B) Encontrar
    
    """
    username=input("username: ")
    user=collection.find_one(user)
    print(user)
    return
    
def delete_user(collection):
    
    """
    C) Eliminar
    
    """
    username=input("usermane: ") 
    return collection.delete_one({
        "username":username

    })
def update_user(collection):
    pass

def default():
    pass