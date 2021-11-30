import setuptools

setuptools.setup(
    name="tuixdate",
    version="1.0.0",
    author="Ericson Joseph",
    author_email="e.e@juanvizcaino.com",
    description="TUIX Timesheet",
    scripts=['tuixdate'],
    url="https://github.com/ej-coder/tuixdate",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'tabulate'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
