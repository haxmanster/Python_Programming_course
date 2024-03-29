import os
from distutils.core import setup, Command


class CheckTabs(Command):
    """ TABs checker """
    description = 'check if files contain TABs'
    user_options = []

    def initialize_options(self):
        """ Init options """
        pass

    def finalize_options(self):
        """Finalize options"""
        pass

    def run(self):
        """ Run command """
        for root, dirs, files in os.walk('.'):
            for name in files:
                fpath = os.path.join(root, name)
                if self._contains_tabs(fpath):
                    print('ERROR: TABs in <%s>' % fpath)

    @staticmethod
    def contains_tabs(fpath):
        """ Return True if fpath file contains tabs. """
        with open(fpath) as f:
            return '\t' in f.read()


setup(name='wordcount',
      version='1.0',
      author='<Your name>',
      py_modules=['wordcount'],
      data_files=[('.', ['sherlock.txt'])],
      cmdclass={'check_tabs': CheckTabs})
