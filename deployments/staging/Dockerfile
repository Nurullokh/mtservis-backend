# Pull base image

FROM python:3.9.7

RUN apt-get update && \
    apt-get -y install netcat git && \
    apt-get clean

# Set some env varibles
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY /requirements /app
RUN pip install --upgrade pip && pip install -r /app/staging.txt
# Add entrypoint.sh
COPY /deployments/staging/entrypoint.sh /app/entrypoint.sh


RUN chmod +x /app/entrypoint.sh
# Copy project
COPY src /app
# Run server
CMD ["/app/entrypoint.sh"]