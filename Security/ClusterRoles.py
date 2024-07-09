def ClusterRoles:
    Role and rolebinding are created within a namespace, IF no ns is defined default ns is used. 

    If Node:
        Can't use with namespace as they are cluster wide'

    so resource are ns or cluster scoped. 


    if ClusterScoped:
        Resources include nodes, PV, clusterroles, clusterrolebindings, certificatesigningrequests, namespaces


        We can create roles like, CLusterAdmin, StorageAdmin, After creating the role bind it to a user by creating a role binding called cluster role binding. 


