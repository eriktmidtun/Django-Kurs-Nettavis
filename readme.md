# Nettavis Django backend

Dette prosjektet er ment å være et kurs i git, django og API, men at man også kan bruke det på De nyes dag for å gjøre samarbeid med de som skriver artikler lettere.

## Requirements

Python3 og pip3

## Virtualenvironment
For å håndtere pakker med ulike versjoner på ulike prosjekter med python kan en bruke virtualenvironment

```bash
pip3 install virtualenv
```

Aktiver virtuelenvironment
```bash
#For Windows

virtualenv venv                      
venv\Scripts\activate                
```
```bash
#For Mac/Linux

virtualenv -p python3 venv          
venv/bin/activate                 
```

Om man da sjekker hvilke pakker man har installert skal listen være tom. Dette kan en sjekke med :

```bash
pip list
```
For å laste ned nye pakker kan man bruke kommandoen vi brukte over. Om en skal laste ned Django kan man da kjøre
```bash
pip install Django
```
For å installere pip pakker en allerede bruker i et prosjekt kan en bruke requirements.txt som referanse.

```bash
pip install -r requirements.txt
```

For å lage en requirement.txt fil bruker man kommandoen:

```bash
pip freeze > requirements.txt
```
Da vil alle pakker du har installert på det utviklingsmiljøet du er i komme med i txt filen.

Vi vil ikke ha med alle ekstra pakkene i git koden vår så vi legger inn "venv/" i .gitignore filen slik at den blir ignorert av git.