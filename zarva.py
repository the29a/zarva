#!/usr/bin/python3
import sys
import docker
from pprint import pprint
import os


#os.environ['DOCKER_HOST'] = 'unix://var/run/docker.sock'

client = docker.from_env()

# Examples from documentation
# client = docker.DockerClient(base_url='unix://var/run/docker.sock')
# client = docker.APIClient(base_url='unix://var/run/docker.sock')

# List Docker images (docker image ls like)
def zarva_list_images():
    images = client.images.list(all=True)
    print(f"{'ID':<20} {'Name/Tags':<30} {'Size':<7}")
    print("-" * 65)
    # Print image info
    for image in images:
        # Get image id (cut hash)
        image_id = image.short_id.replace("sha256:", "")
        
        # Get image tags (if exist)
        tags = image.tags if image.tags else ["<none>"]

        # Getting image size in MB
        size_mb = round(image.attrs["Size"] / (1024 * 1024), 2)
        
        # Print image info
        tags = ", ".join(image.tags) if image.tags else "<none>"
        size_mb = round(image.attrs["Size"] / (1024 * 1024), 2)
        print(f"{image_id:<20} {tags:<30} {size_mb:<7} MB")

# List Docker image summary info (docker inspect like)
def zarva_list_summary():
    images = client.images.list(all=True)
    found_image = None
    image_short_id = sys.argv[2] if len(sys.argv) > 2 else None
    for image in images:
        image_name_or_id = image.short_id.replace("sha256:", "")
        if (image_name_or_id == image.id or
            image_name_or_id in image.tags or    
            image_name_or_id == image_short_id or 
            image_short_id.startswith(image_name_or_id) or
            any(image_name_or_id in tag for tag in (image.tags or []))):
            found_image = image
            break
    
    if found_image:
        pprint(found_image.attrs)
    else:
        print(f"Image '{image_name_or_id}' not found.")

# List Docker Image env only 
def zarva_list_env():
    images = client.images.list(all=True)
    found_image = None
    image_short_id = sys.argv[2] if len(sys.argv) > 2 else None
    for image in images:
        image_name_or_id = image.short_id.replace("sha256:", "")
        if (image_name_or_id == image.id or
            image_name_or_id in image.tags or    
            image_name_or_id == image_short_id or 
            image_short_id.startswith(image_name_or_id) or
            any(image_name_or_id in tag for tag in (image.tags or []))):
            found_image = image
            break

    # If image founr, show info
    if found_image:
        # Show info
        print("Environment Variables:")
        print(*found_image.attrs["Config"]["Env"], sep="\n")
    else:
        print(f"Image '{image_name_or_id}' not found.")

# Show image history
def zarva_list_history():
    images = client.images.list(all=True)
    found_image = None
    image_name_or_id = sys.argv[2] if len(sys.argv) > 2 else None
    for image in images:
        image_short_id = image.short_id.replace("sha256:", "")
        if (image_name_or_id == image.id or
            image_name_or_id in image.tags or    
            image_name_or_id == image_short_id or 
            image_short_id.startswith(image_name_or_id) or
            any(image_name_or_id in tag for tag in (image.tags or []))):
            found_image = image
            break

    if found_image:
        # Get history and reverse output
        history = found_image.history()[::-1]

        # Cleaning output
        def list_layers_clean_created_by(created_by):
            if not created_by:
                return ""
            # Remove /bin/sh -c and other prefixes
            if created_by.startswith("/bin/sh -c"):
                created_by = created_by[len("/bin/sh -c"):].strip()
            # Remove #(nop)
            if created_by.startswith("#(nop)"):
                created_by = created_by[len("#(nop)"):].strip()
            return created_by

        # Show layers history
        for layer in history:
            created_by = layer.get("CreatedBy", "")
            if created_by:  # Ignore empty commands
                cleaned_command = list_layers_clean_created_by(created_by)
                print(cleaned_command)
    else:
        print(f"Image '{image_name_or_id}' not found.")

# Show help
def zarva_help():
    print(
    '''
Usage: zarva.py [TARGET] [OPTION] 

Example: 
python3 zarva.py -t <imageID>

You can use -t or --target as argument.
 --list-image or -li for image list
 --list-summary  or -ls for summary image info (like docker inspect)
 --list-env or -le for list image environment variables
 --list-history or -lh for list image history
 --help or -h to show this command list
    '''
    )

if len(sys.argv) == 1 or sys.argv[1] in ["--help", "-h"]:
    zarva_help()
elif sys.argv[1] in ["-li", "--list-image"]:
    zarva_list_images()
elif sys.argv[1] in ["-ls", "--list-summary"]:
    if len(sys.argv) < 3:
        print("Missing Target.")
        print("You can use -t or --target as argument.")
    else:
        image_name_or_id = sys.argv[2]  # Передаем image_name_or_id
        zarva_list_summary()
elif sys.argv[1] in ["-le", "--list-env"]:
    if len(sys.argv) < 3:
        print("Missing Target.")
        print("You can use -t or --target as argument.")
    else:
        image_name_or_id = sys.argv[2]  # Передаем image_name_or_id
        zarva_list_env()
elif sys.argv[1] in ["-lh", "--list-history"]:
    if len(sys.argv) < 3:
        print("Missing Target.")
        print("You can use -t or --target as argument.")
    else:
        image_name_or_id = sys.argv[2]  # Передаем image_name_or_id
        zarva_list_history()
else:
    print("Invalid arguments, aborting.")


'''if len(sys.argv) == 1 or sys.argv[1] in ["--help", "-h"]:
    zarva_help()
elif sys.argv[1] in ["-li", "--list-image"]:
    zarva_list_images()
elif sys.argv[1] in ["-ls", "--list-summary"]:
    zarva_list_summary()
elif sys.argv[1] in ["-le", "--list-env"]:
    zarva_list_env()
elif sys.argv[1] in ["-lh", "--list-history"]:
    zarva_list_history()
else:
    print("Invalid arguments, aborting.")
'''