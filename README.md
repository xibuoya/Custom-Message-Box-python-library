# Custom Message Box library

Une bibliothèque simple et moderne pour créer des boîtes de dialogue personnalisées avec **CustomTkinter**. Elle permet de récupérer facilement des réponses utilisateur (saisies, confirmations, choix multiples) sans avoir à manipuler des classes complexes.

## 📦 Fonctionnalités

- **Information & Erreur** : Notifications simples.
- **Yes/No** : Boîte de dialogue de confirmation.
- **Entry** : Boîte de dialogue avec saisie de texte.
- **Custom** : Boîte de dialogue de 2 ou 3 boutons personnalisés.

## 🛠 Installation

Assurez-vous d'avoir installé CustomTkinter :

```bash
pip install customtkinter
```

Installer la librairie : 

```bash
pip install custom_message_box
```

## Utilisation
Guide d'utilisation rapide :
- **Message d'Information**(ctkinfo)
    ```python
    ctk_msg.ctkinfo("Titre", "Opération réussie !")
    ```

- **Message d'Erreur** (ctkerror)
    ```python
    ctk_msg.ctkerror("Attention", "Connexion perdue.")
    ```

- **Fenêtre de Confirmation** (ctk_msg_yesno)
Renvoie 1 pour Oui et 0 pour Non.
    ```python
    reponse = ctk_msg.ctk_msg_yesno("Quitter", "Voulez-vous vraiment partir ?")
    ```

- **Saisie de text** (ctk_msg_entry)
Renvoie la chaîne de caractères saisie.
    ```python
    pseudo = ctk_msg.ctk_msg_entry("Pseudo", "Entrez votre nom :", "Ex: Jean")
    ```

- **Boutons personnalisés** (ctk_msg_custom)
Renvoie le texte du bouton cliqué.
    ```python
    choix = ctk_msg.ctk_msg_custom("Menu", "Choisir :", 3, "Jouer", "Options", "Quitter")
    ```

### Exemple complet d'intégration

```python
import customtkinter as ctk
import ctk_msg

 def demo():
nom = ctk_msg.ctk_msg_entry("Login", "Ton nom :", "Pseudo...")
if nom:
conf = ctk_msg.ctk_msg_yesno("Salut", f"Tu es bien {nom} ?")
if conf == 1:
ctk_msg.ctkinfo("Succès", "Profil validé !")

app = ctk.CTk()
btn = ctk.CTkButton(app, text="Lancer Test", command=demo)
btn.pack(pady=50)
app.mainloop()
```
