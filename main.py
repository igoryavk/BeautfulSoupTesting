from bs4 import BeautifulSoup
from colorama import Fore
from os import makedirs
from os.path import exists
from os import rmdir
from shutil import rmtree
import bs4

def parsing_project():
    with open("C://Python//Objects//Device.xml",encoding="utf-8",mode="r") as openxml:
        content=openxml.read()
    bs=BeautifulSoup(content,"lxml")
    root=bs.project

    root_children=[e.name for e in root.children if e.name is not None]
    print("Main structures")
    print(root_children)

def parsing_types():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as openxml:
        content=openxml.read()
    bs=BeautifulSoup(content,"lxml")
    types=bs.types

    types_children=[child.name for child in types.children if child.name is not None]

    print("Here are the main structure of types")
    print(types_children)

def parsing_datatype():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as openxml:
        content=openxml.read()
    bs=BeautifulSoup(content,"lxml")
    datatypes=bs.types.datatypes
    datatypes_children=[child for child in datatypes]
    for datatype in datatypes_children:
        print("---Begin---")
        print(datatype)
        print("---End---")
    print("Here are datatypes")

def parsing_pous():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as plcxml:
        content=plcxml.read()
    bs=BeautifulSoup(content,"lxml")
    print(bs)
    root=bs.types.pous
    pous=[child for child in root.children if child.name is not None]

    for pou in pous:
        print("Имя:"+str(pou.get("name"))+"     Тип:"+str(pou.get("poutype")))
    outbs=BeautifulSoup()
    outbs.append(root)
    with open("C://json//output.txt",mode="w",encoding="utf-8") as out:
        out.write(outbs.prettify())
        out.close()

def saving_pous_into_text():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as plcxml:
        content=plcxml.read()
    bs=BeautifulSoup(content,"lxml")
    pous=[child for child in bs.types.pous if child.name is not None]
    #print(type(pous))
    for pou in pous:
         #print(type(pou))
         interface=pou.interface
         name=pou.get("name")
         with open(f"C://json//interfaces//{name}",encoding="utf-8",mode="a") as out:
             sections=[section for section in interface.children if section.name is not None]
             for section in sections:
                 print(section.name)
                 vars=[var for var in section.children if var.name is not None]
                 for var in vars:
                     print(var)
             #    out.write(str(var))
             # out.close()

def parsing_interface():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as plsxml:
        content=plsxml.read()
    bs=BeautifulSoup(content,"lxml")
    pous=[pou for pou in bs.types.pous if pou.name is not None]
    path="D://POUs/interfaces//"
    if (exists(path)):
        rmtree(path)
    makedirs(f"{path}")
    for pou in pous:
        dir_name=pou.get("name")
        makedirs(f"{path}{dir_name}")

        interface=pou.interface
        sections=[section for section in interface.children if section.name is not None]
        for section in sections:
            #print(section)
            if (not exists(f"{path}{dir_name}//{section.name}")):
                makedirs(f"{path}{dir_name}//{section.name}")

            if type(section.variable)==bs4.element.Tag:
                 var=section.variable

                 filename=f"{path}{dir_name}//{section.name}//{var.get('name')}.txt"
                 with open(filename,encoding="utf-8",mode="a") as file:
                    file.write(str(var))
                    file.close()
def parsing_st():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as plcxml:
        content=plcxml.read()
    bs=BeautifulSoup(content,"lxml")
    pous=[pou for pou in bs.types.pous if pou.name is not None]
    path = "D://POUs/st//"
    if exists(path):
        rmtree(path)
    makedirs(f"{path}")
    for pou in pous:
        with open(f"{path}{pou.get('name')}.txt",encoding="utf-8",mode="a") as file:
            file.write(str(pou.st))
            file.close()

def delete_element_from_tree():
    with open("C://json//myexport.xml",encoding="utf-8",mode="r") as xml:
        content=xml.read()
    bs=BeautifulSoup(content,"lxml")
    out=bs
    for element in  bs.find_all("pou"):
        element.decompose()

    with open("C://json//withoutpou.xml",encoding="utf-8",mode="w") as file:
        file.write(str(out))
        file.close()
def

if __name__ == '__main__':
    #parsing_project()
    #parsing_types()
    #parsing_datatype()
    #parsing_pous()
    #saving_pous_into_text()
    #parsing_interface()
    #parsing_st()
    delete_element_from_tree()