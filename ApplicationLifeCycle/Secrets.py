def secret:
    Create it and inject it can be created both imperative and declarative way.

        --from-literal=DB_Host=mysql

        Used to store sensitive infos. They are stored in an encoded format. 



        Don't specify the data in plain text, use the encoded format base64
        4'


        We can add one env variable or all secrets. 

        Secrets are not encrypted only encoded. Anyone can encode and decode it. 


        Secrets in etcd are not encrypted, but there are ways to do it, Do it in rest. Anyone able to create pods/deployments in the same ns can access the secrets. 



