# DS

This is the repo for the Data science part of the  team

A heroku API app is currently deployed to [Link](https://medcab6api.herokuapp.com/)

the app is using the application factory layout and has a posgresql server hosted

by heroku configured to the enviroment variable DATABASE_URL.

<div>

    Current endpoints:
    - /products/query : for getting specific cards from the database by name of strain in JSON
    - /products/fetch : for getting all of the cards in the database in JSON
    - /admin : the admin panel to rebuild models as needed
 </div>


