FilesFound
____________

Found Files on PC

Example:
#find all files in path with types
$ python main.py /home/user/test
    image/png 6
    text/plain 7
    text/html 1
    image/jpeg 6
    Total files: 20

#find files with sizes and sum all sizes
$ python main.py /home/user/test -s
    /home/user/test/file.png 84462
    ...
    Total files: 2475648

#find files image/png and their size
$ python main.py image/png /home/user/test -s
    /home/user/test/file1.png 84462
    /home/user/test/file2.png 136865
    ...
    Total files: 1478124

#find two types of files and their sizes
$ python main.py image/png text/html /home/user/test -s
    /home/user/test/file1.png 84462
    /home/user/test/file2.html 136865
    ...
    Total files: 1909123

#find two types of files in path
$ python main.py image/png text/html /home/user/test
    image/png 6
    text/html 1
    Total files: 7






