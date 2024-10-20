from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import psutil

app = Flask(__name__)


cpu_usage = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage = Gauge('memory_usage', 'Memory usage percentage')
disk_usage = Gauge('disk_usage', 'Disk usage percentage')
process_count = Gauge('process_count', 'Number of running processes')
swap_usage = Gauge('swap_usage', 'Swap memory usage percentage')

@app.route('/metrics')
def metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)
    process_count.set(len(psutil.pids()))
    swap_usage.set(psutil.swap_memory().percent)
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/')
def home():
    return "Monitoring application with CPU, memory, disk, process count, and swap metrics. Go to /metrics for Prometheus metrics."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
