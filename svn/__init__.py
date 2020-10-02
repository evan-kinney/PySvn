__version__ = '1.0.1'

import svn.utility

def Client(url_or_path, *args, **kwargs):
    return svn.utility.get_client(url_or_path, *args, **kwargs)