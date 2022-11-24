from setuptools import find_packages, setup


setup(
    name='hello-heroku',
    version='0.0.1',
    author='mr',
    url='https://github.com/lenarother/hello-heroku',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)