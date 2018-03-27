print("Enter 'x' for exit");
string=input("enter any string to cout the number of words");
if string=='x':
    exit();
else:
    word_length=len(string.split());
    print("number of words=",word_length);
