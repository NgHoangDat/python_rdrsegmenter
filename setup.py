import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


__version__ = 'v0.1.0'


setuptools.setup(
    name="python_rdrsegmenter",
    packages=setuptools.find_packages(),
    version=__version__,
    author="nghoangdat",
    author_email="18.hoang.dat.12@gmail.com",
    description="python_rdrsegmenter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python-rdrsegmenter rdrsegmenter nlp vietnamese-nlp parser word-segmentation tokenizer',
    url="https://github.com/NgHoangDat/python_rdrsegmenter.git",
    download_url=f"https://github.com/NgHoangDat/python_rdrsegmenter/archive/{__version__}.tar.gz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'pyjnius'
    ]
)