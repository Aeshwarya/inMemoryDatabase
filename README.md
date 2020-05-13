# InMemoryDatabase
A simple python flask application for storing KEY-VALUE in-memmory on distributed nodes.
Cache Eviction algorithm is LRU. Also, the replicas are guranteed to be consistent but may contain different keys for some period of time because the LRU eviction is determined on the basis of the GET request on the particular node. https://github.com/Aeshwarya/inMemoryDatabase/blob/master/cache_architecture.png


### How to run
1. Install Python3 on machine
2. Install pip3
// Installing requirements
3. pip3 install flask
4. pip3 install requests

5. Now, change config file https://github.com/Aeshwarya/inMemoryDatabase/blob/master/app/cacheConfig.py  with appropriate ports and server
6. Leave CURRENT_SERVER  for now, it is not used as of now but can be used in multi machine deployment
7. Now open a terminal and run following command(change command if you have modified the config file):
    `python3 run.py 2222 server1`
8. Similar to step 7 open two other terminal and run the following command on the both terminals respectively
    `python3 run.py 2223 server2`
    `python3 run.py 2224 server3`
9. Now for testing, open another terminal and run following command
   `python3 test.py`
10. The CLI will ask for
      a. PORT: <Enter the port which you want to connect to>
      b. OPERATION: SET/GET/DELETE
      c. KEY: <The key to be SET/GET/DELETED>
      d. VALUE: <The value for key>(Only in case of SET)
11. Play around with CLI
12. The code handles Node crashing and coming back(To test you can go to any of the previous terminal exit the running application and rerun the command to run the node
