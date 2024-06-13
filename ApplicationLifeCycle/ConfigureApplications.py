def ConfigureApplications:
    Different ways to giving a commonad on docker file, 

    From Ubunutu
    CMD sleep 5

    docker build -t ubunutu-sleeper .

    docker run ubuntu-sleepers



 If I want to run a command at startup , 

 docker run ubunut-sleepr sleep 10. but if I want to run with just the value 10 , This is where EntryPoint comes in 


if ENTRYPOINT:
    This is like command , When the container starts this program will run.


    FROM UBUNTU

    ENTRYPOINT ["sleep"]

    
    ->  docker run ubunut-sleepr 10

    Now 10 will be appended to entrypoint. 

    If no value is passed in the parameter, We can set a default value as well. In this case we use both EntryPoint and CMD.

    FROM Ubuntu

    ENTRYPOINT ["sleep"]

    CMD ["5"]


    If any command passed during execution then that takes priority if not then uses the default value. 
