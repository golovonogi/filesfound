import os
import magic
from collections import Counter
from filesfound.sizeoffiles.sizeoffiles import find_size


def find_in_path(path):
    all_files = []
    types = {}
    files=os.listdir(path)

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            all_files.append(os.path.join(path, file))
        elif os.path.isdir(os.path.join(path, file)):
            all_files += find_in_path(os.path.join(path, file))
        else:
            raise ValueError(os.path.join(path, file))

    for file in all_files:
        mimetype = magic.Magic().from_file(file)
        types.update({file:mimetype})

    return types

def count_types(types, path, size):
    files = find_in_path(path)
    c = Counter()
    count = 0
    all_need_types = {}
    for value in files.values():
        c[value] += 1

    if types==[] and size is False:
        count = len(files)
        return c, count

    elif types and size is False:
        for type in types:
            if type in c.keys():
                value = c.get(type)
                all_need_types.update({type: value})
                count += value
        return all_need_types, count

    elif size is True:
        return find_size(types, files)




















