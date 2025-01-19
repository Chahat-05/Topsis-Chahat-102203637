from setuptools import setup, find_packages

setup(
    name='Topsis-Chahat-102203637',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli=topsis.Chahat_102203637:main',  # This will be the entry point for your CLI
        ],
    },
    description='A Python package to implement the TOPSIS method for multi-criteria decision analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chahat',
    author_email='cverma_be22@thapar.edu',
    url='https://github.com/yourusername/topsis_package',  # Replace with your repo URL
    license='MIT',
)
