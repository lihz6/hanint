import setuptools

with open('../README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hanint',
    version='0.1.1',
    author='李鸿章',
    author_email='paindo@163.com',
    description='数字转汉字，如：`101`转`一百零一`',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ngolin/hanint',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'hanint = hanint.index:main'
        ]
    }
)

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*
