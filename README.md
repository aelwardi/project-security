## Sécurité du Pipeline (Veille Technologique)
Lors de la mise en place du pipeline, j'ai identifié une alerte de sécurité majeure publiée en mars 2026 concernant l'action `aquasecurity/trivy-action`.

Problème : Les versions antérieures à 0.35.0 ont été compromises par un attaquant (Tag Hijacking) pour voler des secrets dans les environnements GitHub Actions.

Action prise : Bien que l'énoncé suggère la version 0.33.1, j'ai pris la décision d'utiliser la version v0.35.0 qui est certifiée saine et protégée par les nouvelles fonctionnalités d'immuabilité de GitHub.

Résultat : Le pipeline est protégé contre l'exfiltration de données et les secrets Docker Hub restent sécurisés.
