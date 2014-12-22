from setuptools import setup

setup(name='freezeray',
      version='0.0.2',
      description='Freeze your Python package dependencies',
      url='https://github.com/gamechanger/freezeray',
      author='GameChanger',
      author_email='travis@gc.io',
      license='MIT',
      packages=['freezeray'],
      install_requires=['pip>=1.5.0,<6.0.0'],
      entry_points={'console_scripts': ['freezeray = freezeray.freeze:main']},
      zip_safe=False)
