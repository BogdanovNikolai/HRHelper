FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y docker.io
# Install docker-compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose
RUN usermod -aG docker jenkins
USER jenkins 