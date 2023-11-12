import os
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    version='0.9.0',
    name='croco_selenium',
    author='Alexey',
    author_email='abelenkov2006@gmail.com',
    description='The package providing ways to interact with Selenium Web Driver actions, such as clicking, sending keys etc.',
    keywords='croco selenium actions, webdriver, croco selenium',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blnkoff/croco-selenium',
    project_urls={
        'Documentation': 'https://github.com/blnkoff/croco-selenium',
        'Bug Reports':
        'https://github.com/blnkoff/croco-selenium/issues',
        'Source Code': 'https://github.com/blnkoff/croco-selenium',
    },
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS'
    ],
    python_requires='>=3.11',
    install_requires=install_requires
)
