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
| POST, PUT, DELETE                                                            | Not provided                                                                                                | ✅ PASS     |
| [Profile Details](https://cookbook-drf-api-f6a1e9bf2c65.herokuapp.com/profiles/)         |                                                                                                    |             |
| GET Unauthenticated                                                          | returns 200 response: the profile specified by id                                                           | ✅ PASS     |
| GET Authenticated                                                            | returns 200 response: the profile specified by id                                                           | ✅ PASS     |
| PUT Unauthenticated                                                          | returns 403 error: trying to edit profile specified by id as unauthenticated user                           | ✅ PASS     |  
| POST, DELETE                                                                 | Not provided                                                                                                | ✅ PASS     |



[Back to top](#Top)<br>

[Back to Readme](/README.md#manual-testing)