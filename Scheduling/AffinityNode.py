def NodeAffinity:
    We can use operations other than and like or notIN and so on. 

Existing:
    if requiredDuringSchedulingIgnoreDuringExecution: 

    if preferredDuringSchedulingIgnoredDuringExecution:

Planned:
    if requiredDuringSchedulingRequiredDuringExecution

    if preferredDuringSchedulingRequiredDuringExecution






    it has different types of operators like exists, in or and and more. 


    If there are no pods matching the label on the pods. 


DuringScheduling -> Pods does not exist yet , Pod is about to be created and rules will take effect, If nodes with no matching labels are availed then pods is not scheduled unless preferred where the rule can be ignored and pod can be placed, Try your best to place the pod on the matching node.


DuringExecution -> Pod has been running and change has been made which.  


NodeAffinity  and Taints.Tolerations are used together to achieve goals like only certain pods can be placed in certain nodes. 


