import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sedipack", # Replace with your own username
    version="0.0.6.1",
    author="Philip Ireoluwa Okiokio",
    author_email="philipokiokio@gmail.com",
    description="A Sedimentology package for Grain Statistics and Plots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philip-kio/SediPack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib', 'pandas', 'numpy']
)

