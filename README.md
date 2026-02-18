# Documentation : Mise en place d'une CI Python avec Pytest

Ce guide récapitule la configuration nécessaire pour automatiser vos tests unitaires via GitHub Actions.

## 1. Structure du Projet
Pour que Python et Pytest communiquent correctement, respectez cette hiérarchie :
```
	.
	├── .github/workflows/unit_test_ci.yml
	├── src/
	│   └── operations/
	│       ├── __init__.py
	│       ├── addition.py
	│       └── ...
	├── tests/
	│   └── operations_test.py
	└── pyproject.toml
```

## 2. Configuration du Python Path
Le fichier `pyproject.toml` à la racine est crucial. Il indique à Pytest que le code source se trouve dans le dossier `src`.
	
	[tool.pytest.ini_options]
	pythonpath = ["src"]

## 3. Développement d'une fonction

Admettons le code suivant permettant d'effectuer une addition des 2 arguements.

```python
# Exemple dans src/operations/addition.py
def add(a: int, b: int):
    return a + b
```


## 4. Écriture des Tests
Les fichiers de tests doivent se trouver dans le dossier `tests/` et leurs noms (ainsi que les fonctions) doivent commencer par `test_`.

```python
	# Exemple dans tests/operations_test.py
	from operations.addition import add

	def test_addition_2_plus_2():
	    assert add(2, 2) == 4
```

## 5. Automatisation avec GitHub Actions
Le workflow suivant déclenche les tests à chaque Pull Request vers la branche `main`. Il simule un environnement Ubuntu, installe les dépendances et lance Pytest.

```yml
# Contenu de .github/workflows/unit_test_ci.yml
name: Unit test - CI
on:
  pull_request:
    branches: [main]

jobs:
  operations_testing:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install Pytest
        run: |
          python -m pip install --upgrade pip
          pip install pytest
      - name: Run Tests
        run: python3 -m pytest
```

## 6. Astuces & Bonnes Pratiques
- Commande locale : Utilisez toujours `python3 -m pytest` pour éviter les conflits de PATH.
- `__init__.py`  : Laissez ce fichier (même vide) dans vos sous-dossiers de `src` pour les transformer en packages Python.
- Évolutivité : Si vous ajoutez des bibliothèques externes (numpy, pandas, etc.), créez un fichier `requirements.txt` et installez-le dans le YAML avec `pip install -r requirements.txt`.