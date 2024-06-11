def MonitoringSolution:
    There are open source solutions that helps to gather metrics. 

    Metric Server, Has 1 server prer cluster. Aggregaretes and stores in memory . It is a in memeory solution. Can't have historical data.


    K8s runs an agent on each node called kubelet, recevies info from api-server , There is a sub component called cAdvisor which gathers performance metrics from pod. 

    After we have the metrics server can use commands like kubectl top node. kubectl top pod.'

def ManagingApplicationLog:
    kubectl logs -f mypod , To see the livestream of logs.

    If pod has more than 1 container, We can mention the container name and the pod as well. 



