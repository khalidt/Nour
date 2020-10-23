import setuptools

with open("README.md", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="Nour", 
    version="1.0.3",
    author="Khalid Alkhaldi",
    author_email="K.T.Alkhaldi@gmail.com",
    description="Nour is a tool which converts Arabic words, letters or sentences to and from  Braille notations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khalidt/Nour",
    keywords='Conversion, Braille, development, Arabic to Braille, converter, Arabic Braille, translater, letters, notations,Python, nour',
    package_dir={'': 'src'},  # Optional
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.6'
)
