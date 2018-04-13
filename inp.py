import glob
names=glob.glob("input_files\*.txt")
file = open('input.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i])
    file.write(s)
    file.write('\n')
