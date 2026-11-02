from typing import Optional
from rdkit import Chem


def mol2_to_smiles(mol2_file_path: str, isomeric=True) -> Optional[str]:
    mol = Chem.MolFromMol2File(mol2_file_path, sanitize=True, removeHs=True)

    if mol is None:
        return None

    # Convert the molecule object to Canonical SMILES
    smiles = Chem.MolToSmiles(mol, isomericSmiles=isomeric)

    return smiles