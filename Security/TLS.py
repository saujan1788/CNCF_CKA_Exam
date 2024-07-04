def tls:
    In K8s setup clients need to verify who they say they are, so a server can ask for client's c$rt as well.'


def ServerCerts:
    if kube-apiServer or etcdServer or KubeletServer:
        They have their own public and private key. 

def clientCerts:
    if admin or kubeScheduler or kubeController or kubeProxy:
        They all need their own key pairs as well they need to prove who the're in a normal case client don't need to prove their identity. 

def interServerComms:
    Of all the components only apiserver can communicate with etcd. ETCd needs to authenticate the apiserver as well. 


def CA:
    We need a CA to sign all these certs and better to seperate etcd server ca and other certs. CA will have it's own pair or key and certs as well.'.

def kubelet:
    Each node on the cluster will need a cert to communicate with the apiServer as well. kubelet has a client and a server cert.

    To arrange the perms for the nodes , create a group seperate for the nodes and assign the perms there. 
