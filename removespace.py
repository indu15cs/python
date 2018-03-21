while true:
       print("enter  'x' for exit")
       string=input("enter any string")
       if string=='x':
               break
       else:
            new_string=string.replace("","")
            print("removing all spaces")
            print(new_string)
