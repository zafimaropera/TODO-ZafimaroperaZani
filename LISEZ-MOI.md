Projet Django: Liste de tâches avec AJAX
Dans ce projet, nous allons développer une liste de tâches avec Django et découvrir la puissance d'AJAX pour rendre les choses plus dynamiques.

*** Avant tout ça! Installer d'abord Django avec cet code : " pip install django " dans votre machine s'il n'y avais pas!

*** Premièrement, vous allez diriger dans le repertoire avec cet code sur le terminal " cd .\DjangoProjet-ToDoList\ " et lancer là.

*** Avant de lancer ce projet, il y a quelque configuration et quelque étapes à suivre dans le terminal du VS code comme ceci :
1 - Dans le terminal vous allez taper cet code " pip install -r requirements.txt " mais comme le faire :
" PS C:\Users\User\Desktop\DjangoProjet ToDoList\DjangoProjet-ToDoList> pip install -r requirements.txt " et lancer là.

2 - Après avoir taper requirements, vous allez ensuite faire une migration à la base avec cet code, toujours au terminal : " python manage.py migrate " et lancer là.

3 - Après avoir lancer la migration, vous allez créer une compte super user de django avec cet code : " python manage.py createsuperuser " et vous allez suivre ce que le terminal vous conduit.

*** Après avoir effectué les configurations initiales. Maintenant, nous allons lancer et exécuté le projet avec cet code : " python manage.py runserver ".

NB : /* Faire cette étape si l'application de fonction pas correctement chez vous, s'il vous plaît! */
Après avoir lancer le projet, vous allez dans le volet de votre navigateur. Vous tapez ceci dans volet de votre navigateur, on écrivons : " 127.0.0.1:8000/admin/ " et lancer là. Une fois dans administrateur de Django, vous allez enter votre identifiant (Votre nom d'utilisateur et votre mot de passe ) de votre super user que vous avez créer avant comme suis, voilà le mien : " Nom d'utilisateur : Zani et Mot de passe : 1234 ". vous allez dans statuss de MYAPP et ajouter ceci un à un comme je les avais écris avec leur petit logo s'il vous plaît : "⛔️ À Faire, ⚠️ En Cours et ✅ Terminé"

*** Après avoir enregistrer le statuss, vous allez revenir dans le projet en supprimant " /admin " derrière " 127.0.0.1:8000 " et lancer là. Vous pouvez maintenant utiliser le projet.

*** Utilisation :
- (Ajout tâche) Entre dans la case titre votre tâche et enregistre là avec le bouton verte qui a une petite plus de dans.

- (Modifier tâche) Cliquer sur la tâche que vous avez écris, il y a une case de modification s'ouvre après, modifie là et enregistrer votre modification avec le bouton jaune qui a une petite icon stylet à droite.

- (Supprimer le tâche) Cliquer sur le bouton rouge supprimer qui a une petite icon poubelle à droite.