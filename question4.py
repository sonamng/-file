from os import write


file1=open("question3.txt","r")
for i in file1:
     if "delhi" in i:
          a=open("delhi.txt","a")
          a=write(i)
     elif "shimla" in i:
          e=open("shimla.txt","a")
          e.write(i)
     else:
          p=open("other city.txt","a")
          p.write(i)