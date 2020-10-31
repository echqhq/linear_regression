from setuptools import find_packages, setup
setup(
    name='linear_regression_echqhq',
    packages=find_packages(include=['linear_regression_echqh']),
    version='0.1.0',
    description='Linear regression implementation',
    author='echqhq',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)