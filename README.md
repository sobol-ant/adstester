# Testing ads/trackers traffic

A simple web application for testing ad and tracker traffic by sending POST requests to specified URLs.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn src.main:app --host 0.0.0.0 --reload
```

3. Open http://localhost:8000 in your browser

## Deployment to Render.com

1. Push your code to a GitHub repository

2. Go to [render.com](https://render.com) and create a free account

3. Click "New +" button and select "Web Service"

4. Connect your GitHub repository

5. Configure the web service:
   - Name: Choose any name you like
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn src.main:app --host 0.0.0.0`
   - Plan: Free

6. Click "Create Web Service"

Your application will be automatically deployed and available at the URL provided by Render.
