import setuptools


def fix_requirement(x):
    if x.startswith('git+'):
        package = x.split('.git')[0].split('/')[-1]
        return f'{package} @ {x}'
    else:
        return x


with open('version') as f:
    version = f.read().strip()
with open('requirements.txt') as f:
    required = f.read().splitlines()
    required = [fix_requirement(x) for x in required]


setuptools.setup(
    name='text_cleaning',
    version=version,
    author='Tim Niven',
    author_email='tim@doublethinklab.org',
    description='Text cleaning utilities, functions, and pipelines.',
    url=f'https://github.com/doublethinklab/text-cleaning.git#{version}',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=required)
