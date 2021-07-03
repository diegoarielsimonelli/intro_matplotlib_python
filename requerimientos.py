import os
lista = []
lista.append("pip3 install -U pip --user")
lista.append("pip3 install numpy")
lista.append("pip3 install matplotlib")
lista.append("pip3 install SQLAlchemy")
lista.append("pip3 install requests")
lista.append("pip3 install Flask")
lista.append("pip3 install Flask-SQLAlchemy")
lista.append("pip3 install Flask-Login")

for i in range(len(lista)):
    os.system(lista[i])
    print(lista[i])