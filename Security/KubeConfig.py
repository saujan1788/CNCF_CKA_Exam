def kubeConfig:
    by default it's in user home dir, in .kube dir '.


    It has 3 sections, 

    if Cluster:
        Diff kind of clusters, like dev prod , testing,
        Cert details should be defined as well. Instead of giving the file path we can give the encoded data itself.  
    elif Contexts:
        Context define which user manage which clusters, Like admin@dev, saujan@prod 
        We can define a namespace for a certain context as well
    else users:
        users like admin, dev, prod 

