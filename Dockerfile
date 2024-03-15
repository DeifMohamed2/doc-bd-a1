# Specify base image
FROM ubuntu:latest

# Update packages and install dependencies
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create directory inside container
RUN mkdir -p /home/doc-bd-a1/

# Move dataset to container
COPY dataset.csv /home/doc-bd-a1/

# Open bash shell upon container startup
CMD ["/bin/bash"]
