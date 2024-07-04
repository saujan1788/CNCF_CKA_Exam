def Auth:
    Once a user/service gets access what kind of opertaions do we want to allow. 

    We define different types of roles and associate users with the roles. 



    if webHook:
        If need to managed externally , there are tools like open policy agent. They decide if the user is permitted or not. 

    Diff auth modes like always allow and always deny adn so on or node , rbac, webhook, if multiple defined checks the order the auth mode is set on , Node -> RBAC - > WebHook
