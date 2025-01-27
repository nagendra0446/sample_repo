from setuptools import setup, find_packages

setup(
    name='grading',
    version='0.1.0',
    description='A sample grading package that returns the current timestamp.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/grading',  # Replace with your actual GitHub repo URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
