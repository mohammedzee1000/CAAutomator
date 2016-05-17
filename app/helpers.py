import os

def create_dir(path, perms = None):
    """Checks if a path exists, if not attempts to create it with any permissions, if specified"""

    if not os.path.exists(path):
        os.mkdir(path)

    if perms != None:
        os.chmod(path, perms)

    return

def touchfile(path, text, perms = None):
    """Checks if a file at specified path exists, if not attempts to create it with permissions, if specified"""

    if not os.path.exists(path):
        target = open(path, "w")
        target.write(text)
        target.close()

    if perms != None:
        os.chmod(path, perms)

    return