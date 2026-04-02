## Sécurité du Pipeline (Veille Technologique)
Lors de la mise en place du pipeline, j'ai identifié une alerte de sécurité majeure publiée en mars 2026 concernant l'action `aquasecurity/trivy-action`.

Problème : Les versions antérieures à 0.35.0 ont été compromises par un attaquant (Tag Hijacking) pour voler des secrets dans les environnements GitHub Actions.

Action prise : Bien que l'énoncé suggère la version 0.33.1, j'ai pris la décision d'utiliser la version v0.35.0 qui est certifiée saine et protégée par les nouvelles fonctionnalités d'immuabilité de GitHub.

Résultat : Le pipeline est protégé contre l'exfiltration de données et les secrets Docker Hub restent sécurisés.

### Activation de GitHub Code Scanning
Lors de la première exécution, le job `upload` a échoué car le Code Scanning n'était pas activé par défaut sur le dépôt. Après avoir activé cette fonctionnalité dans les réglages de sécurité de GitHub et configuré la permission `security-events: write`, le pipeline a pu publier les vulnérabilités détectées par Trivy directement dans l'interface GitHub.

## Implémentation des Mesures de Sécurité (Résolution des Vulnérabilités Trivy)
Afin de valider efficacement notre pipeline CI et les capacités d'analyse de Trivy, j'ai délibérément introduit dans un premier temps des versions vulnérables de nos dépendances applicatives :

* **Avant** (`flask==1.1.1`, `jinja2==2.10.1`, `werkzeug==0.15.5`) : Trivy a correctement identifié plusieurs vulnérabilités de criticité Élevée (CRITICAL, HIGH), confirmant le déclenchement des alertes dans l'onglet Security > Code Scanning.

* **Après** (Action de mitigation) : La mesure de sécurité implémentée a été la mise à jour complète de l'arbre des dépendances vers des versions saines et patchées, ce qui a drastiquement assaini l'image Docker finale. Les bibliothèques corrigées sont :
  * `flask>=3.0.3`
  * `jinja2>=3.1.4`
  * `werkzeug>=3.0.3`

### Configuration de l'environnement de Test (Pytest)
Pendant la phase de CI, nous avons rencontré une `ModuleNotFoundError`. Nous avons résolu ce problème de configuration d'environnement en définissant la variable `PYTHONPATH=.` dans le workflow GitHub Actions, permettant ainsi à Pytest de localiser correctement le module principal de l'application Flask.

### Tableau de Remédiation des Vulnérabilités (Trivy & Dependabot)
En plus de Trivy, l'activation de Dependabot a permis de détecter et mapper précisément les failles connues sur les dépendances du projet :

| Librairie | Faille détectée | Gravité | Action corrective |
| :--- | :--- | :--- | :--- |
| Werkzeug | Remote Code Execution (Debugger) | Haute | Mise à jour vers v3.0.3 |
| Jinja2 | Sandbox Breakout (SSTI) | Moyenne | Mise à jour vers v3.1.4 |
| Flask | Session Cookie Vulnerability | Faible | Mise à jour  vers v3.0.3 |

### Conclusion
Grâce à la mise en place de ce pipeline CI/CD, nous avons pu identifier des vulnérabilités critiques via Trivy et Dependabot. L'application a été sécurisée en mettant à jour les dépendances et en corrigeant les fonctions Flask vulnérables (SQLi, SSTI). Le projet est maintenant déployé de manière automatisée et sécurisée via Docker.
