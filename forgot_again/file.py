from ast import literal_eval
from os import remove, makedirs
from os.path import isfile, isdir
from pprint import pprint
from subprocess import Popen


def remove_if_exists(path):
    if isfile(path):
        remove(path)


def load_ast_if_exists(path, default=None):
    if isfile(path):
        with open(path, 'rt', encoding='utf-8') as f:
            return literal_eval(''.join(f.readlines()))
    return default


def pprint_to_file(file, data):
    with open(file, mode='wt', encoding='utf-8') as f:
        pprint(data, stream=f, sort_dicts=False)


def make_dirs(path):
    if not isdir(f'{path}'):
        makedirs(f'{path}')


def open_explorer_at(path):
    Popen(f'explorer /select,"{path}"')
