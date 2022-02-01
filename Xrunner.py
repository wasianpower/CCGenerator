import subprocess
import os

def makedir(dirName):
    os.makedirs(dirName, exist_ok=True )

def main():
  #Python runner source:
  validFields = [2,3,4,5,7,8,9,11,13]
  shiftDict = { #field -> array in the form (shift constant, length coeffiecent)
    2 : [(1,1)],
    3 : [(2,2)],
    4 : [(2,3)],
    5 : [(2,2),(4,4)],
    7 : [(2,3),(3,2),(3,3),(6,2)],
    8 : [(2,7)],
    9 : [(3,2),(4,4),(6,8)],
    11 : [(2,2),(2,5),(3,5),(10,2)],
    13 : [(2,2),(2,3),(3,3),(4,3),(4,4),(5,2),(12,4)]
  }
  maxDict = {
    2 : 256,
    3 : 243,
    4 : 256,
    5 : 130,
    7 : 100,
    8 : 130,
    9 : 130,
    11 : 200,
    13 : 200
  }
  q = int(input("enter a valid field: "))
  startn = int(input("enter start length: "))
  endn = int(input("enter end length: "))
  #IMPORTANT NOTE: since you cant enter input for a nohup, I've just been copying the python files for each field and manually entering length/field info before running. Could also have it read from an input file, perhaps #TODO?
  m = 0
  fileroute = "ConstructionX.txt"
  template = open(fileroute)
  base=(template.readlines())
  template.close()
  used = []
  prev = 0
  makedir("GF" + str(q) + "in")
  makedir("GF" + str(q) + "out")
  for pair in shiftDict[q]:
      a = pair[0]
      n = startn - (startn % pair[1]) + pair[1]
      if pair[0] != prev:
          used = []
          prev = pair[0]
      while n < endn:
          if n in used:
              print("Skipping")
              print(n)
          else:
              used.append(n)
              program = base.copy()
              program[0]=program[0].replace("xxx", str(q))
              program[1]=program[1].replace("xxx", str(n))
              program[2]=program[2].replace("xxx", str(a))
              program[3]=program[3].replace("xxx", "50")
              program[4]=program[4].replace("xxx", str(maxDict[q]))
              out=open("GF" + str(q) + "in/inputshift" + str(a) + "len" + str(n) + ".txt", "w")
              for p in program:
                out.write(p)
              out.close()

              #Alternative

              subprocess.Popen(["nohup magma < GF" + str(q) + "in/inputshift" + str(a) + "len" + str(n) + ".txt >> GF" + str(q) + "out/outputshift" + str(a) + "len" + str(n)+".txt"],shell="True")
              print("Doing")
              print(n)
          n += pair[1]


main()