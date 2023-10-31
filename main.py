from Modules import helper_fuctions
import time

prompt = "Your options are: Show, Add, Edit, Complete, Exit:"
flag = True

while flag:
    time_now = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"It is now:  {time_now}")
    ursInput = input(prompt)
    UrsInput = UrsInput.strip().title()
    match ursInput:
        case "Show":
            currentlst = helper_fuctions.get_current_list()
            filterLst = [item.strip("\n") for item in currentLst]
            for idx, item in enumerate(filterLst):
                print(f"{idx+1}{item}")
            if len(currentlst) <= 0:
                print("None todo list")
        case "Add":
            addtodo = input("Addd this to todo list") + "\n" 
            currentlst = helper_fuctions.get_current_list()
            currentlst.append(addtodo)
            helper_fuctions.write_current_list(currentlst)
        case "Edit":
            currentlst + helper_fuctions.get_current_list()
            editindex =int(input("Edit number:")) -1
            newTodo = input("New todo item: ") + "\n"
            currentlst[editindex] = newTodo
            helper_fuctions.write_current_list(currentlst)
        case "Complete":
            currentlst = helper_fuctions.get_current_list()
            removeTodo = input(" index or Todo name to remove")
            if str.isdigit(removeTodo):
                removeTodo = int(removeTodo) 
                if removeTodo > len(currentlst) or removeTodo < 1:
                    print("Index must be 1 to", len(currentlst)) 
                else:
                    removeTodo = removeTodo -1
                    print("Removed:", currentlst.pop(removeTodo))
            else:
                currentlst.remove(removeTodo)
            helper_fuctions.write_current_list(currentlst)
        case "Exit":
            flag = False    
            