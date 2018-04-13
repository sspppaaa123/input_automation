import glob
names=glob.glob("output_files\*.txt")
file = open('output.txt' , 'w+')
for i in range(0 , len(names)):
    s = str(names[i])
    file.write(s)
    file.write('\n')