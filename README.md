# CITS5505Project2

## How to set up

1. set up MySQL  
create a table named "cits5505", with charset utf8
```MySQL
CREATE SCHEMA `cits5505` DEFAULT CHARACTER SET utf8 ;
```
2. flask migrate  
```shell
flask db init
flask db migrate
flask db upgrade
```
After that, you will see some tables in your database.  
3. Run the application  
```shell
flask run
```

