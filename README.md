# Bot Agenda Discord

Ce bot Discord offre une fonctionnalité d'agenda simple pour afficher les créneaux horaires quotidiens et interagir avec les utilisateurs via des réactions.

## Fonctionnalités

- **!agenda** : Affiche la date du jour et les créneaux horaires disponibles.
- **!message [contenu]** : Envoie un message personnalisé dans le canal avec des options de réaction.

## Commandes

### !agenda
Affiche l'agenda du jour avec les créneaux horaires disponibles. Les utilisateurs peuvent mentionner un rôle spécifique avec l'agenda.

### !message [contenu]
Envoie un message personnalisé dans le canal avec des options de réaction (✅ ou ❌).

## Configuration

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Kevin-LB/bot-agenda-discord.git
   ```

2. **Lancer le Bot**
   ```bash
   python main.py
   ```

## Prérequis

- Python 3.6+
- Bibliothèque `discord.py`
- `python-dotenv` (pour la gestion des variables d'environnement)

## Utilisation

1. Invitez le bot sur votre serveur Discord en utilisant l'URL OAuth2 générée pour votre application.
2. Assurez-vous que le bot dispose des autorisations nécessaires.
3. Utilisez les commandes fournies (`!agenda`, `!message`) dans les canaux désignés pour interagir avec le bot.
