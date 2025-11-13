# 🏆 Projet : Pipeline d'IA pour l'Analyse et la Réponse de Tickets Clients Multilingues

## 🧠 Architecture Modulaire

Ce projet implémente une solution de **Fine-Tuning (LoRA)** pour automatiser le triage et la réponse sur un corpus multilingue (FR, EN, ES, DE, PT).

- **Triage (XLM-R)** : Classification multi-classe (10 départements).
- **Génération (T5-Small + LoRA)** : Utilisation de la technique **PEFT** pour la création de brouillons de réponse, prouvant la gestion des contraintes VRAM/GPU.

[Ajoutez votre meilleur score F1 ici]

## 🛠️ Exécution

Le code source se trouve dans `notebooks/01_FineTuning_Pipeline.ipynb`.
