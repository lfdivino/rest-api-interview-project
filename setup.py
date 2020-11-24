from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]


setup(
    name='api_interview',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/lfdivino/888-spectate-interview-project',
    author='Luiz Felipe do Divino',
    author_email='lf.divino@gmail.com',
    description='API to consume external data to save new events '
                'and support consults for the matches details',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=read("requirements.txt"),
)
