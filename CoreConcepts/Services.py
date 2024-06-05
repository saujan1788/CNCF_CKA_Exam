def services:
    Helps to connect application with other application or users. Used to establish connection. 

    K8s listens for requests on Node on a specific ports and then forwards the requests. 

    if NodePort_Service:
        This is a case where there is a open port in Node and forward request to pod. 

    if ClusterIp:
        Service creates a virtual IP inside the cluster, to allow comss of different services. 

    if LoadBalancer:
        Provisions a LB for supported cloud providers. 


def NodePort:
    TargetPort: 80, This is the pod on the port where the application is exposed. 
    Port: This is the port exposed on the service, this is mapped to the port on POD.

    Service has its own IP in the cluster, 

    NodePort: Port on the node itself, which we use to access the service. 


    port is compulsary when defining a service file, if no other used then a free port in range 30000 - 32767 is used and targetport will be same as port. 

def ClusterIP:
    So bascially create a service which has an IP and behind that there are pods which have their own IP. So request is mapped from the cluster to the pods, Like for a tair service if there is 100db pods , map the 100 db pods ip with a clusterSerice IP and knowing the clusterIP is enough.

def LoadBalancer:
    Instead of exposing an IP and port of each node for a web application, use loadbalancer only works with cloud providers. 


