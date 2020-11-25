from setuptools import setup


def readme():
    """Reads the 'READMD.md' file

    Returns:
        string: 'README.md' file content
    """
    with open('README.md') as file:
        return file.read()


setup(
    name='MachiKoroAI',
    version='0.0.1',
    author='Jens den Braber',
    author_email='',
    packages=['machi_koro.ai'],
    python_requires='>=3.8',
    license='LICENSE.txt',
    description='An AI package for the card game Machi Koro',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'machi_koro',
        'tensorflow'
    ],
    tests_require=['pytest'],
    entry_points={'console_scripts': [
        ''
    ]}
)
