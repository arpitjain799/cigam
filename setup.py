from setuptools import setup


if __name__ == "__main__":

    with open('README.rst', 'r') as f:
        long_description = f.read()

    setup(
        name="magic",
        version="0.0.2",
        description=("magic"),
        py_modules=["magic"],
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
        url="https://github.com/mikusjelly/magic",

    )
