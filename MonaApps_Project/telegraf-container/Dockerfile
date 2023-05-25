# Use the official Telegraf base image
FROM telegraf

# Install Python and any required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install any Python packages required by your script
# For example, if you need requests module, you can add:
RUN pip3 install requests

# Copy the Python script to the container
COPY checker.py /checker.py

# Set the command to execute the Telegraf process
CMD ["telegraf", "--config", "/etc/telegraf/telegraf.conf"]
