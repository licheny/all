with open("score/james.txt","r") as file1:
    james_time=file1.readline().strip().split(",")
#print(james_time)
with open("score/mikey.txt","r") as file2:
    mikey_time=file2.readline().strip().split(",")
with open("score/sarah.txt","r") as file3:
    sarah_time=file3.readline().strip().split(",")
with open("score/julie.txt","r") as file4:
    julie_time=file4.readline().strip().split(",")

def stander1(the_list):
    #print(the_list)
    if the_list.find("-")!=-1:
        #print("hello")
        (mins,sec)=the_list.split("-")
    elif the_list.find(":")!=-1:
        (mins,sec)=the_list.split(":")
    else:
        return the_list
    the_list=mins+"."+sec
    return the_list

james_backup_time=list()
mikey_backup_time=list()
sarah_backup_time=list()
julie_backup_time=list()

for each_time in james_time:
    james_backup_time.append(stander1(each_time))
for each_time in mikey_time:
    mikey_backup_time.append(stander1(each_time))
for each_time in sarah_time:
    sarah_backup_time.append(stander1(each_time))
for each_time in julie_time:
    julie_backup_time.append(stander1(each_time))
# print(james_backup_time)
james_backup_time.sort()
mikey_backup_time.sort()
sarah_backup_time.sort()
julie_backup_time.sort()
print(james_backup_time)
print(mikey_backup_time)
print(sarah_backup_time)
print(julie_backup_time)


