import argparse
import json
from neo4j import GraphDatabase

# Neo4j database configuratie
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your_password_here"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def insert_data(tx, data):
    query = """
    MERGE (p:Paper {title: $title})
    SET p.abstract = $abstract, p.date = $date

    FOREACH (author IN $authors |
        MERGE (a:Author {name: author})
        MERGE (a)-[:WROTE]->(p)
    )

    FOREACH (entity IN $entities |
        MERGE (e:Entity {word: entity.word})
        SET e.label = entity.label
        MERGE (p)-[:MENTIONS]->(e)
    )
    """
    authors = [name.strip() for name in data.get('author', '').split(',')]
    entities = data.get('entities', [])

    tx.run(query, title=data['title'], abstract=data['abstract'], date=data['date'], authors=authors, entities=entities)

def process_jsonl(file_path, max_lines):
    with driver.session() as session:
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                data = json.loads(line)
                session.write_transaction(insert_data, data)
    print(f"✅ {min(i + 1, max_lines)} records geïmporteerd.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Importeer een JSONL-bestand in Neo4j.")
    parser.add_argument("jsonl_file", help="Pad naar het JSONL-bestand")
    parser.add_argument("--max-lines", type=int, help="Maximaal aantal regels om te importeren")

    args = parser.parse_args()
    process_jsonl(args.jsonl_file, args.max_lines)

    driver.close()
