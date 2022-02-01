import subprocess

InputTemplateFile = "templateConstaCosets.txt"
OutputFolder =  "outputs2/"
InputFolder = "inputs2/"

template = open(InputTemplateFile)
base=(template.readlines())
template.close()

print("TestCase using cyclotomic cosets")

q = int(input("enter field: "))
n = int(input("enter start length: "))
endn = int(input("enter max length: "))
a = 1
if q != 2:
    a = int(input("enter shift constant:"))

while n <= endn:
    program = base.copy()
    program[0]=program[0].replace("x", str(q))
    program[1]=program[1].replace("x", str(n))
    program[3]=program[3].replace("x", str(a))

    Ifile= InputFolder+"I"+ str(a) + "len" + str(n)+".txt"
    out=open(Ifile, "w")
    for p in program:
      out.write(p)
    out.close()

    Ofile=OutputFolder+ "O" + str(a) + "len" + str(n)+".txt"
    subprocess.Popen(["nohup magma < "+ Ifile +" > " +Ofile +"&"],shell=True)

    n+= 1;
    print("Done",n)
