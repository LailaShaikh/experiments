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


def get_dirs_list(path):
    return [os.path.join(path, d) for d in os.listdir(path) \
            if os.path.isdir(os.path.join(path, d))]



def get_files_only(path):
    return [d for d in os.listdir(path) \
            if os.path.isfile(os.path.join(path, d))]


def print_line(files, level=1):
    for _f in files:
        print "\t" * level, "|---- %s" %_f


def start_from_dir(_path, level=1):
    #print "\t o" * level
    print "\n", "\t" * level, _path
    _files = get_files_only(_path)
    print_line(_files, level)


def tree(top_path):
    start_from_dir(top_path, level=0)
    _dirs = [(1, i) for i in get_dirs_list(top_path) if i]
    while _dirs:
        level, curr_dir = _dirs.pop()
        start_from_dir(curr_dir, level)
        
        
        _dirs.extend([(level + 1, i) for i in get_dirs_list(curr_dir) if i])


if __name__ == '__main__':
    #tree('/home/navaneethan/workspace/hirenew')
    tree('/home/navaneethan/workspace/autosourcing_engine/tests')
