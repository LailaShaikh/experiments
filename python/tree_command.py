import os

'''
|-f1
|-f2
|-d1
| |-f1
| |-f2
| |-d2
|    |-f1
|-d2

'''


def print_line(files):
    for _f in files:
        print "\t |---- %s" %_f


def tree(top_path):
    for root, dirs, files in os.walk(top_path):
        print "%s" % root, dirs
        print_line(files)


if __name__ == '__main__':
    #tree('/home/navaneethan/workspace/hirenew')
    tree('/home/navaneethan/workspace/autosourcing_engine/tests')
