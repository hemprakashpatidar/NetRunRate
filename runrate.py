T1=input("Enter Team Name ")
cnrr=int(input("Enter Current runrate "))
m=int(input("Enter matches played "))
thresh=float(input("Enter runrate to overcome "))
f1=(cnrr+7.5)*20*m
scores=[f1,20*m,150*m,20*m]


print("If", T1, "bat first")
for1b1=(scores[0]+150)/(scores[1]+20)
for i in range(150,1,-1):
  nrr=for1b1-(scores[2]+i)/(scores[3]+20)
  if nrr>thresh:
    print(T1, "needs to win by atleast",150-i,"runs")
    break
print("if",T1,"bowls first")
for2b2=(scores[2]+150)/(scores[3]+20)
i=20.0
while(i>=0):
  nrr=(scores[0]+151)/(scores[1]+i)-for2b2
  if nrr>thresh:
    print(T1, "needs to win in ",int(i)+round((i-int(i))*0.6,1),"overss")
    break
  i=i-1/6
