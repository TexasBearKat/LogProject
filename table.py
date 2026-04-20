from log import log

def create_table(groupdim, pointerdim, base, start, digits):
    counter = start
    return_list = []
    group = []

    for i in range(0, groupdim):    
        for j in range(0, pointerdim):
            group.append(f"log{base} {counter} = ")
            group.append(str(log(base=base, y=counter, digits_past_decimal=digits)))
            counter += 1
    
        return_list.append(group)
        group = []
    
    return return_list
