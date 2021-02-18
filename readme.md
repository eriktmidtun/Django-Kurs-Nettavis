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

Eksempel .env:
```bash
#.env

DEBUG=True
SECRET_KEY='fiojeaiofjoaekf0+0I9I98FU4RJKFA9EJF94AJF'
```
En kan også ha ulike filer for settings og spesifisere hvilken du skal bruke når du kjører serveren

```bash
python manage.py runserver --settings=app.settings
```

ALLOWED_HOST sier hvem som kan snakke med serveren.

## Django-admin startapp

om man kjører kommandoen

```bash
django-admin startapp APP-NAVN
```
lager django en ny app (eller python package) som fungerer som en modul.
Her er det viktig å legge inn den nye appen du lagde i settings.py i listen INSTALLED_APPS

Django lager da en ny mappe med appnavnet ("nettavis") og legger til en del filer.
models.py er hvor en definerer django sine database modeller.
En burde bruke django sine modeller istedenfor å bruke egne SQL queries. Dette er mer sikkert og det gjøre det enklere å bruke og bytte mellom databasetyper.

For å bruke de nye modellene må en få django til å opprette databasetabeller for deg. 
```bash
python manage.py makemigrations
```
Dette legger nye migration filer i nettavis/migrations
For å utføre disse migrations kjører en 
```bash
python manage.py migrate
```
Da er det laget en tabell med navn artikkel i databasen. Per nå har vi ingen måte å opprette nye artikkler eller se eksisterende.

For å gi mulighet for å opprette/slette/redigere artikler i admin panelet må vi registrere modellen i filen admin.py.

### Laste opp bilder
Om vi prøver å laste opp et bilde i adminpanelet vil vi få en feil. Dette er fordi vi ikke har satt opp urlpattern for statiske filer eller opplastninger. Vi kan legge til url patterns for statiske filer i urls. vi kan også sette hvor vi vil at opplastede filer skal lagres i settings med MEDIA_ROOT.

## Django Templates
Django har et eget språk for å generere HTML filer dynamisk. For å bruke dette må en opprette en mappestruktur med html filer inne i appen du vil lage template for. For oss blir det "nettavis/templates/nettavis/index.html". Må så si hvor templates ligger i settings TEMPLATES DIRS. I filen views.py definerer vi en view som tar inn en request og returnerer en html-fil. For at vi skal kunne komme til denne filen må vi oppdatere url patterns i app/urls.py med viewet vi nettop laget.

### Rendre ting fra databasen med django templates
For å rendre ting feks en artikkel fra databsen i django tamplates må man legge dette til i views.py ved å importere modellen som et object du har lyst å rendre fra og legge den til i render kallet. I templates kan man så bruke Django template languages for å rendre alle modellene. Man kan bruke "{% for artikkel in artikler.all %} HTML og DJANGO KODE HER{% endfor %}" for å loope igjennom all artikler og en vise tittelen til en artikkel med {{artikkel.tittel}}.

### Legge til css og andre statiske filer.
Man kan legge til statiske filer som css og logo ved å lage en mappe kalt static/ og legge disse filene inni her. Registrer denne mappen i STATICFILES_DIRS i settings.py og legg til STATIC_ROOT. STATIC_ROOT er mappen django henter filene fra når serverer kjøres. i templates må du loaded static i starten med {% load static %} og man kan da kalle på statiske filer i href med feks: href="{% static 'styles.css' %}.

### Flere urls.py filer
Det kan være lurt å flytte url logikken fra en django app inn i den appen urlen skal brukes i. I hoved urls.py filen kan man bruke "from django urls import include" og bytte ut view og name med include('nettavis.urls'). Da kan man lage en urls.py i nettavis/ som inneholder de urlene man vil bruke i den appen. dette gjør at vi lett kan bygge videre på urlen /nettavis/ med feks /nettavis/1/ for å vise den første artikkel.

### Dynamiske urler basert på modeller
Om man skal rendre en arikkel basert på id-en i databasen må man først legge dette til i urlpatterns i nettavis/urls.py. Dette kan gjøre med '<int:artikkel_id>/' som url hvor artikkel_id er det som blir videresendt til viewet man spesifiserer. Dette blir da en parameter i viewet.

