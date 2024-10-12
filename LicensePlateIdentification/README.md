# Automatic License Plate Reader with IoT Integration

## Overview

This project involves developing an automatic license plate reader system using Optical Character Recognition (OCR) with TensorFlow, creating a FastAPI backend to handle the logic and database interactions, and integrating an Arduino device for IoT functionality.

## Features

1. Automatic license plate reading using OCR.
2. Checking the license plate against a Redis database.
3. Adding and removing license plates from the Redis database.
4. Sending a signal to an Arduino device over Wi-Fi.

## Installation

 Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

## Running the Project

1. Start the services using Docker Compose:
    ```bash
    docker-compose up
    ```

2. The FastAPI server will be available at `http://localhost:8000`.
3. Redis will be available at `localhost:6379` and its data will persist across restarts.

## Usage

- The FastAPI server exposes endpoints to check, add, and remove license plates:
  - `POST /check_plate/` to check a license plate.
  - `POST /add_plate/` to add a new license plate.
  - `DELETE /remove_plate/` to remove an existing license plate.
- The event listener continuously captures images from the camera and processes them for license plates.

## License

This project is licensed under the MIT License.
