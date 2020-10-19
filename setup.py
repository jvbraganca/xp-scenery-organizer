import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xp-scenery-organizer",
    version="0.0.1",
    author="João Bragança",
    author_email="jvbragancaa@gmail.com",
    description="A small package to organizer the X-plane's scenery_packs.ini file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvbraganca/xp-scenery-organizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CC BY-NC 4.0  License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)