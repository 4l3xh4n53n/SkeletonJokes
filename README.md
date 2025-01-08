![image](https://github.com/user-attachments/assets/95acb369-c65c-4ee8-acfb-42b31ab771c6)

# Skeleton Jokes 💀

This is a website that I made so I can get skeleton jokes. That's it.

## Running on baremetal
First make a virtual environment
```bash
python3 -m venv skeletonjokes
```
To activate the virtual environment run the correct command for your operating system.
```bash
source venv/bin/activate # Mac and Linux
venv/Scripts/activate.bat # Windows CMD
venv/Scripts/Activate.ps1 # Windows PowerShell
```
Secondly install the requirements from `requirements.txt`
```bash
pip install -r requirements.txt
```
Finally you can run the flask application with this command
```bash
flask --app main.py run
```
## Running with Docker
First build the image
```bash
docker build . -t skeleton-jokes
```
Then you can either run the image from the command line
```bash
docker run -d -p 8080:8080 skeleton-jokes
```
Or with Docker Compose
```bash
docker-compose up -d
```
## Running with Kubernetes 
You will want to upload your version of the image to a docker registry, do not use the image that is provided with the `Deployment.yaml` file it WILL NOT WORK! 
```bash
cd Kubernetes
kubectl apply -f Deployment.yaml
kubectl apply -f Service.yaml
```
You may want to change to service to a node port.
```yaml
apiVersion: v1
kind: Service
metadata:
  name: skeleton-jokes-svc
spec:
  selector:
    app: skeleton-jokes
  ports:
  - port: 8080
    targetPort: 8080
    nodePort: [port here]
  type: NodePort
```
Alternatively you can use an Ingress.
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
  name: [insert name]
spec:
  rules:
  - host: [insert host name]
    http:
      paths:
      - path: "/"
        pathType: Prefix
        backend:
          service:
            name: [insert host name]
            port:
              number: 8080
```

## Accessing the website
Assuming you are running the website on your local machine the website can be accessed from: `127.0.0.1:8080` or to access the api `127.0.0.1:8080/api`.
If it is running on another machine simply change the IP address, and if it's running with Kubernetes NodePort, make sure to change the port to the node port.

# 💀💀💀