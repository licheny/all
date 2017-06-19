import sys
def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
    for each_ite m in the_list:
        if isinstance(each_line,list):
            print_lol(each_line,ident,level+1,fn)
        else:
            if(indent):
                for tap_stop in range(level):
                    print("\t",end="",file=fn)
            print(each_item,file=fn)
#读取文件将其转换为list
man=list()
other=list()
try:
    data=open("sketch.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            line_spoken=line_spoken.strip()
            if(role=="Man"):
                man.append(line_spoken)
            elif(role=="Other Man"):
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The datafile is missing!")
#将list写入文件中
try:
    man_file=open("man_data.txt","w")
    other_file=open("other_data.txt","w")
    print_lol(man,True,1,fn=man_file)
    print_lol(other,True,1,fn=other_file)
except IOError:
    print("File error.")
finally:
    man_file.close()
    other_file.close()