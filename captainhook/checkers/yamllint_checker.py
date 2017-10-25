# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import os
from .utils import bash, get_config_file

DEFAULT = 'off'
CHECK_NAME = 'yamllint'
NO_YAMLLINT_MSG = ("yamllint is required for the yamllint plugin.\n"
                   "`pip install yamllint` or turn it off in your {}"
                   " file.".format(get_config_file()))
REQUIRED_FILES = ['.yamllint']


def _filter_yaml_files(files):
    "Get all yaml files from the list of files. The extention based filter"
    yaml_files = []
    for f in files:
        extension = os.path.splitext(f)[-1]
        if extension:
            if extension in ('.yaml', 'yml'):
                yaml_files.append(f)

    return yaml_files


def run(files, temp_folder):
    """Check yaml format.

    """
    try:
        import yamllint  # NOQA
    except ImportError:
        return NO_YAMLLINT_MSG

    yaml_files = _filter_yaml_files(files)

    if yaml_files:
        return bash('yamllint {0}'.format(' '.join(yaml_files))).value()
    return ''
