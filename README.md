# projekt
## Rozproszony system monitoringu usług sieciowych w współpracy z firmą Samsung

Autorzy:
Kinga Górska,
Mikołaj Grzempa,
Szymon Jański,
Wojtek Kostowski,
Janek Karczewicz,
Thang Cao.

## Initial setup
Project build on python version 3.10, you need to install all requirements and edit files listed below \
don't forget about django migrate before runserver \
to generate INFLUXDB_AUTH_TOKEN use:
```
python MonaApps_Project\MonaApps\token_generator.py
```
to generate SECRET_KEY use:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
  
* Files to edit:
  *  grafana-container\docker-compose.yml
  *  InfluxDB-container\Influx\api_keys.txt
  *  MonaApps_Project\Download_content\telegraf-container\docker-compose.yml
  *  MonaApps_Project\MonaApps_Project\.env
  *  MonaApps_Project\MonaApps_Project\settings.py
      * LINE ~93 - GRAFANA_IFRAME_LINK - link to dashboard
      * LINE ~150 - smtp server config (part is in .env)

 More info about INFLUXDB SETUP in:  *InfluxDB-container\readme.txt*
