from setuptools import setup

setup(name='OpenSeesAPI',
      version='0.1',
      install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
      ],
      description='A OpenSees Wrapper in Python',
      url='http://github.com/nassermarafi/OpenSeesAPI',
      author='Nasser Marafi',
      author_email='marafi@uw.edu',
      license='UW',
      packages=['OpenSeesAPI'],
      zip_safe=False)
