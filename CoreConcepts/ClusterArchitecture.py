def Architecutre:

    if ControlPlaneComponents:

        if Master:

             Controller-manager, Node-Controller, Replication Controller, Scheduler, ETCD Cluster, kube-api server (the most imp guy) CEO of k8s.

            ContainerRunTimeEngine: Docker, containerd

            Each ship is a node, each ship has captain need to look after their ship and communicate with master ship , make sure reports are sent , load appropriate container, captain of the ship is kubelet, kubelet listens for instrcution from the kube-api server and does what's being told.' 
        
        if Worker:
            kubelet : Ships captain 
            kube-proxy, Enusre that container can talk to each other. 
            Container runtime Engine

    crictl : Container Runtime CLI , used to debug the container runtime. 


def etcd:

    Everything is stored here. After the change is updated here change is considered complete. Etcd default port is 2379

    etcd in ha , need to know about each other
