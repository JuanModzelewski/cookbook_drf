<a name="Top"></a>
<h1> Manual testing </h1>

[Back to Readme](/README.md#manual-testing)

In manual testing data was entered in the backend using both the front-end and back-end to test the API's general functionality.
All data is appropriately providing CRUD Functionality.

| Testcase                                                                     | Expected Result                                                                                             | Test Result |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| **Profiles**                                                                 |                                                                                                             |             |
| [Profile List](https://cookbook-drf-api-d322c7998986.herokuapp.com/profiles/)         |                                                                                                    |             |
| GET Unauthenticated                                                          | returns 200 response: a list of all the profiles                                                            | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: a list of all the profiles                                                            | ✅ PASS     |
| POST, PUT, DELETE                                                            | not provided                                                                                                | ✅ PASS     |
| [Profile Details](https://cookbook-drf-api-d322c7998986.herokuapp.com/profiles/)         |                                                                                                    |             |
| GET Unauthenticated                                                          | returns 200 response: the profile identified by id                                                           | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: the profile identified by id                                                           | ✅ PASS     |
| PUT Unauthenticated                                                          | returns 403 error: trying to edit profile identified by id as unauthenticated user                           | ✅ PASS     |  
| POST, DELETE                                                                 | not provided                                                                                                | ✅ PASS     |
| **Recipes**                                                                 |                                                                                                              |             |
| [Recipe List](https://cookbook-drf-api-d322c7998986.herokuapp.com/recipes/)         |                                                                                                      |             |
| GET Unauthenticated                                                          | returns 200 response: the recipe identified by id                                                           | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: the recipe identified by id                                                           | ✅ PASS     |
| POST Unauthenticated                                                          | returns 200 response: the recipe form is hidden below the recipe list                                     | ✅ PASS     |
| POST Authenticated                                                            | returns 200 response: allows authenticated users to create a recipe at the bottom of the recipe list       | ✅ PASS     |
| POST, DELETE                                                                 | not provided                                                                                                | ✅ PASS     |
| **Recipe Details**                                                                 |                                                                                                       |             |
| [Recipe List](https://cookbook-drf-api-d322c7998986.herokuapp.com/recipes/52/)         |                                                                                                   |             |
| GET Unauthenticated                                                          | returns the recipe identified by id                                                                         | ✅ PASS     |
| GET Authenticated                                                            | returns the recipe identified by id                                                                         | ✅ PASS     |
| PUT Unauthenticated                                                          | not provided                                                                                                | ✅ PASS     |
| PUT Authenticated Owner                                                      | allows recipe owner to update the recipe                                                                   | ✅ PASS     |
| PUT Authenticated Not Owner                                                  | not provided                                                                                               | ✅ PASS     |
| DELETE Authenticated Owner                                                   | allows recipe owner to delete the recipe                                                                   | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | delete not present                                                                                          | ✅ PASS     |
| DELETE Unauthenticated                                                       | delete not present                                                                                           | ✅ PASS     |
| POST                                                                         | not provided                                                                                           | ✅ PASS     |
| **Favorites**                                                                 |                                                                                                            |             |
| [Favorites](https://cookbook-drf-api-d322c7998986.herokuapp.com/favorites/)|                                                                                                             |             |
| GET Unauthenticated                                                          | returns a list of favorite id, owner, created_at, and recipe                                                | ✅ PASS     |
| GET Authenticated                                                            | returns a list of favorite id, owner, created_at, and recipe                                                | ✅ PASS     |
| POST Unauthenticated                                                         | form to add to favorites not present                                                                       | ✅ PASS     |
| POST Authenticated                                                           | allows user to add a specified recipe to favorites                                                         | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | delete option not present                                                                                 | ✅ PASS     |
| DELETE Authenticated Owner                                                   | allows favorite owner to delete favorite                                                                   | ✅ PASS     |
| DELETE Unauthenticated                                                       | delete option not present                                                                                  | ✅ PASS     |
| POST                                                                         | not provided                                                                                           | ✅ PASS     |
| **Reviews**                                                                 |                                                                                                            |             |
| [Reviews](https://cookbook-drf-api-d322c7998986.herokuapp.com/reviews/)|                                                                                                             |             |
| GET Unauthenticated                                                          | returns a list of reviews                                                                                  | ✅ PASS     |
| GET Authenticated                                                            | returns a list of reviews                                                                                  | ✅ PASS     |
| POST Unauthenticated                                                         | form to add to review not present                                                                       | ✅ PASS     |
| POST Authenticated                                                           | form is displayed at the bottom of the review list                                                       | ✅ PASS     |
| DELETE Authenticated Not Owner                                               | delete option not present                                                                                 | ✅ PASS     |
| DELETE Authenticated Owner                                                   | allows user to delete review                                                                   | ✅ PASS     |
| DELETE Unauthenticated                                                       | delete option not present                                                                                  | ✅ PASS     |
| PUT Authenticated Not Owner                                                   | editing option not present                                                                                 | ✅ PASS     |
| PUT Authenticated Owner                                                   | allows user to update review                                                                   | ✅ PASS     |
| PUT Unauthenticated                                                       | editing option not present                                                                                  | ✅ PASS     |

[Back to top](#Top)<br>

[Back to Readme](/README.md#manual-testing)