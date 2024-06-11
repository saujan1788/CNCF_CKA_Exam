def ResourceLimit:
    CPU and Memory limits can be defined. 1CPU and 1GiM this is the minimum amount of resource required. 



if CPULimit:
    1vCPU,1Core = 1 CPU

    we can defined 1vCPU limit and only 1 vCPU will be used. Need to use limits section in yaml file. A container cannot use more CPU resources than its limit.  

    A container can use more memory than it has been allocated. IfF that happens frequently pods will crash with OOM error. 

By default , there is no request or limit on the pods 
By default , there is no request or limit on the pods 

once memory is assigned to a pod we can't throttle it we have to kill it and retrieve it.'

LimitRange: We can define max, min and default value for pod. default.mem = 1Gi, max.me = 1Gi, min.me = 500Mi, for memory and for CPU default = 500m, max =1, min = 100m


What if we want all the pods cannot use more than 85% of resources, for this we can define resouece quota on the namespace level. This defines the max resource that can be used in the NS 

