#!/bin/bash

# Define the container ID
CONTAINER_ID="5c7d99e9301d37ee0481ca3b475179066e5e3d5c991377811a40167e19406f9d"  # Replace with the actual container ID

# Specify the directory within the container where output files are located
CONTAINER_DIR="/home/doc-bd-a1/"

# Specify the local directory where you want to save the output files
LOCAL_DIR="service-result/"

# Create the local directory if it doesn't exist
mkdir -p "${LOCAL_DIR}"

# Copy output files from the container to the local machine
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}res_dpre.csv" "${LOCAL_DIR}"
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}eda-in-1.txt" "${LOCAL_DIR}"
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}eda-in-2.txt" "${LOCAL_DIR}"
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}eda-in-3.txt" "${LOCAL_DIR}"
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}vis.png" "${LOCAL_DIR}"
docker cp "${CONTAINER_ID}:${CONTAINER_DIR}k.txt" "${LOCAL_DIR}"

# Stop the container
docker stop "${CONTAINER_ID}"

echo "Output files copied to '${LOCAL_DIR}'"
