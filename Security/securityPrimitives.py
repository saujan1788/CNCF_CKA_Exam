def kubeAPIServer:
    First priority should be to restrict access to the api server, only ssh based authentications are allowed


    if Authentication:
        Who can access unames, pwd, certs external auth LDAP and service accounts for services 

    if Authorization:
        RBAC is used to configure what kind of access. 


    All comms with apiServer is secured using TLS , comms from etcd cluster, kube proxy, kube scheduler, kubelet, controller manager. 



