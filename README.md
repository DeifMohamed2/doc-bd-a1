# Project Execution Guide

This project involves a pipeline for data processing and analysis using Python scripts within a Docker container. The pipeline includes data loading, data preprocessing, exploratory data analysis, visualization, and model implementation.

## Docker Hub : 
### https://hub.docker.com/layers/deifmohamed/doc-bd-a1/latest/images/sha256:d13839044b4aa93c48da840c1c62ddbd11f52528adfae1509849117811e83d87?tab=layers

## Git Hub : 
### https://github.com/DeifMohamed2/doc-bd-a1

## Execution Steps

1. **Build Docker Image**: 
   - After creating the Dockerfile, we build it to produce an image.
     ```
     docker build -t bd-a1-image .
     ```

2. **Run Docker Container**: 
   - we Run the container using the generated image.
     ```
     docker run -it --name bd-a1-container bd-a1-image
     ```

3. **Inside the Container**:
   - Create the Python files as specified.
   - Initiate the pipeline using the command:
     ```
     python3 load.py dataset.csv
     ```

4. **Pipeline Execution**:
   - The pipeline will generate several files and figures, conforming to the prescribed outputs.

5. **Data Transfer**:
   - Run the final.sh script inside the container to relocate generated files to your local machine.
     ```
     bash final.sh
     ```

6. **Push Docker Image to Docker Hub** (BONUS):
   - Push the Docker Image to Docker Hub.
     ```
     docker tag bd-a1-image username/bd-a1-image
     docker push username/bd-a1-image
     ```

7. **Push All Files to GitHub Repo** (BONUS):
   - Push all your files to a GitHub repo.

## Docker Commands Used

- `docker build -t bd-a1-image .`: Build Docker image.
- `docker run -it --name bd-a1-container bd-a1-image`: Run Docker container.
- `docker cp container_id:/path/to/source /path/to/destination`: Copy files from container to local machine.
- `docker stop container_id`: Stop Docker container.
- `docker tag bd-a1-image username/bd-a1-image`: Tag Docker image.
- `docker push username/bd-a1-image`: Push Docker image to Docker Hub.

