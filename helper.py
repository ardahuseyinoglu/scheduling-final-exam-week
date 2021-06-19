course_days = ["BBM102-d",
      "BBM202-d",
      "BBM234-d",
      "BBM242-d",
      "BBM342-d",
      "BBM382-d",
      "BBM405-d",
      "BBM406-d",
      "BBM410-d",
      "BBM416-d",
      "BBM421-d",
      "BBM428-d",
      "BBM432-d",
      "BBM442-d",
      "BBM456-d",
      "BBM461-d",
      "BBM467-d",
      "BBM486-d",
      "AIN200-d",
      "AIN212-d",
      "ELE296-d",
      "FIZ138-d",
      "AIT204-d",
      "MAT254-d",
      "MUH104-d",
      "BEB650-d",
      "FIZ117-d",
      "IST292-d",
      "ING112-d",
      "TKD104-d",
      "MAT124-d"]


course_hours = ["BBM102-h",
      "BBM202-h",
      "BBM234-h",
      "BBM242-h",
      "BBM342-h",
      "BBM382-h",
      "BBM405-h",
      "BBM406-h",
      "BBM410-h",
      "BBM416-h",
      "BBM421-h",
      "BBM428-h",
      "BBM432-h",
      "BBM442-h",
      "BBM456-h",
      "BBM461-h",
      "BBM467-h",
      "BBM486-h",
      "AIN200-h",
      "AIN212-h",
      "ELE296-h",
      "FIZ138-h",
      "AIT204-h",
      "MAT254-h",
      "MUH104-h",
      "BEB650-h",
      "FIZ117-h",
      "IST292-h",
      "ING112-h",
      "TKD104-h",
      "MAT124-h"]


courses = ["BBM102",
      "BBM202",
      "BBM234",
      "BBM242",
      "BBM342",
      "BBM382",
      "BBM405",
      "BBM406",
      "BBM410",
      "BBM416",
      "BBM421",
      "BBM428",
      "BBM432",
      "BBM442",
      "BBM456",
      "BBM461",
      "BBM467",
      "BBM486",
      "AIN200",
      "AIN212",
      "ELE296",
      "FIZ138",
      "AIT204",
      "MAT254",
      "MUH104",
      "BEB650",
      "FIZ117",
      "IST292",
      "ING112",
      "TKD104",
      "MAT124"]

bbm_4xx_courses = ["BBM405",
      "BBM406",
      "BBM410",
      "BBM416",
      "BBM421",
      "BBM432",
      "BBM442",
      "BBM456",
      "BBM461",
      "BBM467",
      "BBM486"]

exam_hours = [3,3,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,2,2,2,1,2]
exam_dict = dict(zip(courses, exam_hours))


#-----------------------------------------------------------------------------------------

for course in course_hours:
    print("(or (= {0} 9)(= {0} 10)(= {0} 11)(= {0} 12)(= {0} 13)(= {0} 14)(= {0} 15)(= {0} 16)(= {0} 17)(= {0} 18))".format(course))

#-----------------------------------------------------------------------------------------

from itertools import combinations
 
comb = combinations(courses, 2)
for i in list(comb):
    p0 = str(exam_dict[i[0]])
    p1 = str(exam_dict[i[1]])
    print ("(=> (= {0}-d {1}-d) (or (<= (+ {0}-h {2}) {1}-h) (<= (+ {1}-h {3}) {0}-h)))".format(i[0], i[1], p0, p1))

#-----------------------------------------------------------------------------------------

comb = combinations(bbm_4xx_courses, 3)
for i in list(comb):
    print ("(=> (= {0}-d {1}-d) (distinct {2}-d {0}-d))".format(i[0],i[1],i[2]))
    
#-----------------------------------------------------------------------------------------

comb = combinations(bbm_4xx_courses, 2)

for i in list(comb):
    p0 = str(exam_dict[i[0]])
    p1 = str(exam_dict[i[1]])
    print ("(=> (= {0}-d {1}-d) (and (distinct (+ {0}-h {2}) {1}-h) (distinct (+ {1}-h {3}) {0}-h)))".format(i[0], i[1], p0, p1))

#-----------------------------------------------------------------------------------------


import pandas as pd
import numpy as np

df = pd.DataFrame(columns=("4","7", "8", "9", "10", "11"),index=("9","10","11","12","13","14","15","16","17","18"))

new_dict = {}
# first element is day second element is hour.
for course in courses:
    new_dict[course] = [None, None]



f = open("smt2_out.txt")

while True:
    line1 = f.readline()
    line2 = f.readline()
        
    if line2:
        course, info = line1.split()[1].split("-")
        num = line2.split()[0][:-1]
        if info == 'd':
            new_dict[course][1] = num
        elif info == 'h':
            new_dict[course][0] = num
    
    else: break


for key, value in new_dict.items():
    #print(key, value)
    if type(df.loc[value[0],value[1]]) is list:
        df.loc[value[0],value[1]].append(key)
    else:
        df.loc[value[0],value[1]] = [key]