#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the backend server
cd backend
uvicorn server:app --host 0.0.0.0 --port 8000
