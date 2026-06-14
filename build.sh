docker build . -t nk732100/flask-test-app 
docker push nk732100/flask-test-app:latest
kubectl delete -f flask-test-app.yml
kubectl apply -f flask-test-app.yml
minikube service flask-test-app-service -n kube-learning