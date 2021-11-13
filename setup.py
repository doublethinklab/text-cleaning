import setuptools


with open('requirements.txt') as f:
    required = f.read().splitlines()
with open('version') as f:
    version = f.read().strip()


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
