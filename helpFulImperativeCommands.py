def examTips:

    kubectl run --image=nginx nginx
    kubectl create deployment --image=nginx nginx
    kubectl expose deployment nginx --port 80

    kubectl edit deployment nginx
    kubectl scale deployment nginx --replicas=5
    kubectl set image deployment nginx ngins=nginx:1.18

    kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml

    kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml
    

    if NodePort:
        kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml 


kubectl run redis --image=redis:alpine -l tier=db

kubectl create ns dev-ns

kubectl taint node node01 spray=mortein:NoSchedule

kubectl taint node controlplane node-role.kubernetes.io/control-plane:NoSchedule-

kubectl lable node node01 color=blue

kubectl run static-busybox --image=busybox --dry-run=client -o yaml --command -- sleep 1000 > test.yml

kubectl config view : To check the config info
