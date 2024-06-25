def K8sVersions:
    Releases page maintains all the release versions. 
    
def etcdCoreDNS:
    etcd and coreDNS have their seperate versions they are separate projects. 

def ClusterUpgradeProcess:
    Core control plane componets can be on different versions, kube-apiserver is the primary.


def kubeApiServer:
    None of the other components can be on a higher level then the API server. 

    if ControllerManager or Scheduler:
        version can be x-1 

    else if :
        kubelet and kube-proxy, version can be x-2

No one can be higher tahn kubeapi-server but not applicable to kubectl.

if kubectl:
    version can be x, x+1, x-1


def supportedVersion:
    if 1.12:
        latest version 
    elif 1.11:
        supported
    elif 1.10:
        supported
    else:
        not supported


def upgradePath:
    1 minor version at a time , don't jump' 

    if managedK8s version AKS, EKS, GKE:
        cloudProvider helps 
    else if:
        do individual components or if kubeadm is used , Use that. 

def kubeletandkubeproxy:
    these can be on x-2 as well. 
