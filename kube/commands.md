# Some useful commands. 

## minikube start 

`minikube start` or `minikube start --driver docker`

## kubectl commands

### kubectl get 
- `kubectl get pods` or `kubectl get pods --watch`<br>
- `kubectl get deploy`<br>
- `kubectl get hpa` <br>
- `kubectl get svc` or `kubectl get svc -o wide`<br>
- `kubectl get namespaces`
- `kubectl get pvc`

### kubectl cleaning with awk

`kubectl get deploy | awk '{print $1}' | xargs kubectl delete deployment`
`kubectl get svc | awk '{print $1}' | xargs kubectl delete svc`

### kubectl other 
- `kubectl apply -f yaml_file.yaml`<br>
- `kubectl exec -ti <pod name> /bin/bash` <br>
- `kubectl get service <service-name> --output='jsonpath="{.spec.ports[0].nodePort}"'`<br>
- `kubectl cluster-info`<br>

## minikube network

`minikube service <service-name> --url`<br>
`minikube ip`<br>
`minikube tunnel` - to access through browser 

## minikube end 

`minikube stop` <br>
`minikube delete`


## frequent commands to clean all 

kubectl get deploy | awk 'NR>1{print $1}' | xargs kubectl delete deploy 

kubectl get pvc | awk 'NR>1{print $1}' | xargs kubectl delete pvc 

kubectl get pv | awk 'NR>1{print $1}' | xargs kubectl delete pv

kubectl get svc | awk 'NR>1{print $1}' | xargs kubectl delete svc