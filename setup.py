from setuptools import setup, find_packages

requirements = [
    'requests',
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='integresql-client-python',
    version='0.9.2',
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/msztolcman/integresql-client-python',
    project_urls={
        'GitHub: issues': 'https://github.com/msztolcman/integresql-client-python/issues',
        'GitHub: repo': 'https://github.com/msztolcman/integresql-client-python',
    },
    download_url='https://github.com/msztolcman/integresql-client-python',
    author='Marcin Sztolcman',
    author_email='marcin@urzenia.net',
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=requirements,
    # see: https://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: BDD',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Unit',
    ]
)
