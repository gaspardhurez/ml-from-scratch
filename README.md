# ml-from-scratch

**Un projet pédagogique pour implémenter les fondations du Machine Learning en pur Python, sans bibliothèque externe.**

Ce dépôt contient une série d’implémentations construites étape par étape, dans le but de comprendre en profondeur les mécanismes des algorithmes de machine learning. Chaque module est accompagné de notes théoriques et de scripts d'expérimentation.

---

## 📦 Contenu du projet

Le projet couvre progressivement les éléments suivants :

- Opérations d’algèbre linéaire (vecteurs, matrices, projections…)
- Transformations de données (normalisation, encodage, PCA…)
- Fonctions coût et optimisation (MSE, log loss, descente de gradient…)
- Modèles linéaires (régression, classification…)
- Réseaux de neurones simples (propagation avant et arrière)

---

## 🗂️ Structure
ml-from-scratch/
│
├── algebra/            ← Algèbre linéaire (vecteurs, matrices, géométrie)
├── preprocessing/      ← Manipulations et transformations de données
├── core/               ← Fonctions coût, optimisation, utilitaires
├── models/             ← Modèles ML linéaires
├── networks/           ← Réseaux de neurones simples (ANN)
├── notes/              ← Résumés théoriques en markdown
└── playgrounds/        ← Scripts d’expérimentation

---

## ⚙️ Stack technique

- Python 3.x uniquement
- Pas de dépendances externes (implémentation en Python brut)