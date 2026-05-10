from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 DevOps CI/CD Pipeline Project</h1>
    <p>This application is deployed using Jenkins, Docker, and AWS EC2.</p>
    <p>Tools used:</p>
    <ul>
        <li>Jenkins - CI/CD Pipeline</li>
        <li>Docker - Containerization</li>
        <li>SonarQube - Code Quality Analysis</li>
        <li>Trivy - Security Scanning</li>
        <li>AWS EC2 - Deployment Server</li>
    </ul>
    <h3>✅ Application is running successfully!</h3>
    """

app.run(host='0.0.0.0', port=5000)