# NTLM Password Spraying Tool

**Auteur : 0xgh05t**
**Version : 1.0**
**Licence : MIT**

---

## Description

Le script NTLM Password Spraying est un outil Python conçu pour effectuer des tests de sécurité sur les services SMB via le protocole NTLM (NetNTLM). Son principal objectif est d'automatiser l'identification rapide de comptes utilisateur valides en testant un seul mot de passe sur une liste d'utilisateurs, minimisant ainsi les risques de verrouillage de compte.

---

## Fonctionnalités

* **Automatisation des tentatives d'authentification SMB via NTLM**
* **Mode verbose pour affichage temps réel des tentatives**
* **Présentation claire et concise des résultats**
* **Prise en charge d'adresses IP et de domaines FQDN**

---

## Dépendances

Ce script requiert :

* Python 3.x
* [Impacket](https://github.com/SecureAuthCorp/impacket)

Installation rapide :

```bash
pip install impacket
```

---

## Installation

Clonez simplement ce dépôt GitHub :

```bash
git clone <url-de-votre-dépôt>
cd ntlm-password-spraying
```

---

## Utilisation

Syntaxe générale :

```bash
python ntlm_spray.py -u <fichier_utilisateurs> -f <fqdn> -p <mot_de_passe> -t <IP_ou_hostname> [-v]
```

### Paramètres :

* `-u`, `--userfile` : Chemin vers le fichier contenant la liste d’utilisateurs
* `-f`, `--fqdn` : Domaine cible complet (ex : `example.local`)
* `-p`, `--password` : Mot de passe à tester
* `-t`, `--target` : Adresse IP ou hostname de la cible SMB
* `-v`, `--verbose` (optionnel) : Affichage détaillé en temps réel

---

## Exemple

```bash
python ntlm_spray.py -u users.txt -f example.local -p "Password123" -t 192.168.1.10 -v
```

---

## Capture d'écran

![image](https://github.com/user-attachments/assets/d2f90bd9-6b63-4c97-836c-36948a07aea3)

---

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Avertissement

Ce script est uniquement destiné à des fins éducatives et de tests de sécurité. Son utilisation doit être strictement limitée à des environnements et systèmes pour lesquels vous avez une autorisation explicite. L'auteur ne saurait être tenu responsable d'une mauvaise utilisation de cet outil.
