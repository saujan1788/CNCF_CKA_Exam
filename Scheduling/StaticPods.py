def StaticPods:
    Imagine a situation where there is only kubelet and no controlPlane components of k8s. Kubelet can schedule the pods itself if the pod definition file is present in /etc/kubernetes/manifests, Kubelet checks this location periodically. All the pod files on the node will be here. 


if StaticPods:
    These are the pods created by kubelet itself without any interaction with the kubeapi server. Kubelet works at a pod level and can only understand pod not deployments or RS. 

    Checke the kubelet service to find the path for the above manifest files, look for config option or look for config file and look for static pod path.

    docker ps will list the pods created in this way, kubectl won't work as no control plane components.'

def UseCase:
    We can use this to create control plane components. Create yml files for apiserver, etcd and controller manager keep the file in /etc/kubernetes/manifests and then kubelet will create the pods. kubeadm uses this approach.


