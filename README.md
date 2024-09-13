# Backend du site de l'EPL

Developpement du backend du site web de l'École Polytechnique de Lomé (EPL)

## Fonctionnalités

- **[FastAPI](https://fastapi.tiangolo.com/)** (Python 3.8)
- **[PostgreSQL](https://www.postgresql.org/)** pour la base de données
- **[SqlAlchemy](https://www.sqlalchemy.org/)** pour l'ORM

## Fonctionnalités

- Support informatif sur la structure institutionnelle et l'organisation
- Support informatif sur les programmes de formation et les cours
- Support informatif sur les procédures de recrutement et les concours
- Support informatif sur la vie et les activités sur le campus
- Support informatif sur les partenaires académiques nationaux et internationaux
- Support informatif sur les partenaires commerciaux nationaux et internationaux
- Support informatif sur la recherche, l'innovation, le transfert et les services
- Accès à un espace extranet réservé aux ressources internes
- Interface de dialogue et de partage d'expériences ou de témoignages avec les étudiants en mobilité (blog et forums)
- Interface de collecte de données des nouveaux candidats (formulaire de contact)
- Gestion du calendrier partagé, y compris la gestion des calendriers de groupe par e-mail ou en collaboration avec les opérateurs télécoms (par SMS)
- Back office pour le suivi des activités du site (récupération des formulaires, mise à jour des listes de diffusion, téléversement de documents et de ressources partenaires, etc.)
- Intégration avec les systèmes tiers (comptes de réseaux sociaux de l'EPL)
- Messagerie électronique pour le personnel de l'EPL (gestion des comptes EPL)
- Annuaire, support technique interne

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

## License

Pas encore définie