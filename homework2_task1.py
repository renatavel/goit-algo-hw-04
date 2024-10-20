from pathlib import Path
def total_salary(file_path):
    total=0
    average=0
    num=0
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            for line in file:
                objects=line.split(",")  
                try:
                    total+=int(objects[1])
                    num+=1
                except (ValueError, IndexError):
                     pass 
        if num==0:
            print("File doesn't have the correct data.")  
            return None, None   
        average=int(total/num)
        return total,average
    except (FileNotFoundError, PermissionError):
        print("File isn't acceptable.")
        return None, None

file_path=Path("C:\Projects\Project 1\employees_salary.txt")    
total,average=total_salary(file_path)  
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  