# Skrypt do update telegrafa
import docker

client = docker.from_env()

# Start the Telegraf container
container = client.containers.run("telegraf", detach=True, name="telegraf")

# Copy the Telegraf configuration file to the container
config_file_path = "/path/to/telegraf.conf"
with open(config_file_path, "rb") as f:
    container.put_archive("/etc/telegraf", f.read())

# Restart the Telegraf container
container.restart()
