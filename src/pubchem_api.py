"""
PubChem API utilities.

This module retrieves selected chemical properties
from PubChem PUG REST.
"""

import requests


PUBCHEM_BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"


def get_compound_properties(cid):
    """
    Retrieve selected properties for a PubChem compound.
    """

    url = (
        f"{PUBCHEM_BASE_URL}/compound/cid/{cid}/"
        "property/MolecularFormula,MolecularWeight,InChIKey/JSON"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()
