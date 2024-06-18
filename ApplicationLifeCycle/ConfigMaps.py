def ConfigMap:
    Config maps are used to pass data as a key value pair in k8s. Image where a set of values needs to be shared across 100 pods instead of defining that in 100 locations , Define once and reference it. Comes with all sort of cental mmgt advantages. 

    if configMap:
        Create the config map and then inject it to the pod. Two ways imperative and declarative. 

         kubectl create configmap \
                 app-config --from-literal= APP_COLOR=blue
                            --from-literal = APP_MOD=prod


    Creating a config map file is better 

    apiVersion: v1
    kind:
    metadata:
        name: app-config
    data:
        APP_COLOR=blue
        APP_MODE= prod



    if configMapCreated and inject in pod:
        Add the envFrom property: 
            - configMapRef:
                name: app-config

    We can reference one value as well if needed not the whole file, for example 

    if onlyOneValue:
        valueFrom:
            configMapKeyRef:
                name: app-config
                key: APP_COLOR


