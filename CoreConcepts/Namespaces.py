def nameSpaces:

    Each Namespace can have its own resource limit kinda like a vlan in the networking term. There is a default NS and then we have a kube-system ns created by k8s and kube-public for the resources that needs to be public. 

    To set a ns as a default we can use the 

    kubectl config set-context $(kubectl config current-contxt) --namespace=dev

    Create a resoure quota file to limit the resources. 
