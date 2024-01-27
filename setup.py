from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

def read_version():
    with open('VERSION', 'r') as version_file:
        version = version_file.read().strip()

    return version

setup(
    name='sendenv',
    version=read_version(),
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
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'sendenv=sendenv.main:main',
        ],
    },
)