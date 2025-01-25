def insert_ordered(data: list, val):
    for i, v in enumerate(data):
        if val < v:
            data.insert(i, val)
            return
    data.append(val)

data = []
while txt := input():
    day, mm = txt.split()
    insert_ordered(data, (day, int(mm)))
            
print(data)