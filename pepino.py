from pickle import dump, dumps, load, loads
 
obj = [10,(10,11),None, True, False, 'Hola, mundo!']
pickled_obj = dumps(obj)
print(pickled_obj)
unpickled_obj = loads(pickled_obj)
print(unpickled_obj)

# with open("pickled_obj.pickle", "wb") as f:
#     dump(obj, f)
# with open("pickled_obj.pickle", "rb") as f:
#     unpickled_obj = load(f)
# # Verificar que sean iguales.
# print(unpickled_obj == obj)  # True

import json

data_j=json.dumps([[1,2],obj])#, indent=2)

print(data_j)
with open("data.json", "w") as f:
   json.dump(data_j, f)


with open("data.json") as f:
    data = json.load(f)
# Imprime [True, False, None, 'Hola, mundo!'].
print(data)