import json
import subprocess

m=[]
with open('lib.txt') as jsonfile:
  data= json.load(jsonfile)
  for p in data["Dependencies"]:
    m.append(p)
    subprocess.Popen(["pip","install",p],stdout=subprocess.PIPE,universal_newlines=True)


w=subprocess.Popen(["pip","list"],stdout=subprocess.PIPE,universal_newlines=True)

out=w.communicate()

u=out.split("\n")
u=u[2:]
v=[]

for i in u:
  x=[]
  t=i.split(" ")
  for j in t:
   
    if j!='':
      x.append(j)
      
 
  
  v.append("==".join(x))


failed=[]
for i in m:
  if i not in v:
    failed.append(i)
  
    
if len(failed)==0:
  print("SuccessFully Downloaded")
else:
  print("Failed To Download :")
  for j in failed:
    print(j)