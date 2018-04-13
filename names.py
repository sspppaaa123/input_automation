import glob
names=glob.glob("codes\*.py")
file = open('file_names.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i]).replace("codes\\" , "")
    file.write(s)
    file.write('\n')
