def kubeControllerManger:
    NodeController : CHecks the status of nodes, If no heartbeat is received in 45s then Node is considered not healthy. 

    ReplicationController: Check the status of replica sets, Makes sure desired replica sets is mentioned. 


     There are a lot of controllers not just node and replica set. 

     kube-controller has a pod in kube-system ns. 


def kubeScheduler:
    Decides which pods goes to which nodes, Won't place the pods but decides which pods go where, it's kubelets that places the pods. 

    Filters the nodes based on the resource requirements like how much cpu does it need and how much cpu does a node have. 

    Ranks Nodes as well the one which is least used is higher rank. 

def kubelet:
    Captain of the ship, Does all the paperwork to be part of the cluster. 

def kubeProxy:
    Pod has a separate network, Service is not like a conatienr, It's a virtual thing only on k8s memory'. kube-proxy is a process that runs on each node on k8s cluster, it looks for new services , proxy uses iptables and creates rule to do traffic forwarding. 

def ReplicaController:
    Helps to maintain a certain number of replicas.
