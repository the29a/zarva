# zarva

`zarva` is a Python script that provides a convenient interface for working with Docker images using the Docker SDK. The script allows you to perform various operations with Docker images, such as listing images, retrieving detailed information about an image, viewing environment variables, and inspecting the image's history.

##### **Main Features:**
1. **List Docker Images** (`--list-image` or `-li`):
   - Displays a list of all Docker images on the local machine with their IDs, tags, and sizes.

2. **Image Summary Information** (`--list-summary` or `-ls`):
   - Shows detailed information about a specific Docker image (similar to the `docker inspect` command).

3. **Image Environment Variables** (`--list-env` or `-le`):
   - Displays the environment variables defined in the Docker image.

4. **Image History** (`--list-history` or `-lh`):
   - Shows the history of changes made to the Docker image, including the commands executed to create each layer.

5. **Help** (`--help` or `-h`):
   - Displays help information on how to use the script.

##### **Usage:**
```bash
python3 zarva.py [OPTION]
```

##### Running in Docker
Pull image from GHCR:
```bash
docker pull ghcr.io/the29a/zarva:latest
```

Or you can build image manualy:
```bash
docker build -t zarva .
```

Run zarva inside Docker:
```shell
# Pulled image
docker run -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/the29a/zarva -li                    
ID                   Name/Tags                      Size   
-----------------------------------------------------------------
1cb1059880dd         ghcr.io/the29a/zarva:latest    457.01  MB

# Builded image
docker run -v /var/run/docker.sock:/var/run/docker.sock zarva -li 
ID                   Name/Tags                      Size   
-----------------------------------------------------------------
35ac1920cce2         zarva:latest                   457.02  MB
```


##### **Examples:**
- List Docker images:
  ```bash
  python3 zarva.py --list-image
  ```
- Get detailed information about an image:
  ```bash
  python3 zarva.py --list-summary <imageID>
  ```
- View environment variables:
  ```bash
  python3 zarva.py --list-env <imageID>
  ```
- View image history:
  ```bash
  python3 zarva.py --list-history <imageID>
  ```

---

#### **Requirements:**
- Python 3.x
- Docker SDK for Python (`docker` module)
- Docker installed and running on the local machine

##### **Installation:**
1. Install the Docker SDK for Python:
   ```bash
   pip install docker
   ```
2. Ensure Docker is installed and running on your machine.

---
#### TODO
- [x] Running zarva in Docker
- [ ] Move from ubuntu to alpine
- [ ] Remade exaple dockerfiles
