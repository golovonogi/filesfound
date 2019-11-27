import argparse
from filesfound.typeoffiles.typeoffiles import count_types


def args_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", type=str, nargs='*',
                        help="type of files")
    parser.add_argument("path",type=str, help="in this path")
    parser.add_argument("-s", "--size", action="store_true",
                        help="size of files")
    args = parser.parse_args()


    types_files, count = count_types(args.type, args.path, args.size)
    for item in types_files.items():
        print(*item)
    print("Total files:", count)

