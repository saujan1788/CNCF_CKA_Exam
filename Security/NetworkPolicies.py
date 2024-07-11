def NetworkPolicies:
    Ingress and Egress rules must be defined if a specific need is there. Need to create a netowrk policy object and label it with the pod. 

    We can define an ingress rule to say podselctor and match a lable or namespace and match namespace if traffic is coming outside from the k8s cluster we can define an ipBlock too like : 192.168.0.1/24
    
    We can define and/or rules like from prod namespace and name must be api-pod if we want or then define a unique block for the rule. 


    if egress:
        we can send traffic outside of our cluster using egress say to define ip, protocol and port.
