import json

# library confilcts when this file has name "json.py"

def print_header():
    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed       MTU  ")
    print("-------------------------------------------------- --------------------  ----------  ------")

data_path = "sample.json"

print_header()

with open(data_path) as f:
    data = json.load(f)

for i in data["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"], end='')
    print((50 - len(i["l1PhysIf"]["attributes"]["dn"])) * ' ', end=' ')
    print(i["l1PhysIf"]["attributes"]["descr"], end='')
    print((20 - len(i["l1PhysIf"]["attributes"]["descr"])) * ' ', end='  ')
    print(i["l1PhysIf"]["attributes"]["speed"], end='')
    print((10 - len(i["l1PhysIf"]["attributes"]["speed"])) * ' ', end='  ')
    print(i["l1PhysIf"]["attributes"]["mtu"], end='\n')