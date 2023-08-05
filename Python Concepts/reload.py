import importlib
import filechanges

def changes():
   try:
       importlib.reload(filechanges) 
       filechanges.file_changes()
    except:
        pass
    
for i in range(5):
    changes()
    print("Hit enter to reload...")    