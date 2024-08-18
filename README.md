# Backend du site de l'EPL

Le projet consiste à concevoir, créer et développer le site web pour l'École Polytechnique de Lomé (EPL) afin de communiquer sur les activités du service administratif de l'école.

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
- PostgreSQL
- [Poetry](https://python-poetry.org/)

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/kekelidiane/Backend_site.git
    cd Backend_site
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
    Ou, si vous utilisez Poetry :
    ```sh
    poetry install
    ```

4. Configurez les variables d'environnement. Créez un fichier `.env` à la racine du projet et ajoutez les variables suivantes :
    ```env
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

5. Initialisez la base de données :
    ```sh
    alembic upgrade head
    ```

## Gestion des Migrations de Base de Données avec Alembic

### 1. **Info**

[Alembic](https://alembic.sqlalchemy.org/en/latest/) est un outil de gestion des migrations pour SQLAlchemy, utilisé pour gérer les changements dans le schéma de base de données de manière versionnée. Dans ce projet, Alembic est utilisé pour suivre et appliquer les modifications apportées aux modèles SQLAlchemy.

### 2. **Installation**

Assurez-vous d'avoir Alembic installé dans votre environnement virtuel. Vous pouvez l'installer via pip :

    ```sh
    pip install alembic
    ```	

### 3. **Configuration d'Alembic**

Le fichier de configuration `alembic.ini` contient les paramètres de connexion à votre base de données. Assurez-vous que les paramètres suivants sont correctement configurés :

   [alembic]
   script_location = alembic
   sqlalchemy.url = postgresql+asyncpg://user:password@localhost/dbname

### 4. **Utilisation**

1. **Créer une Nouvelle Migration**

   Pour générer un nouveau fichier de migration en fonction des modifications apportées aux modèles, utilisez :

   ```bash
   alembic revision --autogenerate -m "Description de la migration"

2. **Appliquer les Migrations**

    Pour appliquer les migrations à la base de données, utilisez :

    ```bash
    alembic upgrade head

3. **Revenir à une Migration Précédente**

    Si vous devez annuler les migrations, vous pouvez revenir à une révision précédente en utilisant :

    ```bash
    alembic downgrade <revision>


### 5. **Conseils de Débogage**

Ajoutez une section sur le débogage des erreurs courantes que vous pourriez rencontrer lors de l'utilisation d'Alembic.

```markdown
## Débogage

Si vous rencontrez des problèmes avec les migrations, vérifiez les éléments suivants :

- **Configuration de la Base de Données** : Assurez-vous que les informations de connexion dans `alembic.ini` sont correctes.
- **MetaData** : Vérifiez que `target_metadata` dans `env.py` est correctement configuré avec vos modèles SQLAlchemy.
- **Journalisation** : Consultez les journaux pour des messages d'erreur spécifiques lors de l'exécution des commandes Alembic.


## Démarrage du Serveur
    Pour démarrer le serveur de développement :
    ```sh
    uvicorn app.main:app --reload
    ```	

## Exécution des Tests

Pour excécuter les futurs tests, utilisez:
    ```sh
    pytest
    ```

## Structure du projet

Confere projet

## Documentation de l'API


Pour accéder à la documentation interactive de l'API, démarrez le serveur et ouvrez votre navigateur aux adresses suivantes :

- Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contribution

Les contributions sont les bienvenues !

## License

Pas encore définie