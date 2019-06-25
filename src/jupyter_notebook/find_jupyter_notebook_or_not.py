def isNotebookFn():
    '''
    Check if code is executed in a Jupyter notebook or not

    Parameters
    ----------
    None

    Return
    ------
    bool - True if the code is executed in a Jupyter notebook
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
    else:
        print ('The code is not executed inside a Jupyter Notebook')
