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
    name='nlp_pipeline',
    version=version,
    author='Tim Niven',
    author_email='tim@doublethinklab.org',
    description='API and client for our NLP pipeline.',
    url=f'https://github.com/doublethinklab/nlp-pipeline.git#{version}',
    packages=setuptools.find_packages(),
    package_data={'': ['*.yml']},
    python_requires='>=3.9',
    install_requires=required)
