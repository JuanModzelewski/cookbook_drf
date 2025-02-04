<a name="Top"></a>
<h1> Manual testing </h1>

[Back to Readme](/README.md#manual-testing)

Manual Testing for the overall functionality of the API was performed by entering dummy data in the backend both via Backend-and Front-end.
All data is CRUDed accordingly.

Screenshots have been taken borth in local production and in deployed version to display that everything is working as expected.
The screenshots during testing is taken in local production to more specifically show the auth and unauth results for the api and to properly display that everything is working. 
Images from the deployed api and the admin django panel can be found [here](#deployed-admin-screens)

| Testcase                                                                     | Expected Result                                                                                             | Test Result |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| **Profiles**                                                                 |                                                                                                             |             |
| [Profile List](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/profiles/)         |                                                                                                    |             |
| GET Unauthenticated                                                          | returns 200 response: a list of all the profiles                                                            | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: a list of all the profiles                                                            | ✅ PASS     |
| POST, PUT, DELETE                                                            | not provided                                                                                                | ✅ PASS     |
| [Profile Details](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/profiles/)         |                                                                                                    |             |
| GET Unauthenticated                                                          | returns 200 response: the profile identified by id                                                           | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: the profile identified by id                                                           | ✅ PASS     |
| PUT Unauthenticated                                                          | returns 403 error: trying to edit profile identified by id as unauthenticated user                           | ✅ PASS     |  
| POST, DELETE                                                                 | not provided                                                                                                | ✅ PASS     |
| **Recipes**                                                                 |                                                                                                              |             |
| [Recipe List](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/recipes/)         |                                                                                                      |             |
| GET Unauthenticated                                                          | returns 200 response: the recipe identified by id                                                           | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: the recipe identified by id                                                           | ✅ PASS     |
| POST Unauthenticated                                                          | returns 200 response: the recipe form is hidden below the recipe list                                     | ✅ PASS     |
| POST Authenticated                                                            | returns 200 response: allows authenticated users to create a recipe at the bottom of the recipe list       | ✅ PASS     |
| POST, DELETE                                                                 | not provided                                                                                                | ✅ PASS     |
| **Recipe Details**                                                                 |                                                                                                       |             |
| [Recipe List](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/recipes/52/)         |                                                                                                   |             |
| GET Unauthenticated                                                          | returns the recipe identified by id                                                                         | ✅ PASS     |
| GET Authenticated                                                            | returns the recipe identified by id                                                                         | ✅ PASS     |
| PUT Unauthenticated                                                          | not provided                                                                                                | ✅ PASS     |
| PUT Authenticated Owner                                                      | allows recipe owner to update the recipe                                                                   | ✅ PASS     |
| PUT Authenticated Not Owner                                                  | not provided                                                                                               | ✅ PASS     |
| DELETE Authenticated Owner                                                   | allows recipe owner to delete the recipe                                                                   | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | delete not present                                                                                          | ✅ PASS     |
| DELETE Unauthenticated                                                       | delete not present                                                                                           | ✅ PASS     |
| POST                                                                         | delete not present                                                                                           | ✅ PASS     |
| **Favorites**                                                                 |                                                                                                            |             |
| [Recipe List](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/favorites/)|                                                                                                             |             |
| GET Unauthenticated                                                          | returns a list of favorite id, owner, created_at, and recipe                                                | ✅ PASS     |
| GET Authenticated                                                            | returns a list of favorite id, owner, created_at, and recipe                                                | ✅ PASS     |
| POST Unauthenticated                                                         | form to add to favorites not present                                                                       | ✅ PASS     |
| POST Authenticated                                                           | allows user to add a specified recipe to favorites                                                         | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | form not present to delete                                                                                 | ✅ PASS     |
| DELETE Authenticated Owner                                                   | allows favorite owner to delete favorite                                                                   | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | not provided                                                                                               | ✅ PASS     |
| DELETE Unauthenticated                                                       | not provided                                                                                                | ✅ PASS     |
| POST                                                                         | not provided                                                                                                | ✅ PASS     |
[Back to top](#Top)<br>

[Back to Readme](/README.md#manual-testing)