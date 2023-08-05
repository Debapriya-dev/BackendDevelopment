 import json

from employee import details, employee_name, age, title  

 employee_dict= {        

"first_name": str(name),        

"age": int(age),        

"title": str(title)    }   

 return employee_dict  


  with open(output_file, "w") as file: 

  file_write=file.write(json_obj)       

 return file_write  


 details()  

  employee_dict = create_dict(employee_name, age, title)    print("employee_dict: " + str(employee_dict))  

 json_object = json.dumps(employee_dict)    print("json_object: " + str(json_object))  

 write_json_to_file(json_object, "employee.json")  

