To setup an InfluxDB:
- create buckets: "valid_metrics" and "telegraf_data_agent"
- create api tokens:
  - one token for all access 
    - copy influx all access token and paste it to Influx/api_keys.txt
  - one token with permission to write to "telegraf_data_agent" bucket
    - this token should be copied to downloadable version of agent's telegraf plugin and pasted in telegraf's docker-compose.yml file (MonaApps_Project\Download_content\telegraf-container\docker-compose.yml)
- import task from Influx/validate_data.json
