# Docker Airflow Dev Container

`This is a fully self contained docker - poetry project for setting up Airflow dev environments`

`All the software required to build this app will be installed when running the steps listed below`

# Prerequisites

## Setup Docker & Git
### Windows
#### Using admin powershell
1. Install WSL if not installed (```wsl --install```)
2. Start WSL (```wsl --list --online```)
3. Add your preferred linux distro (```wsl --install -d Ubuntu-20.04```)
3. Install Chocolatey 

    ```
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(‘https://chocolatey.org/install.ps1’))
    ```
4. install docker using choco (```choco install -y docker-desktop```)
5. Install git ( if not installed ) (```choco install -y git```)

### Linux
#### Using Bash

```
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo usermod -a -G docker $USER
sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker
newgrp docker
sudo systemctl start docker
sudo systemctl enable docker
sudo apt-get install git
```
#
# Tool Usage

1. Clone repo (```git clone repo ```) 
2. go into project directory (``` cd Airflow ```)
3. Create your feature branch (try to use a relevant branch name) (`git checkout -b feature/fooBar`)
4. Update a airflow.env file with your desired environment variables
5. build your local environment (`docker compose up airflow-init`)
6. start services (`docker compose up`)
7. to run code interactively from terminal run (`docker exec -it (docker inspect --format="{{.Id}}" airflow-init) bash`)
#



## Accessing the environment
After starting Airflow, you can interact with it in 3 ways:

### [CLI commands](https://airflow.apache.org/docs/apache-airflow/stable/usage-cli.html).

You can also run CLI commands, but you have to do it in one of the defined airflow-* services. For example, to run airflow info, run the following command:
`docker-compose run airflow-worker airflow info`


If you have Linux or Mac OS, you can make your work easier and download a optional wrapper scripts that will allow you to run commands with a simpler command.

`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.0/airflow.sh'`

`chmod +x airflow.sh`

Now you can run commands easier.

`./airflow.sh info`

You can also use bash as parameter to enter interactive bash shell in the container or python to enter python container.

`./airflow.sh bash`

`./airflow.sh python`

### [Web Interface](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)

Once the cluster has started up, you can log in to the web interface and begin experimenting with DAGs.
The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow.

### [REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)

Basic username password authentication is currently supported for the REST API, which means you can use common tools to send requests to the API.

The webserver is available at: http://localhost:8080. The default account has the login airflow and the password airflow. Here is a sample curl command, which sends a request to retrieve a pool list:

```
ENDPOINT_URL="http://localhost:8080/"
curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"
```

## Networking
In general, if you want to use Airflow locally, your DAGs may try to connect to servers which are running on the host. In order to achieve that, an extra configuration must be added in docker-compose.yaml. For example, on Linux the configuration must be in the section services: airflow-worker adding extra_hosts: - "host.docker.internal:host-gateway"; and use host.docker.internal instead of localhost. This configuration vary in different platforms. Please check the Docker documentation for Windows and Mac for further information.


#
#### Deployment Overview
#
![Deployment Solution][deployment-diagram]
#

# Best Practices

#
## Contributing

1. Fork it 
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


### Technologies used by this build 
#
[More Details on Chocolatey](choco)

[More Details on Docker](docker)

[More Details on Poetry](poetry)

[More details on airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

[More details on airflow connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)

<!-- Markdown link & img dfn's -->
[forking-repo]: https://docs.microsoft.com/en-us/azure/devops/repos/git/forks?view=azure-devops&tabs=visual-studio-2019
[choco]: https://community.chocolatey.org/courses/getting-started/what-is-chocolatey
[docker]: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/docker-defined
[poetry]: https://python-poetry.org/docs/
[deployment-diagram]: https://lucid.app/publicSegments/view/714776b6-8cb5-4280-9957-ee1300c696d1/image.png
[databrick-import-workbooks]: https://learn.microsoft.com/en-us/azure/Airflow/notebooks/notebook-export-import


#
`cleanup docker env`
#
```
docker kill $(docker container ls -q)
docker system prune -a 
``` 