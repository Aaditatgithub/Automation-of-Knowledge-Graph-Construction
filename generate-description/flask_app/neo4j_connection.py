from neo4j import GraphDatabase
from config import Config

class Neo4jConnection:
    def __init__(self):
        self.uri = Config.NEO4J_URI  # AuraDB URI
        self.user = Config.NEO4J_USER
        self.password = Config.NEO4J_PASSWORD
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        """Closes the Neo4j connection."""
        self.driver.close()

    def execute_query(self, query, parameters=None):
        """Executes a Cypher query and returns results."""
        with self.driver.session() as session:
            return session.run(query, parameters).data()

# Create a global Neo4j connection instance
neo4j_conn = Neo4jConnection()
