**Generate Token**
----
  Returns json data about a token for the user to be passed-in every request in header.

* **URL**

  /generateToken

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
    `username=[string]`
    `password=[string]`


* **Header Params**
   `Not required`
  

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** '{"token": "2023891394667c182ecbd222054338a9118ff11d",
                   "message": "Use this generated Token with Authorisation : Token 2023891394667c182ecbd222054338a9118ff11d"}'
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'error': 'Invalid Credentials'}`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {'error': 'Please provide both username and password'} `

<!-- ///////////////////////////////////////////////////////////////// -->

**Create blog**
----
  Returns json data about blog creation.

* **URL**

  /createblog

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
    `title=[string]`
    `image=[file]`
    `description=[string]`
    **Examples** 

    `title = Your blog title`
    `image= image file`
    `description= your blog content `

  
* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message":"Blog Created Successfully"}`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Some Error Occured in Blog Creation Contact admin"} `

<!-- ///////////////////////////////////////////////////////////////// -->

**Update blog**
----
  Returns json data about blog updation.

* **URL**

  /updateblog

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
    `blogid=[integer]`
    
    **Optional:**
    `title = [string]`
    `image=[file]`
    `description=[string]`
    
    **Examples** 
    `blogid = 1`
    `title = Your blog title`
    `image= image file`
    `description= your blog content `
* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message":"Blog Updated Successfully"}`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Blog not available with the given Blog-Id"} `


<!-- ///////////////////////////////////////////////////////////////// -->

**Delete blog**
----
  Returns json data about blog soft deletion.

* **URL**

  /deleteblog

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
    `blogid=[integer]`
    `delete=[Boolean]`

    **Examples** 
    `blogid = 1`
    `delete = True`
    **Optional:**
    None`

* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message":"Blog Deleted Successfully"}`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Blog not available with the given Blog-Id"} `

<!-- ///////////////////////////////////////////////////////////////// -->

**Search blog**
----
  Returns json data about searched blog.

* **URL**

  /searchblog

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
    `title=[string]`

    **Examples** 
    `title = any string here`

    **Optional:**
    None`

* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[["test title update","test description update"],["test title for slug with update","test description for slug"],["test title for slug UPADTE","test description for slug with update"],["test title for slug with update view","test description for slug with update"],["test title final update","test description final"],["test title final update","test description final"]]`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Searched blog is not in the Database. Maybe it was deleted by You"} `

<!-- ///////////////////////////////////////////////////////////////// -->

**Publish blog**
----
  Returns json data about blog publishing.

* **URL**

  /publishblog

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
    `blogid=[integer]`
    `publish=[Boolean]`

    **Examples** 
    `blogid = 1`
    `publish = True`
    
    **Optional:**
    None`

* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"message":"Blog Published Successfully"}`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Blog not available with the given Blog-Id"} `

<!-- ///////////////////////////////////////////////////////////////// -->

**View All blog**
----
  Returns json data about all blog .

* **URL**

  /viewallblog

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
    None
    **Examples** 
    None
    
    **Optional:**
    None`

* **Header Params**
    `Authorization: Token <the token received>`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{"blogid":1,"title":"test title update","description":"test description update","createdDate":"2021-02-18T18:09:15.883652Z","published":false,"isDelete":false,"lastUpdated":null},{"blogid":2,"title":"test title for slug with update","description":"test description for slug","createdDate":"2021-02-20T06:35:23.903700Z","published":false,"isDelete":false,"lastUpdated":null},{"blogid":3,"title":"test title for slug UPADTE","description":"test description for slug with update","createdDate":"2021-02-20T07:03:43.490911Z","published":true,"isDelete":false,"lastUpdated":null},{"blogid":4,"title":"test title for slug with update view","description":"test description for slug with update","createdDate":"2021-02-20T07:08:39.566383Z","published":true,"isDelete":false,"lastUpdated":null},{"blogid":5,"title":"test title final update","description":"test description final","createdDate":"2021-02-20T07:24:43.166936Z","published":false,"isDelete":false,"lastUpdated":null},{"blogid":6,"title":"test title final update","description":"test description final","createdDate":"2021-02-20T08:18:24.705200Z","published":false,"isDelete":false,"lastUpdated":null}]`

  * **Code:** 400 BAD REQUEST <br />
    **Content:** ` {"message":"Some error occurred while fetching blog"} `
