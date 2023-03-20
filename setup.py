from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dvc_DL_TF_experiment",
    version= "0.0.1",
    author= "AAZZIOUI",
    description= "A small package for dvc DL TensorFlow demo",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    url= "https://github.com/AAZZIOUI/dvc_ml_tf",
    author_email="anas.azzioui@gmail.com"
    packages=["src"],
    license= "GNU",
    python_requires= ">=3.10",
    install_requires= [
        'dvc',
        'pandas',
        'tensorflow',
        'matplotlib',
        'numpy',
        'tqdm',
        'pyYAML',
        'boto3',
    ]
)