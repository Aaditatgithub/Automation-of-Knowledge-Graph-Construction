class Config:
    KAFKA_BROKER = 'localhost:9092'
    TOPIC_NAME = 'test_topic'

    # Neo4j Configuration
    NEO4J_URI = "neo4j+s://41495b6f.databases.neo4j.io"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "9HhsOWzUtVWIpwO1sjUvmM3X2MVSWJKGIdNdo3XoBBg"

    #LLM Configuration
    GROQ_API_KEY = "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"
    GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
    GROQ_MODEL = "llama-3.2-90b-vision-preview"
