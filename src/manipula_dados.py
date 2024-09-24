import pandas as pd
from src.cria_dados import transforma_em_serie

def manipula_serie(serie):
    """
    Soma uma serie em um negócio pronto

    Parameters
    ----------
    serie: pd.Series
        Uma serie pra manipular

    Returns
    -------
    pd.Series:
        Uma serie manipulada :o

    Raises
    ------
    ZeroDivisionError:
        um erro
    """
    return serie.add(transforma_em_serie({"IV": 99999}))
