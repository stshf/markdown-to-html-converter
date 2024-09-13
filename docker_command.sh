docker build -t markdown-to-html-python3 .
docker run -v $(pwd)/output:/app/output markdown-to-html-python3