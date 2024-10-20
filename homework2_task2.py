from pathlib import Path
def get_cats_info(file_path):
    cats_info_list=[]
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            for line in file:
                objects=line.split(",") 
                if len(objects)<3:
                    raise IndexError("Not enough values.")
                try:
                    cats_vocabulary={
                        'id':objects[0], 
                        'name':objects[1],
                        'age':int(objects[2])}
                    cats_info_list.append(cats_vocabulary)
                except (ValueError,IndexError):
                    print("File doesn't have the correct data.")  
                    continue 
        return cats_info_list
    except (FileNotFoundError, PermissionError):
        print("File isn't acceptable.")
        return []

file_path=Path("C:\Projects\Project 1\cat_info.txt")  
cats_info = get_cats_info(file_path)
print(cats_info)    