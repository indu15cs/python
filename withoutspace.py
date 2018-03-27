def count_letter(string):
    count=0
    for i in range(len(string)):
         if string[i].isalpha():
             count+=1
    return count
print(count_letter("python program is good"))
