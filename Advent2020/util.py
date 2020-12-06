
def filemap(func, filename, sep='\n'):
    with open(filename) as f:
        raw = f.read().strip().split(sep)
        return list(map(func, raw))