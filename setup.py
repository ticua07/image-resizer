from setuptools import setup

setup(
    name='image-resizer',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
        'pillow'
    ],
    entry_points='''
        [console_scripts]
        image-resize=main:resize
    ''',
)