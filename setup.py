from setuptools import find_packages, setup
setup(
    name='FSRray',
    packages=find_packages(include=['FSRray']),
    version='1.0.0',
    description='My first Python library',
    author='Alexis Devillard',
    license='MIT',
    install_requires=['pyserial'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)