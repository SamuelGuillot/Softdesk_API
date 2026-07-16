# SoftDesk API

## Description

SoftDesk API est une API REST développée avec **Django** et **Django REST Framework** permettant la gestion collaborative de projets, de tickets (*issues*) et de commentaires.

L'application permet de :

* créer et gérer des utilisateurs ;
* créer des projets ;
* ajouter des contributeurs à un projet ;
* créer et suivre des tickets (*issues*) ;
* ajouter des commentaires sur les tickets ;
* sécuriser les accès grâce à l'authentification **JWT (JSON Web Token)**.

Le projet répond aux exigences de sécurité **OWASP**, de protection des données **RGPD** et applique plusieurs principes de **Green Code**.

---

# Technologies utilisées

* Python 3.x
* Django
* Django REST Framework
* Django REST Framework Simple JWT
* SQLite (par défaut)
* Poetry

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/VOTRE_UTILISATEUR/softdesk-api.git
cd softdesk-api
```

## 2. Installer les dépendances

```bash
poetry install
```

## 3. Activer l'environnement virtuel

```bash
poetry shell
```

> Si votre version de Poetry ne prend plus en charge `poetry shell`, vous pouvez exécuter directement les commandes avec `poetry run`.

## 4. Appliquer les migrations

```bash
poetry run python manage.py migrate
```

## 5. Créer un superutilisateur

```bash
poetry run python manage.py createsuperuser
```

## 6. Lancer le serveur

```bash
poetry run python manage.py runserver
```

L'application est accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

---

# Authentification

L'API utilise **JSON Web Token (JWT)**.

## Obtenir un token

```http
POST /login/
```

Exemple de réponse :

```json
{
  "access": "votre_access_token",
  "refresh": "votre_refresh_token"
}
```

Pour accéder aux routes protégées, ajoutez l'en-tête suivant à vos requêtes :

```text
Authorization: Bearer <access_token>
```

---

# Endpoints principaux

## Authentification

| Méthode | Endpoint   | Description          |
| ------- | ---------- | -------------------- |
| POST    | `/signup/` | Créer un utilisateur |
| POST    | `/login/`  | Obtenir un token JWT |

## Projets

| Méthode | Endpoint          |
| ------- | ----------------- |
| GET     | `/projects/`      |
| POST    | `/projects/`      |
| GET     | `/projects/{id}/` |
| PUT     | `/projects/{id}/` |
| PATCH   | `/projects/{id}/` |
| DELETE  | `/projects/{id}/` |

## Contributeurs

| Méthode | Endpoint                            |
| ------- | ----------------------------------- |
| GET     | `/projects/{id}/contributors/`      |
| POST    | `/projects/{id}/contributors/`      |
| DELETE  | `/projects/{id}/contributors/{id}/` |

## Issues

| Méthode | Endpoint                            |
| ------- | ----------------------------------- |
| GET     | `/projects/{id}/issues/`            |
| POST    | `/projects/{id}/issues/`            |
| GET     | `/projects/{id}/issues/{issue_id}/` |
| PUT     | `/projects/{id}/issues/{issue_id}/` |
| PATCH   | `/projects/{id}/issues/{issue_id}/` |
| DELETE  | `/projects/{id}/issues/{issue_id}/` |

## Commentaires

| Méthode | Endpoint                                                  |
| ------- | --------------------------------------------------------- |
| GET     | `/projects/{id}/issues/{issue_id}/comments/`              |
| POST    | `/projects/{id}/issues/{issue_id}/comments/`              |
| PUT     | `/projects/{id}/issues/{issue_id}/comments/{comment_id}/` |
| PATCH   | `/projects/{id}/issues/{issue_id}/comments/{comment_id}/` |
| DELETE  | `/projects/{id}/issues/{issue_id}/comments/{comment_id}/` |

---

# Sécurité

L'API applique plusieurs bonnes pratiques de sécurité :

* authentification via JWT ;
* mots de passe chiffrés par Django ;
* permissions personnalisées avec Django REST Framework ;
* validation des données par les serializers ;
* protection des informations sensibles via des variables d'environnement ;
* suivi des dépendances avec Dependabot.

---

# Conformité RGPD

Le modèle utilisateur comprend :

* un consentement pour être contacté ;
* un consentement pour le partage des données personnelles.

L'inscription est refusée aux utilisateurs de moins de **15 ans**.

Chaque utilisateur peut supprimer définitivement son compte ainsi que ses données personnelles.

---

# Optimisations Green Code

Afin de limiter la consommation de ressources, l'API met en œuvre :

* la pagination des résultats ;
* l'utilisation de `select_related()` et `prefetch_related()` pour optimiser les requêtes SQL ;
* des serializers limitant l'imbrication des ressources ;
* des requêtes ciblées afin de réduire les accès inutiles à la base de données.

---

# Tests

Les principaux tests portent sur :

* l'authentification JWT ;
* les opérations CRUD sur chaque ressource ;
* les permissions selon le rôle de l'utilisateur ;
* la validation des données ;
* les codes de réponse HTTP.

Les tests peuvent être réalisés avec **Postman** ou tout autre client HTTP.

---

## Optimisation des performances avec Django Silk

Afin d'analyser et d'optimiser les performances de l'API, **Django Silk** a été utilisé.

Silk est un outil de profilage qui permet de visualiser les requêtes SQL exécutées, le temps de réponse des vues et les éventuels problèmes de performance, comme le **problème N+1**.

Grâce à cet outil, plusieurs optimisations ont été mises en place :

* utilisation de `select_related()` pour optimiser les relations de type `ForeignKey` ;
* utilisation de `prefetch_related()` pour les relations `ManyToMany` et les relations inverses ;
* réduction du nombre de requêtes SQL exécutées lors de la récupération des ressources.

Après chaque modification, les performances ont été vérifiées avec l'interface de Silk afin de mesurer l'impact des optimisations et de s'assurer que les requêtes étaient exécutées de manière efficace.

L'interface Silk est accessible à l'adresse :

```text
http://127.0.0.1:8000/silk/
```

> **Remarque :** Silk est un outil de développement et ne doit pas être activé en environnement de production.
