import argparse
from filesfound.typeoffiles.typeoffiles import find_in_path, count_types


def args_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", type=str, nargs='*',
                        help="type of files")
    parser.add_argument("path",type=str, help="in this path")
    parser.add_argument("-s", "--size", action="store_true",
                        help="size of files")
    args = parser.parse_args()

    #files = find_in_path(args.path)
    #print("Total files:", len(files))

    types_files, count = count_types(args.type, args.path, args.size)
    for item in types_files.items():
        print(*item)
    print("Total files:", count)

    #вывод элементов по типу
    #types = find_type(all_files)
    #c = count_types(types)
    #for item in c.items():
    #    print(*item)

    #вывод элементов по заданному типу
    #spec_type, count = find_specific_type(c, args.type)
    #print("Total files:", count)
    #for item in spec_type.items():
    #    print (*item)

    #подсчет размера файлов по типу
    #s, c = find_size(all_files, args.type)
    #print("Total files:", c)
    #print("Total size:", s, "bytes")

    #s, c = find_size(args.type, args.path, all_files)
    #print("Total files:", c)
    #print("Total size:", s, "bytes")


