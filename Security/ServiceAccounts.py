def serviceAccount:
    Two types of account user and service.

    Things like Prometheus , Jenkins uses service accounts. 


    Service account will need a token which is stored in a secret object and the secret object is linked to the service account.


    A default service account is created in each namespace. Secret is mounted as a volume if running within the same cluster in most cases. 

    Service account of an existing pod cannot be changed need to recreate and change it. 

    k8s will mount default service account by default. 



    if 1.22 and 1.24:
        Few things changed since these version, Each ns has a default SA and has a token associated with it. when pod is created this secret is mounted. 

        Token was valid as long as the account was valid. After 1.22 there is TokenRequestAPI, which makes things more secure. Tokens are Audiencebound, TimeBound and ObjectBound. 

        After 1.24: 
            We can still create non expiring tokens  by creating a secret object and assocaite with a service account and the required api 


            Only create service account token secret object if you can't use TokenRequest API'.
