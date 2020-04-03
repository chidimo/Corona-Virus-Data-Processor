# Corona

1. Create folder and initialise a new virtualenv inside with `pipenv install`
1. Activate the virtualenv with `pipenv shell`
1. Add `README`, `.gitignore`, `.editorconfig`
1. Create an `ipython` kernel inside this folder. We need to work with juypter notebook. See help [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments)

    1. `pipenv install jupyter ipykernel`
    1. `python -m ipykernel install --user --name py37corona --display-name "Python37corona"`
    1. Run command `jupyter notebook` to spin up an `ipython` kernel.
    1. Get a list of all kernels `jupyter kernelspec list`
    1. Delete a kernel `jupyter kernelspec uninstall <kernel-name>`
1. Install `pipenv install mongoengine dnspython`

Flags: <https://www.countryflags.io/>
