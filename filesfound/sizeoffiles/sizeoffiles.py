import os



#def find_size(all_files, types):
#        c = 0
#        s = 0
#        t = find_type(all_files)
#        for type in types:
#            for k, v in t.items():
#                if v == type:
#                    c += 1
#                    s += os.path.getsize(k)
#        return s, c



def find_size(types, all_types):
    size = 0
    all_values = {}
    if types==[]:
        for k in all_types.keys():
            size_of_file = os.path.getsize(k)
            all_values.update({k:size_of_file})
            size += os.path.getsize(k)
        return all_values, size
    elif types:
        for type in types:
            for k, v in all_types.items():
                if v == type:
                    size_of_file = os.path.getsize(k)
                    all_values.update({k:size_of_file})
                    size += size_of_file
        return all_values, size


