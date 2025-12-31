# Example pseudocode to push custom metrics to Stackdriver (Cloud Monitoring)
from google.cloud import monitoring_v3
client = monitoring_v3.MetricServiceClient()
project_name = client.project_path('your-project')
# create metric and write time series...
