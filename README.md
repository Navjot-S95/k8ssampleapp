# k8sSampleApp

Simple Get service written in python and deployed on kubernetes.


## Setting Up k8s environment using minikube
### Prerequisites
- Ubuntu 20.04 LTS virtual machine

### Setup
 Create linux user and add the user to sudo and docker group
```sh
adduser mini
usermod -aG sudo mini
usermod -aG docker mini
su - mini
```
Install docker and minikube
```sh
mkdir ~/demo
cd ~/demo
sudo  apt  install docker.io
usermod -aG docker mini
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
git clone https://github.com/Navjot-S95/k8ssampleapp.git
cd ~/demo/k8ssampleapp
```

for building docker image
```sh
cd ~/demo/k8ssampleapp/docker
docker build -t navjot2singh/getservice:v1 .
```
Already docker image has been pushed to public docker hub repo
to pull image
```sh
docker pull navjot2singh/getservice:v1
```
Deploy manifests
```sh
cd ~/demo/k8ssampleapp/manifests
kubectl create -f deployment.yaml
kubectl create -f service.yaml
kubectl create -f ingress.yaml
```

monitoring and metrics- Enable node port for kubernetes dashboad
```sh
 kubectl patch svc kubernetes-dashboard --type='json' -p '[{"op":"replace","path":"/spec/type","value":"NodePort"}]' -n kubernetes-dashboard
 ```
 
 TO fetch the node ip and nodeport
 ```sh
 minikube ip              
 kubectl -n kubernetes-dashboard get svc kubernetes-dashboard -o=jsonpath='{.spec.ports[?(@.port==80)].nodePort}'
 
 In browser open
 minikubeip:NodePort
 ```

