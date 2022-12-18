from setuptools import Extension, setup
from torch.utils import cpp_extension

setup(
    name="homemade_linear",
    version="0.1",
    description="A homemade reproduction of nn.Linear in C++",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    url="https://github.com/fxmarty/homemade-linear",
    author="Felix Marty",
    license="MIT",
    install_requires=["torch"],
    ext_modules=[
        cpp_extension.CppExtension(
            "homemade_linear._CPP",
            ["homemade_linear/linear.cpp", "homemade_linear/bindings.cpp"],
        )
    ],
    cmdclass={"build_ext": cpp_extension.BuildExtension},
    python_requires=">=3.7.0",
    zip_safe=False,
)
