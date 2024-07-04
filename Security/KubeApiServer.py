def APIGroups:
    old version was v1, now k8s is moving to named api groups. 

    /apps /extensions, /networking.k8s.io, /storage.k8s.io, authentication.k8s.io, /certificates.k8s.io : API Groups 

    Any call to the API server needs to be authenticated. 


    All resources in k8s are grouped into different api groups, At top level there is core and named apigroups and each api groups has its own types of resources. 


