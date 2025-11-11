fn = ["faculty.json","subject.json"]
import json as j

def arrangeFac(data:dict):
    temp = {}
    for key,value in zip(range(1,len(data)+1),data.values()):
        temp[str(key)] = value
    return temp

def arrangeSub(data:dict):
    temp1 = {}
    for key1,value1 in data.items():
        temp2 = {}
        for key,value in zip(range(1,len(value1)+1),value1.values()):
            temp2[str(key)] = value
        temp1[key1] = temp2
    return temp1

def loadData(filename):
    with open(f"Data/{filename}") as f:
        data = j.load(f)
    return data

def dumpData(data,filename):
    with open(f"Data/{filename}","w") as f:
        j.dump(data,f)

def addFaculty():
    data = loadData(fn[0])
    id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    data[id] = {"Id":id,"Name":name}
    data = arrangeFac(data)
    dumpData(data,fn[0])

def removeFaculty():
    data = dict(loadData(fn[0]))
    for key,value in data.items():
        print(f"{key}:- Id: {value["Id"]},Name: {value["Name"]}")
    no = int(input("Enter No.: "))
    data.pop(str(no))
    data = arrangeFac(data)
    dumpData(data,fn[0])
# fac done

def addSubject():
    data = loadData(fn[1])
    sem = int(input("Enter Sem: "))
    code = input("Enter Code: ")
    name = input("Enter Name: ")
    data[str(sem)][code[-2::]] = {"Code":code,"Name":name}
    data = arrangeSub(data)
    dumpData(data,fn[1])
    # print(data)

def removeSubject():
    data = dict(loadData(fn[1]))
    sem = int(input("Enter Sem: "))
    temp = data[str(sem)]
    for key,value in temp.items():
        print(f"Key:{key}:- Code: {value["Code"]},Name: {value["Name"]}")
    id = int(input("Enter Key: "))
    data[str(sem)].pop(str(id))
    data = arrangeSub(data)
    dumpData(data,fn[1])
    # print(data)



def editData():
    while True:
        print("1:Add Faculty,\n2:Remove Faculty,\n3:Add Subject,\n4:Remove Subject,\n5:Back")
        choise = (input("Enter Operation: "))
        print()
        if choise=="1":
            addFaculty()
        elif choise=="2":
            removeFaculty()
        elif choise=="3":
            addSubject()
        elif choise=="4":
            removeSubject()
        elif choise=="5":
            break
        else:
            print("Enter Valid Operation!\n")
            

# editData()


# with open("Data/faculty.json","r") as f1:
#     FAC = j.load(f1)
# print(arrangeFac(FAC))

# with open("Data/subject.json","r") as f1:
#     SUB = j.load(f1)
# print(arrangeSub(SUB))

# addFaculty()
# removeFaculty()
# addSubject()
# removeSubject()