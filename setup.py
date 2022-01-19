from setuptools import setup, find_packages
import os


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='flaxmodels',
      version='0.1.1',
      url='https://github.com/matthias-wright/flaxmodels',
      author='Matthias Wright',
      packages=find_packages(),
      install_requires=['h5py',
                        'numpy',
                        'requests',
                        'packaging',
                        'dataclasses',
                        'filelock',
                        'jax',
                        'jaxlib',
                        'flax',
                        'Pillow',
                        'regex',
                        'tqdm'],
      extras_require={
        'testing': ['pytest'],
      },
      python_requires='>=3.6',
      license='Each model has an individual license.',
      description='A collection of pretrained models in Flax.',
      long_description=long_description,
      long_description_content_type='text/markdown')
