# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
import os
from .utils import bash, get_config_file

DEFAULT = 'off'
CHECK_NAME = 'yamllint'
NO_YAMLLINT_MSG = ("yamllint is required for the yamllint plugin.\n"
                "`pip install yamllint` or turn it off in your {} file.".format(get_config_file()))


def _filter_yaml_files(files):
    "Get all python files from the list of files."
    yaml_files = []
    for f in files:
        # If we end in .py, or if we don't have an extension and file says that
        # we are a python script, then add us to the list
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
