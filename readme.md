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

## Starte nytt Django prosjekt
Når django er installert med pip kan en kjøre 
```bash
django-admin startproject PROSJEKTNAVN
```
Da vil Djano sette opp de viktigste filene for deg. Filene som blir laget da er manage.py og alle filene som ligger i app/.

En kan da kjøre
```bash
python manage.py runserver

# Kan også spesifisere ip og port på slutten: 127.0.0.1:8000 for default
```
for å starte opp serveren. Da får man opp Django sin startpage. i terminalen står det at du har unaplied migrations. Det betyr at databasen ikke er satt opp. Om du kjører 
```bash
python manage.py migrate
```
setter du opp en SQlite3 database. Dette er bare en fil (db.sqlite3) og bør bare brukes til utvikling. Denne kan også være lurt å ha i .gitignore.
Du vil også få en mappe __pychache__ som inneholder .pyc filer. Disse er cached kompilerte filer og skal ikke være med i repositoriet. Legg dette inn i .gitignore.

## /admin og urls.py

Etter en har satt opp en database og kjørt migrate kan man gå inn på /admin. Du har ikke brukernavn og passord enda. Dette kan lages med:

```bash
python manage.py createsuperuser
```

Man kan deretter logge inn på admin panelet med den brukeren man lagde. Her er det viktig at en ikke lager bruker dårlige brukernavn/passord.

I filen app/urls.py ser man urlpattern til "admin/". om man endrer "admin/" her til feks "adminpanel/" vil en dette bli den nye stien for adminpanelet.

## settings.py

i app/settings.py er det mye viktig. DEBUG skal alltid være False i production og SECRET_KEY må byttes ut. En grei ting å gjøre er å lese disse fra envirnoment variabler. Dette kan gjøre med dotenv eller decouple. En må da lage en .env fil og legge inn disse verdiene når en skal kjøre server eller laste inn environment variabler på andre måter som gitlab variabler.

En kan også ha ulike filer for settings og spesifisere hvilken du skal bruke når du kjører serveren

```bash
python manage.py runserver --settings=app.settings
```

ALLOWED_HOST sier hvem som kan snakke med serveren.