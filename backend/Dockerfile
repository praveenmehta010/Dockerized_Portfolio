# Use lightweight Python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy requirements first (for better caching)
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY app ./app

# expose port
# EXPOSE 7000

# run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7000"]