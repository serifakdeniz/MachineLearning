import numpy as np
names= ['Ben','mehmet','serif','nedim']
call_numbers=[300,10,70,23]
average_deal_sizes=[8,6,24,23]
revenues=[2400,60,12000,2333]
data=np.array([],dtype=int)
 
def append_names(names_list):
    global data
    for i in names_list:
        data=np.append(data,names.index(i))

def append_performance_measures(feature_list):
    global data
    data=np.append(data,feature_list)


append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

print(data)
print(data.shape)

data=data.reshape(4,4)
print(data)
print(data.shape)
print(data[0])
print(data[1])
print(data[2])
print(data[3])



def calculate_performance(employee_name):
    idx=names.index(employee_name)
    number_of_calls=data[1,idx]
    avg_deal_size=data[2,idx]
    revenue=data[3,idx]
    score=(avg_deal_size*revenue)/number_of_calls
    return score

print(calculate_performance("serif"))
print(calculate_performance("mehmet"))

performance_scores=[]
for name in names:
    score=int(calculate_performance(name))
    performance_scores.append(score)

data=np.concatenate((data,[performance_scores]),axis=0)

print(data)

idx_best_employee=np.argmax(data[4])
idx_worst_employee=np.argmin(data[4])
print(idx_best_employee)
print(idx_worst_employee)

print("**********************************************************")
print(data[1,2])