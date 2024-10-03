# Backend d'un site à ..................

## Prérequis

- Python 3.8+
- FastAPI
- PostgreSQL

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/kekelidiane/Stage-EPL/Backend-with-FastAPI.git
    ```

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv env
    source env/bin/activate  # Sur Windows : `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```
    
4. Configurez les variables d'environnement. Créez un fichier `.env` à la racine du projet et ajoutez les variables suivantes :
    ```env
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

## Démarrage du Serveur
    Pour démarrer le serveur de développement :
    
    ```bash
    uvicorn app.main:app --reload

## Exécution des Tests

Pour excécuter les futurs tests, utilisez:
    ``` 
    pytest
    ```

## Structure du projet

Confère projet

## Documentation de l'API
Pour accéder à la documentation interactive de l'API, démarrez le serveur et ouvrez votre navigateur aux adresses suivantes :

- Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contribution

Les contributions sont les bienvenues !