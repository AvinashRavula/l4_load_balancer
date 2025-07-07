# l4_load_balancer

This project implements a simple Layer 4 (TCP) load balancer using HAProxy, Python and Docker Compose.

## Overview

- **HAProxy** acts as a TCP load balancer, forwarding incoming connections on port 8080 to backend servers.
- **Backend servers** are simple Python HTTP servers that respond with their hostname, allowing you to see which backend handled your request.
- **Docker Compose** is used to orchestrate the HAProxy and backend containers, connecting them on a custom bridge network.

## Project Structure

- `backend/`: Contains a Python HTTP server and its Dockerfile.
- `haproxy/`: Contains the HAProxy configuration and Dockerfile.
- `docker-compose.yml`: Defines and connects all services.

## Usage

1. **Create docker network:**
   ```sh
   docker network create lb-net

2. **Build and start the services:**
   ```sh
   docker-compose up --build
