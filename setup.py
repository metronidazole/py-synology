from distutils.core import setup

setup(
    name='py-synology',
    version='0.5.1',
    packages=['synology'],
    url='https://github.com/metronidazole/py-synology',
    license='MIT',
    author='snjoetw, metronidazole',
    author_email='',
    description='Python API for Synology Surveillance Station (DSM7)',
    requires=['requests']
)