```python
def artikkel_template(request, artikkel_id):
    artikkel = get_object_or_404(Artikkel, pk=artikkel_id)
    return render(request,'artikkel.html', {'artikkel': artikkel})
```
Django har en annen shortcut en render som heter get_object_or_404. Denne sender returnerer objektet eller en 404 response om objektet man spør etter ikke eksisterer. Ellers er det bare å rendere en artikkel på samme måte som med alle artiklene.

### Formatering av objekter.
Om man skal ha dato fra et objekt/modell som bruker DateTimeField får man nødvendigvis ikke datoen på formatet man vil. Man kan da lage metoder i modellen for å hjelpe. formater_publisert i models.py returnerer en formatert dato på string format. Man kan kalle på disse i Django templates med {{artikkel.formater_publisert}} istedenfor {{artikkel.publisert}}.

## Bruke andre pakker
Det finnes extensions og pakker/moduler som kan brukes for nesten hva som helst. Hvordan disse legges til avhenger av pakken, men en vanlig ting man må gjøre er å laste ned med pip og legge den itl i requirements.txt og legge til pakken i INSTALLED_APPS i settings.py. Et eksempel er What you see is what you get editoren Django-summernote for å gi mer muligheter for å formatere brødteksten.

## Lage GraphQL API
Å lage grapql api med django er ganske lett. installer graphene-django med pip og i INSTALLED_APPS. Lag ny django app med 
```bash
django-admin startapp graphqlApi
```
og slett autogenerete filer du ikke trenger som graphqlApi/models.py,  graphqlApi/admin.py ,graphqlApi/apps.py, graphqlApi/views.py og mappen migrations.

Lag en graphqlApi/urls.py og include denne i app/urls.py. Legg til en urlpattern:
```python
path("", csrf_exempt(GraphQLView.as_view(graphiql=True)))
```
graphiql er interface for å teste grapql, denne kan settes til False i production.

Opprett filen graphqlApi/schema.py og regisrer schema i settings under GRAPHENE.

Importer modellene du vil bruke og lag Types for disse. med class Meta kan man bestemme hvilke fields man skal kunne querye på denne måten vil graphene velge riktige fields. Om man vil ha en annen formatering på feks publisert må man eksludere de fra meta fields, legge de til som ekstra field og resolve de manuelt.

class Query skal inneholde alle querys du vil kunne søke etter. Vi vil ha en måte å søke på alle artikler og en måte å etterspørre en spesifikk artikkel. Disse kan ha parametere for å si feks hvor mange artikler du vil ha eller hvilken id på arikkelen du vil requeste. Kan også bruke hjelpefunkjsoner, men kan være greit å legge disse i en annen fil for å separere logikken.

Til slutt må vi sette 
```python
schema = graphene.Schema(query=Query)
```

Da skal man kunne gå til /graphql/ og sende queries på feks formen:
```js
{
  alleArtikler(count:2) {
    id
    tittel
    bilde
  }
  artikkel(id:2){
    id
    tittel
    bilde
    
  }
}
```

## Django Rest Framework
djangorestframework installerers med pip og legges inn i INSTALLED_APPS som rest_framework.

På samme måte som graphql lager vi en ny app med 
```bash
django-admin startapp restApi
```
her trenger vi ikke models.py og migrations. Men her lager vi også en urls.py og includer den i apps/urls.py. 

Django rest framework bruker serilalizers for å konvertere django modeller til og fra json. Vi lager en serializers.py. Siden vi bare skal konvertere en modell til Json kan vi bruke ModelSerializer. Denne fungerer på en lignende måte som Type i grapql. Vi sier hvilke feilds vi vil ha i class Meta og legger til ekstra feilds om vi trenger det. For å bruke modell methoder kan man spesifiserer serializer typen og pointe til metoden med source. Gjør dette på publiser og sist_oppdatert. 

i restApi/views.py kan vi lage ulike views for ulike kall. Om man skal lage et enkelt GET api kan man bruke APIview og lage get metoder. Der henter man objektet man vil fra databasen, serializer det Json og sender det i response. Kan lage ulike views for ulike ting man vil requeste, feks ArtikkelList for alle artikler og ArtikkelDetail for en spesifikk Artikkel basert på id.

Kan så legge disse viewsene inn i urls og bruke de med .as_view(). 