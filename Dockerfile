FROM python:3.12-slim

# Links the image to your repo on GitHub (replace with your repo URL)
LABEL org.opencontainers.image.source="https://github.com/YOUR_USERNAME/dummy-model"
LABEL org.opencontainers.image.description="Dummy model image for testing registry uploads"

WORKDIR /app
COPY model.py .

ENTRYPOINT ["python", "model.py"]
CMD ["3"]
