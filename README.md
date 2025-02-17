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
- [ ] Running zarva in Docker
- [ ] Remade exaple dockerfiles