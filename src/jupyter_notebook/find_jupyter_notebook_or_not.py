# Title         : Find jupyter kernel or standard python interpreter
# Date Added    : 25 Jun 2019
# Date Modified : 25 Jun 2019
# Reference [1] : https://stackoverflow.com/questions/35595766/matplotlib-line-magic-causes-syntaxerror-in-python-script
# Reference [2] : https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook

def isNotebookFn():
    '''
    Check if code is executed in a Jupyter notebook or not

    Parameters
    ----------
    None

    Return
    ------
    bool - `True` if the code is executed in a Jupyter notebook, otherwise `False`
    '''
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or qtconsole
        else:
            return False # Other type
    except NameError:
        return False     # Other type (Probabably standard python interpreter)

if __name__ == "__main__":
    isNotebook = isNotebookFn()

    if isNotebook:
        print ('The code is executed inside a Jupyter Notebook')

        # <=> %matplotlib inline
        print ('Accessing IPython API and calling `run_line_magic`')
        get_ipython().run_line_magic('matplotlib','inline')
    else:
        print ('The code is not executed inside a Jupyter Notebook')
