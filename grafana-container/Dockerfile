# Use an official Grafana runtime as the base image
FROM grafana/grafana:latest

# Set environment variables
ENV GF_SECURITY_ADMIN_USER=admin
ENV GF_SECURITY_ADMIN_PASSWORD=admin
ENV GF_INSTALL_PLUGINS="grafana-clock-panel,grafana-simple-json-datasource"
ENV GF_INSTALL_PLUGINS="grafana-influxdb-flux-datasource"

RUN grafana-cli --pluginsDir "${GF_PATHS_PLUGINS}" plugins install grafana-influxdb-flux-datasource

# Copy custom configuration files (if needed)
COPY custom.ini /etc/grafana/custom.ini

# Expose the Grafana port
EXPOSE 3000

# Start Grafana server
CMD [ "grafana-server", "--config=/etc/grafana/custom.ini" ]
