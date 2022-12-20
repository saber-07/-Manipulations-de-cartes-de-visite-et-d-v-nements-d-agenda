
![Logo](../rsc/logo_vcard_bco.ico)


# Manipulations de cartes de visite et d'évènements d'agenda


Ce projet est réalisé dans le cadre de l’UE Python du Semestre 5 de la L3 Informatique.
Pour ce projet, on doit réaliser une application desktop en python permettant de manipuler des cartes de visites et des évènements d’agenda à l’aide de fichiers « vcf » qui représentent les cartes de visites et de fichiers « ics » qui représentent les agenda. Dans l’application, il sera permis la sélection de carte de visites ou bien d’agenda à partir d’une arborescence parcourue entièrement, aussi la modification, l’enregistrement des modifications sur le fichier et la génération d’une de page HTML valide contenant un fragment de microformats de calendrier et de contact ainsi que la conversion des en fichiers vcf.

L’application qui s’intitulera « V&C Solution » pourra être utilisé en mode console et en mode graphique et assura tous les fonctionnalité demandé dans le cahier de charge.


## Auteur

- [@saber-07](https://github.com/saber-07)


## 🚀 À propos de moi

Je suis Saber Abderrahmane étudiant à CY Cergy Paris Université en Licence 3 informatique


## Installation des bibliothèques requisent

```bash
  pip install vobject
  pip install icalendar
  pip install ics
  pip install prettytable
  pip install tkinter
```
    
  
##  Tests

Pour tester l'app, taper les commandes suivantes

```bash
    python cli.py -h
    python cli.py -d ../rsc
    python cli.py -v ../rsc/john-doe.vcf 
    python cli.py -v ../rsc/john-doe.vcf -t ../rsc/john-doe.html
    python cli.py -v ../rsc/john-doe.vcf -c ../rsc/john-doe.csv 
    python cli.py -i ../rsc/exemple.ics    
    python cli.py -i ../rsc/exemple.ics -c ../rsc/exemple.csv   
    python cli.py -i ../rsc/exemple.ics -t ../rsc/exemple.html
    python gui.py
```


## Documentation

[Documentation](doc/html/index.html)

