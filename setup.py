from setuptools import setup

setup(name='coordinate_finder',
      version='0.4',
      description='Equidistaqnt Coordinate Finder',
      packages=['coordinate_finder'],
      author='Alex Terry & Alistair Heath',
      author_email='alexterry48@gmail.com',
      zip_safe=False,
      include_package_data=True)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="EAlex Terry & Alistair Heath",
    author_email="alexterry48@gmail.com.com",
    description="Package to find Lat & Long coordinates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
