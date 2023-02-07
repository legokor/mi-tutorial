# Python environment

It is recommended to virtual enviroments for your projects so that project dependencies don't get messed up.

There are some popular solutions such as `venv`, `pipenv`, `conda`, and many others. We will cover these later. But for now, stick with `conda`.

Create a conda environment named `mi-tutorial`:
```sh
conda create -n mi-tutorial python=3.9
conda activate mi-tutorial
```

Install all the requirements specified in the `requirements.txt`:
```sh
pip install -r requirements.txt
```

Install our custom package as editable. In this way, we can develop our code in notebooks and `.py` source files in parallel. Our package is easy to use from notebooks without having to deal with path issues.
```sh
pip install -e .
```