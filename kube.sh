kubectl delete -f flask-test-app.yml
kubectl apply -f flask-test-app.yml
minikube service flask-test-app-service -n kube-learning