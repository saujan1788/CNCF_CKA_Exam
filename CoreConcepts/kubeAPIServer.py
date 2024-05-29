def kubeapiserver:
    when we run kubectl, it talks to kubeapi server, request is first authenticated and then validated.

    kube-api server only interacts directly with the etcd , other interact to etcd via the kube-api server. 

def kubescheduler:
    It monitors the api server and realises a new pod with no node is present find rgiht node and tells the apiserver and then apiserver updates the etcd db and then kubelet creates the new pod on the node. 
