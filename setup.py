from setuptools import setup

setup(name='OpenSeesAPI',
      version='0.12',
      # install_requires=[
      # "numpy",
      # "matplotlib",
      # ],
      description='A OpenSees Wrapper in Python',
      url='http://github.com/nassermarafi/OpenSeesAPI',
      author='Nasser Marafi',
      author_email='marafi@uw.edu',
      license='MIT',
      packages=['OpenSeesAPI', 'OpenSeesAPI.Analysis', 'OpenSeesAPI.Model','test'],
      zip_safe=False)
