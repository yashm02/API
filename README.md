# API

The above description outlines a backend structure for a Django project, which includes three tables: Client, Artist, and Work. Client table has a name field and a foreign key to the User instance. Artist table has a name field and a many-to-many relationship with the Work table. Work table has a link field and a work type field with three possible values: Youtube, Instagram, and Other.

Additionally, a REST API is created with several endpoints:

1. GET /api/works: This endpoint returns a list of all works with their details such as link and work type.

![image](https://user-images.githubusercontent.com/102669147/221287350-5187b948-0f10-404e-a9dc-569a7d70a5d1.png)

2. GET /api/works?artist=[Artist Name]: This endpoint returns a list of works filtered by artist name.

![image](https://user-images.githubusercontent.com/102669147/221287252-43874962-a141-4aab-a81e-f9440aef224f.png)

3. GET /api/works?work_type=Youtube or pk of YouTube: This endpoint returns a list of works filtered by work type.

![image](https://user-images.githubusercontent.com/102669147/221287409-1afd0bc2-3ca5-4242-a1f0-674a0c4cc340.png)

4. POST /api/register: This endpoint allows users to register by providing their username and password in the request body.


