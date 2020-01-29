import random
import json
import string

start_time = 350
start_size = 2
start_weight = 0.1
center = "center"
gap = center + ".gap"


child_prob = 0.7
time_inc_min = 10

time_inc_rand = 40

def add_node(node_list, parent_name, parent_time, parent_size, parent_weight):
    name = parent_name+'.'+''.join([random.choice(string.ascii_letters) for n in range(5)])
    imports = [center]
    time = parent_time - int(time_inc_min +  time_inc_rand * random.random())
    if time < 50:
        return
    while random.random() < child_prob:
        add_node(node_list, name, time, parent_size, parent_weight)
    while random.random() < child_prob:
        node_list.append({"name":name+'.'+''.join([random.choice(string.ascii_letters) for n in range(5)]),
                          "time":time-5,
                          "size":parent_size,
                          "weight":parent_weight,
                          "imports":[center]})
        imports = []
    node_list.append({"name":name,"time":time,"size":parent_size,"weight":parent_weight,"imports":[]})
    

node_list = []
while((len(node_list)<400) or (len(node_list)>1000)):
    node_list = []
    add_node(node_list, center, start_time, start_size, start_weight)
    print(len(node_list))
        
node_list.append({"name":center,"time":start_time,"size":start_size,"weight":start_weight,"imports":[]})

with open('big_bonkerfield_pre.json', 'w') as outfile:
    json.dump(node_list, outfile)
