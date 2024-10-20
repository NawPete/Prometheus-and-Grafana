# Case Study: Monitoring System Using Docker, Prometheus, Grafana, and Python Flask

## Project Goal

For this project, I set out to create a real-time system resource monitoring application. The application was designed to collect data on CPU usage, memory (RAM), disk usage, the number of running processes, and swap memory utilization. I used Prometheus for data collection, and the visualization was done through Grafana. Everything was deployed in Docker containers, using Docker Compose to simplify environment management and enable easy scalability.

## Project Challenges

The project posed several key challenges:

1. **Real-time monitoring** – It was necessary to develop an application that efficiently collected system data and presented it in a format readable by Prometheus.
2. **Containerization** – All components needed to run in Docker containers, ensuring easy deployment and management.
3. **Flexibility** – The system needed to be easily extensible, allowing new metrics or monitoring modules to be added in the future.

## Project Implementation

The project was completed in several stages:

### 1. Creating a Monitoring Application with Python Flask

I started by developing the application in Python, using the Flask framework. To collect system data (CPU, RAM, disk, processes, swap), I used the **psutil** library. The collected data was exposed on the `/metrics` endpoint, from which Prometheus could scrape the metrics.

The application collected the following metrics:

- **CPU usage** – The percentage of CPU load.
- **Memory (RAM) usage** – The percentage of system memory in use.
- **Disk usage** – The usage of the main system partition.
- **Number of running processes** – The count of active system processes.
- **Swap memory usage** – The percentage of swap memory in use.

The application was set to run on port **8080**, and Prometheus regularly gathered the data from this endpoint.

### 2. Containerizing the Application

The next step was containerizing the application. I used Docker and Docker Compose to deploy the monitoring app, Prometheus, and Grafana in separate containers. Docker Compose allowed me to easily launch all services simultaneously.

In the **Dockerfile**, I specified the Python image for the application, which included all the necessary dependencies. In the **docker-compose.yml** file, I defined all the services, ensuring that the monitoring app, Prometheus, and Grafana would run within the same Docker network, enabling seamless communication between them.

### 3. Configuring Prometheus and Grafana

Next, I configured Prometheus to scrape data from the monitoring application at regular intervals. In the **prometheus.yml** file, I specified the scraping frequency and the source of the metrics (the application’s endpoint).

Then, I configured Grafana to visualize the data collected by Prometheus. Grafana connected to Prometheus, allowing the creation of dashboards with dynamic graphs monitoring CPU usage, RAM, disk space, process count, and swap memory.

## Results

This project allowed me to:

- **Monitor system resources** in real time by collecting and displaying data on CPU, memory, disk, and processes.
- **Automate deployment** – Using Docker Compose, I was able to quickly launch and manage the entire environment, which significantly sped up testing and development.
- **Maintain flexibility** – The system was designed to be easily expandable, allowing new features, metrics, or monitoring modules to be added with ease.

## Lessons Learned

Working on this project helped me understand how powerful and flexible tools like Docker, Prometheus, and Grafana are for monitoring system resources. Containerization made it easy to deploy and manage the system, while the flexibility of these tools opened up possibilities for further project development.

---

## Technologies Used

- **Python Flask** – Monitoring application.
- **psutil** – For gathering system resource data.
- **Prometheus** – For collecting and storing metrics.
- **Grafana** – For visualizing system data.
- **Docker & Docker Compose** – For containerization and automating the environment.

## Future Expansion Opportunities

- **Adding more metrics** – Incorporating more detailed data, such as network monitoring or temperature readings.
- **Notification system** – Integrating Grafana with alerts to automatically notify when thresholds are exceeded.
- **Scaling** – The system can be expanded to include additional machines and servers, allowing monitoring of more resources simultaneously.

## Conclusion

This project demonstrates how effectively Docker, Prometheus, and Grafana can be used to monitor system resources in real time. It was a step towards automating monitoring and managing environments in a scalable and easy-to-deploy way. This project can serve as a foundation for further work aimed at more advanced monitoring and automation processes.
