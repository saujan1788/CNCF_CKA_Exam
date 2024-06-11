def DaemonSets:
    They are like replica sets, Runs one copy pod pod in each node of the cluster. When node is removed that pods is removed. Best for monitoring agent log collector.  

    Kubeproxy can be deployed as a daemonset for the cluster

    Kubeproxy can be deployed as a daemonset for the cluste. Networking is a good used case. 

    DeamonSet : apps/v1r

    They are ignore by kube-scheduler.


