## Sécurité du Pipeline (Veille Technologique)
Lors de la mise en place du pipeline, j'ai identifié une alerte de sécurité majeure publiée en mars 2026 concernant l'action `aquasecurity/trivy-action`.

Problème : Les versions antérieures à 0.35.0 ont été compromises par un attaquant (Tag Hijacking) pour voler des secrets dans les environnements GitHub Actions.

Action prise : Bien que l'énoncé suggère la version 0.33.1, j'ai pris la décision d'utiliser la version v0.35.0 qui est certifiée saine et protégée par les nouvelles fonctionnalités d'immuabilité de GitHub.

Résultat : Le pipeline est protégé contre l'exfiltration de données et les secrets Docker Hub restent sécurisés.

### Activation de GitHub Code Scanning
Lors de la première exécution, le job `upload` a échoué car le Code Scanning n'était pas activé par défaut sur le dépôt. Après avoir activé cette fonctionnalité dans les réglages de sécurité de GitHub et configuré la permission `security-events: write`, le pipeline a pu publier les vulnérabilités détectées par Trivy directement dans l'interface GitHub.
