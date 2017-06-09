from setuptools import setup


if __name__ == "__main__":

    with open('README.md', 'r') as f:
        long_description = f.read()

    setup(
        name="cigam",
        version="0.0.1",
        description=("magic"),
        py_modules=["cigam"],
        keywords="",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Utilities",
        ],

        author="mikusjelly",
        author_email="mikusjelly@gmail.com",
        url="https://github.com/mikusjelly/cigam",

    )
