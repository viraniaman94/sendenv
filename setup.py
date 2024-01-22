from setuptools import setup, find_packages

setup(
    name='sendenv',
    version='0.1.1',
    description='A tool for developers to share environment variables with their team over the internet.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aman Virani',
    author_email='viraniaman94@gmail.com',
    url='https://github.com/viraniaman94/sendenv',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
        'Topic :: Communications :: File Sharing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.10',
    install_requires=[
        'prompt_toolkit==3.0.43',
        'magic-wormhole==0.13.0'
    ],
    entry_points={
        'console_scripts': [
            'sendenv=main:main',
        ],
    },
)