# CITS5505Project2

## How to set up

1. set up MySQL  
create a table named "cits5505", with charset utf8
```MySQL
CREATE SCHEMA `cits5505` DEFAULT CHARACTER SET utf8 ;
```
2. Configure your Mysql username and password in config.py
3. Database migrate  
```shell
flask db init
flask db migrate
flask db upgrade
```
After that, you will see some tables in your database.  
4. Run the application  
```shell
flask run
```
