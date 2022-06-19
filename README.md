# k8sSampleApp

Simple Get service written in python and deployed on kubernetes.

## Repo Details
### service.py
Python service that responds to an HTTP GET request and returns: 
- a. Timestamp 
- b. hostname 

### Dockerfile
- Dockerfile using which a lean image of size 45 mb can be created
- It is using alpine base image
For building docker image
```sh
cd ~/demo/k8ssampleapp
docker build -t navjot2singh/getservice:v1 .
```
#### Already docker image has been pushed to public docker hub repo and manifests files are configured with that image
To pull image
```sh
docker pull navjot2singh/getservice:v1
```

### Manifests folder
It contains all the required k8s manifest files
- deployment.yaml
- service.yaml
- ingress.yaml

#### Deployment of k8s manifest
```sh
cd ~/demo/k8ssampleapp/manifests
kubectl create -f deployment.yaml
kubectl create -f service.yaml
kubectl create -f ingress.yaml
```


### img folder
It contains endpoint and metric dashboard images for reference


## Testing Environment
- Minikube on windows or mac - https://minikube.sigs.k8s.io/docs/start/
- Minikube on Linux- ubuntu - Refer below


## Setting Up k8s environment using minikube
### Prerequisites
- Ubuntu 20.04 LTS virtual machine

### Setup
 Create linux user and add the user to sudo and docker group
```sh
adduser mini
usermod -aG sudo mini
su - mini
```
Install docker and minikube
```sh
mkdir ~/demo
cd ~/demo
sudo apt update
sudo  apt  install docker.io
sudo usermod -aG docker mini
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo apt install conntrack
```

setup kubectl
```sh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

start minikube
```sh
exit
su mini
cd ~/demo
docker ps               //to check if user mini has access to docker sock
minikube start --driver=none --extra-config=kubelet.housekeeping-interval=10s
```

enable addons
```sh
minikube addons enable ingress
minikube addons enable metrics-server
minikube addons enable dashboard
```

Clone code
```sh
cd ~/demo
git clone https://github.com/Navjot-S95/k8ssampleapp.git
```

Deploy manifests
```sh
cd ~/demo/k8ssampleapp/manifests
kubectl create -f deployment.yaml
kubectl create -f service.yaml
kubectl create -f ingress.yaml
```
### Test the endpoint
In commandline
 
```sh
minikube ip                      ## provides the node IP

curl --header 'Host: k8ssampleapp.com' <MINIKUBE_IP>                 
```
Browser- create host entry
```sh
<MINIKUBE_IP>     k8ssampleapp.com
```


## Monitoring and Metrics
Enable node port for kubernetes dashboad
```sh
 kubectl patch svc kubernetes-dashboard --type='json' -p '[{"op":"replace","path":"/spec/type","value":"NodePort"}]' -n kubernetes-dashboard
 ```
 
 TO fetch the node ip and nodeport
 ```sh
 minikube ip              
 kubectl -n kubernetes-dashboard get svc kubernetes-dashboard -o=jsonpath='{.spec.ports[?(@.port==80)].nodePort}'
 
 In browser open
 http://<MINIKUBE_IP>:NodePort
 ```

