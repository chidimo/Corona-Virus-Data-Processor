# Corona Virus Data Processor

Process data from <https://covid.ourworldindata.org/data/ecdc/full_data.csv>

1. Create a new folder and `cd` into it.
1. Run `pipenv install` to nitialise a new virtualenv inside
1. Activate the virtualenv with `pipenv shell`
1. Add `README`, `.gitignore`, `.editorconfig`
1. Create a custom `ipython` kernel for this environment. We need to work with juypter notebook. See help [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments)

    1. `pipenv install jupyter ipykernel`
    1. `python -m ipykernel install --user --name py37corona --display-name "Python37corona"`
    1. Run `jupyter notebook` to spin up an `ipython` kernel.
    1. List all kernels: `jupyter kernelspec list`
    1. Delete a kernel `jupyter kernelspec uninstall <kernel-name>`
1. Install `mongoengine` and `dnspython` with `pipenv install mongoengine dnspython`
