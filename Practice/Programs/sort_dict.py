def sort_dict(d):
    sort_by_values = dict(sorted(d.items(), key= lambda items: items[1]))
    sort_by_keys = dict(sorted(d.items(), key= lambda items: items[0]))
    print(f"{sort_by_values} \n {sort_by_keys}")


sort_dict({'one':1, 'two':2,  'four':4,'three':3,})