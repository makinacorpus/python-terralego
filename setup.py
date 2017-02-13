from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='terralego',
    version='0.1',
    description='Python bindings for Terralego services.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',

    ],
    url='https://terralego.fr',
    author='Autonomens',
    author_email='contact@autonomens.fr',
    license='MIT',
    packages=['terralego'],
    install_requires=[
        'requests==2.13.0',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
)
