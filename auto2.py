import subprocess
import filecmp
f1 = open('input.txt' , 'r')
f2 = open('output.txt', 'r')
f3 = open('file_names.txt' , 'r')
f4 = open('status.txt' , 'w')
ip_names = f1.readlines()
op_names = f2.readlines()
scripts = f3.readlines()

for i in range(0 , len(scripts)):
    s = 'Op\output' + str(i) + '.txt'
    myinput = open(str(ip_names[i]).rstrip('\n') , 'r')
    myoutput = open( s , 'w')
    p = subprocess.Popen(str(scripts[i]).rstrip('\n'), stdin=myinput, stdout=myoutput, stderr=myoutput , shell = True)
    p.wait()
    myoutput.flush()
    t = filecmp.cmp(str(op_names[i]).rstrip('\n') , s)
    if t == True:
        f4.write(str(scripts[i]).rstrip('\n') + ' -successful\n')
    else:
        f4.write(str(scripts[i]).rstrip('\n') + ' -failed\n')
        






