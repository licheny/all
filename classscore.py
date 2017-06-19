def sanitize(the_list):
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

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times])))[0:3]

def get_score_data(filename):
    try:
        with open(filename,"r") as score:
            data=score.readline()
        templ=data.strip().split(",")
        return(Athlete(templ[0],templ[0],templ))
    except IOError as fileerror:
        print("File error"+str(fileerror))
        return(None)

james=get_score_data("score/james.txt")

print(james.name+"best scores are"+str(james.top3()))