def ManualScheduling:
    Each pod definition has a field NodeName created by K8s. If there is no scheduler pods will be in pending state, Define the nodename on the pod , Once pod is create we can't edit this property.' If a pod is already created we need to send a post request by creating a binding file. 

    if podSelection:
        kubectl get all --selector env=prod

def TaintsAndTolerations:
    Taint and Tolerance , Taint is applied on Node, TOleration on Nodes, If a pod can tolerate the node it can be placed. If no tolerance is defined pods can't be tolerated on any nodes.' 

    There are three values on tainting a node. No Schedule, PreferNoSchedule and No Execute.

    if NoSchedule: Pods won't be scheduled at all if can't tolerate.

    elif PreferNoSchedule: As the name indicates.

    else NoExecute: No new pods will be scheduled and existing pods will be evicted if can't tolerate. 


    Taints and toleration doesn't tell a pod it must be placed on that node its more line on a ndoe what pods do you want to accept, if taint = blue only pods with blue toleration but if a pod has blue toleration and other nodes have no taints that pod can be placed on those nodes too. 

    kubectl taint node node01 spray=mortein:NoSchedule


