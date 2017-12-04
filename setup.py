from setuptools import setup, find_packages
import re

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('client/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.rst') as f:
    readme = f.read()

setup(name='DiscoSpotipy',
      author='GiovanniMCMXCIX',
      author_email='irimea.giovani.9@gmail.com',
      url='https://github.com/GiovanniMCMXCIX/DiscoSpotipy',
      version=version,
      packages=find_packages(),
      license='MIT',
      description='A Discord RPC for Spotify written in Python.',
      long_description=readme,
      include_package_data=True,
      install_requires=requirements,
      test_suite='tests',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ]
      )