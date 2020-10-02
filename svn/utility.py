import os
import re

import svn.common
import svn.local
import svn.remote
import svn.constants

def get_client(url_or_path, *args, **kwargs):
    return svn.remote.RemoteClient(url_or_path, *args, **kwargs) if is_url(url_or_path) else svn.local.LocalClient(url_or_path, *args, **kwargs)

def is_url(url_or_path):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_regex, url_or_path)

def get_common_for_cwd():
    path = os.getcwd()
    uri = 'file://{}'.format(path)

    cc = svn.common.CommonClient(uri, svn.constants.LT_URL)
    return cc
