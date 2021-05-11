Getting started with SingleStore stored procedures and Python
=============================================================


Whether you're using an ORM or straight SQL, you can get started with SingleStore (formerly MemSQL) fast. Here's an introductory sample of using SingleStore stored procedures with Python. This sample includes all the CRUD methods: Create, Read by id, Read all, Update, and Delete.

Usage
-----

1. [Sign up](https://msql.co/2E8aBa2) for a free SingleStore license. This allows you to run up to 4 nodes up to 32 gigs each for free.

2. Spin up a SingleStore cluster. Choose the deployment strategy that makes sense to you:

   a. **Cloud**: Start a [Managed Service trial](https://msql.co/3iQ0SE8) and run `init.sql`.
   
   b. **VMs**: [Install SingleStore](https://msql.co/3ay2PCb) on a supported Linux distribution then run `init.sql`.
   
   c. **Containers**: Grab your license key from [SingleStore portal](https://msql.co/3fZoxjO) and set it into `docker-compose.yaml`. Then run `docker-compose up` to start the cluster and automatically run `init.sql`.

3. Run the example:

   a. In `main.py`, adjust `host`, `port`, `user`, and `password` to match your database connection details. For example, if running from containers, `host="localhost"` is perfect. If running from Managed Service, set the host to the client endpoint from the portal.
   
   b. `pip install mysql-connector-python`
   
   c. `python main.py`


License
-------

MIT
