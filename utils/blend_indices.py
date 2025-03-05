import numpy as np
from typing import List, Dict

def celcius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celcius(f):
    return (f - 32) * 5/9

### Reid vapor pressure 

def rvpi(rvp):
    return np.power(rvp, 1.25)

def inv_rvpi(rvpi):
    return np.power(rvpi, 1.0/1.25)

### Pour Point Index

def ppi(pp):
    ppc = fahrenheit_to_celcius(pp)
    term1 = (ppc + 273.15) / 283.15
    term2 = np.multiply(term1, 100**0.08)
    return np.power(term2, 12.5)

def inv_ppi(ppi):
    return (283.15*((ppi/100)**0.08) - 273.15) * 1.8 + 32


### viscosity index

def vbi(v):

    assert np.all(v > 0.2)

    vbi = np.log10(np.log10(v + 0.8))
    return vbi


def inv_vbi(vbi):
    vb = np.power(10, np.power(10, vbi)) - 0.8
    return vb


### API/specific gravity index

def sg(api):
    return np.divide(141.5, 131.5 + api)

def api(sg):
    return np.divide(141.5, sg) - 131.5


blend_indices = {
    "vis100f": {
        "index_name": "vis100f_idx",
        "func": vbi,
        "inv_func": inv_vbi
    },
    "rvp": {
        "index_name": "rvp_idx",
        "func": rvpi,
        "inv_func": inv_rvpi
    },
    "pour": {
        "index_name": "pour_idx",
        "func": ppi,
        "inv_func": inv_ppi
    },
    "api": {
        "index_name": "sg",
        "func": sg,
        "inv_func": api
    }
}


def process_quality_constraints(constraints: Dict[str, List[float]]) -> Dict[str, List[float]]:
    """_summary_

    Parameters
    ----------
    constraints : Dict[str, List[float]]
        _description_

    Returns
    -------
    Dict[str, List[float]]
        _description_
    """

