import os
from platform import system

from setuptools import setup

data_dir_path: str = {
    'Windows': os.path.join(os.environ.get('LOCALAPPDATA', ''), 'dictCLI'),
    'Linux': os.path.join(os.environ.get('HOME', ''), '.cache', 'dictCLI'),
}[str(system())]
data_dir_exists = os.path.exists(data_dir_path)
cache_dir_exists = os.path.exists(os.path.join(data_dir_path, 'word_cache'))

if not data_dir_exists:
    os.mkdir(data_dir_path)
    if not cache_dir_exists:
        os.mkdir(os.path.join(data_dir_path, 'word_cache'))
# XXX: unreadable one line implementation of above nested if statement
# os.mkdir(data_dir_path)
# (os.mkdir(os.path.join(data_dir_path, 'word_cache'))
#  if cache_dir_exists else None) if not data_dir_exists else None
setup(
    name='dictionary',
    url='https://www.github.com/Chaitanyabsprip/dictionaryCLI',
    author='Chaitanya Sharma',
    author_email='chaitanyasanjeevsharma@gmail.com',
    description=
    'A command line dictionary that allows you to bookmark words and easily flip through them.',
    long_description='',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    license='MIT',
    py_modules=['config'],
    packages=['dictcli'],
    # scripts=['main.py'],
    entry_point={'console_scripts': ['dictcli.main=main:main']},
)
