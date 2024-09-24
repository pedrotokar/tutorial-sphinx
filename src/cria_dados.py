"""Modulo que trata de dados"""

import pandas as pd

def transforma_em_serie(dictionary):
    """
    Transforma um dicionario em dataframe

    Parameters
    ----------
    dictionary: dict
        o dicionario para transformar em dataframe

    Returns
    -------
    pd.Series
        A serie feita.

    Raises
    ------
    ZeroDivisionError:
        quando você passa um zero sei lá
    """
    return pd.Series(dictionary)
