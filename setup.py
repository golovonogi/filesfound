from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='filesfound',
      version='0.1',
      description='The square of numbers',
      url='http://github.com/golovonogi/filesfound',
      packages=['filesfound'],
      include_package_data=True,
      entry_points={
            'console_scripts': ['filesfound=filesfound.main:args_command'],
      },
      zip_safe=False,
      test_suite="tests",
      )