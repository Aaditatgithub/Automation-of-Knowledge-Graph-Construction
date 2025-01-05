Here is a possible `README.md` file for your project:

---

# Stylumia Hackathon Project

This project combines a modern Vite-powered React frontend, a Flask-based backend API, and Apache Kafka for event streaming and messaging. The architecture is built to demonstrate seamless integration of microservices and modern web technologies for a hackathon event.

## Demo

[![Watch the Demo Video](https://img.youtube.com/vi/<YOUR_VIDEO_ID>/0.jpg)](https://www.youtube.com/watch?v=<YOUR_VIDEO_ID>)

*Click on the image above to watch the demo video.*

## Folder Structure

```
Stylumia-Hackathon/
│
├── frontend/                     # React-based frontend
│   ├── src/                      # Source files for the React app
│   ├── .bolt/                    # Configuration files
│   ├── package.json              # Node.js project metadata
│   └── vite.config.ts            # Vite configuration
│
├── generate-description/         # Directory for other related scripts
│   ├── flask_app/                    # Flask-based backend API
│   └── myenv
├── docker-compose.yml            # Docker Compose setup for Apache Kafka
└── Readme.md                     # Project documentation
```

---

## Setup Instructions

To set up and run the project locally, follow these steps:

### 1. Running the Vite React App

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

---

### 2. Setting up Docker for Apache Kafka

1. Ensure Docker is installed and running on your system.

2. Navigate to the root of the project directory where the `docker-compose.yml` file is located.

3. Start the Kafka services using Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Confirm that Kafka is running by checking the Docker containers:
   ```bash
   docker ps
   ```

---

### 3. Running the Flask App

1. Navigate to the `generate-description` directory:
   ```bash
   cd generate-description
   ```

2. Create a virtual environment (if not already done):
   ```bash
   python -m venv myenv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ``` 

4. Install required Python dependencies inside flask_app dir:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask app:
   ```bash
   python app.py
   ```

6. Ensure the Kafka container is running for proper Flask-Kafka integration.

---

## Additional Notes

- Ensure Node.js and Python are installed on your machine.
- Make sure Docker is properly configured and has access to the necessary resources (memory, CPU).
- The Flask app communicates with Kafka, so Kafka must be running before starting the Flask app.

--- 

Feel free to adjust paths or add details as per your project needs.