def CAServerAPI:

    Usually all the certs are on master server itself, But when things grow we need to manage it automated way. We can automate the cert process. 


    Need to create a CSR request object, 

    After the object is created, need to do kubectl certificate approve jane(name of the cert)

    if ControllerManager:
        looks after the certificate related operations. There are controllers such as CSR approving , csr signing. 
