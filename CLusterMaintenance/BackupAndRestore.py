def Backup:
    If backup is need then we can do:
        kubectl get all -all-namespaces -o yaml > all-deploy-services.yaml

    VELERO:
        Helps us to take k8s backup 

        These options query the API server.


def etcd:
    all info are stored here, If we need to backup our etcd. --data-dir=/var/lib/etcd this is the dir where all the data is stored.

    we can take snapshot of etcd, etcdctl snapshot save snapshot.db 

    We can restore the cluster using this snapshot. 



Backup via API Server vs Backup via etcd

if no access to etcd backup via apiserver.


