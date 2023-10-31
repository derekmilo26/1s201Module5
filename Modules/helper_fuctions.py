FILEPATH = "todos.txt"
def get_current_list (filepath=FILEPATH):
    with open(filepath, 'r') as todo_file:
        get_currnet_list = todo_file.readlines()
    return get_currnet_list

def write_current_list(todo_list, filepath=FILEPATH):
     with open(filepath,"w") as tododFile:
          tododFile.writelines(todo_list)

if __name__=="__main__":
   print("debugging purpose")
   print(get_current_list("./todos.txt"))
