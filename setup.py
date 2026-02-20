from setuptools import setup, find_packages

setup(
    name='Adyen',
    packages=find_packages(include=["Adyen*"], exclude=["tests", "tests.*"]),
    version='14.0.0',
    maintainer='Adyen',
    maintainer_email='support@adyen.com',
    description='Adyen Python Api',
    long_description="A Python client library for accessing Adyen APIs",
    author='Adyen',
    author_email='support@adyen.com',
    url='https://github.com/Adyen/adyen-python-api-library',
    keywords=['payments', 'adyen', 'fintech'],
    python_requires='>=3.8',
    install_requires=[], # Core is standard library only, plus optional clients below
    extras_require={
        "requests": ["requests>=2.25.0"],
        "pycurl": ["pycurl>=7.43.0"],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "mock>=4.0.0",
            "requests>=2.25.0",
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ]
)
