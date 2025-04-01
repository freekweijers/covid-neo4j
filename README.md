# Neo4j JSONL Importer

Dit project bevat een Python-script voor het importeren van gegevens uit een JSONL-bestand in een Neo4j-database.

## Voorwaarden

Zorg ervoor dat je de volgende software op je systeem hebt geïnstalleerd:

- Python 3.x
- Docker en Docker Compose

## Installatie

Volg deze stappen om het project op te zetten:

1. **Clone de repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Stel de Neo4j-database in**:
   - Zorg ervoor dat je Docker en Docker Compose hebt geïnstalleerd.
   - Voer het volgende commando uit om de Neo4j-database te starten:
     ```bash
     docker-compose up -d
     ```
   - Dit zal de Neo4j-database starten op `localhost` met de standaard poorten.

3. **Installeer de vereiste Python-pakketten**:
   - Maak een virtuele omgeving aan (optioneel maar aanbevolen):
     ```bash
     python -m venv venv
     source venv/bin/activate  # Op Windows: venv\Scripts\activate
     ```
   - Installeer de vereiste pakketten:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configureer de databaseverbinding**:
   - Open het bestand `import_to_neo4j.py` en wijzig de variabelen `NEO4J_USER` en `NEO4J_PASSWORD` indien nodig om overeen te komen met je Neo4j-configuratie.

## Gebruik

Om gegevens uit een JSONL-bestand te importeren, gebruik je het volgende commando:

```bash
python import_to_neo4j.py <pad_naar_jsonl_bestand> --max-lines <max_aantal_regels>
```

Bijvoorbeeld:

```bash
python import_to_neo4j.py data/covid19_output_analysed.jsonl --max-lines 100
```

Dit commando importeert maximaal 100 records uit het opgegeven JSONL-bestand in de Neo4j-database.


## Power BI koppelen
Om Power BI te koppelen aan Neo4j is het nodig om de Neo4j ODBC connector te downloaden.
https://neo4j.com/bi-connector/

Open Power BI Desktop.

Search for ODBC in the Get data from another source panel.

Select Simba Neo4j in the DSN dropdown menu.

Insert the connection string Host=localhost;SSL=0 in the Advanced options section.

Insert your username and password.

## Opmerkingen

- Zorg ervoor dat je het wachtwoord in de `docker-compose.yml` en in het Python-script aanpast naar een veilig wachtwoord.
- Controleer de Neo4j-database via de webinterface op `http://localhost:7474` om de geïmporteerde gegevens te bekijken.
