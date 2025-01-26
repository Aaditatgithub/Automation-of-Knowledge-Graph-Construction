class Config:
    KAFKA_BROKER = 'localhost:9092'
    TOPIC_NAME = 'test_topic'

    # Neo4j Configuration
    NEO4J_URI = "neo4j+s://41495b6f.databases.neo4j.io"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "9HhsOWzUtVWIpwO1sjUvmM3X2MVSWJKGIdNdo3XoBBg"

    GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
    # LLama3.2 vision config (image classification)
    IGROQ_API_KEY = "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"
    IGROQ_MODEL = "llama-3.2-11b-vision-preview"

    MISTRAL_API_KEY = "P4c0n7YJr4YwWCefa97g6Zd24QetjJDp"

    #LLM Configuration (Product classification)
    GROQ_API_KEY = "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"
    GROQ_MODEL = "llama-3.3-70b-versatile"
