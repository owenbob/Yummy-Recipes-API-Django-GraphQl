

create_user_query = '''
                mutation{
                createUser(
                    username:"bobby",
                    email:"bob@gmail.com",
                    password:"123"
                ){
                    user{
                    username
                    email
                    }  
                }
                
                }
                '''

create_user_query_response = {
                                "data": {
                                    "createUser": {
                                    "user": {
                                        "username": "bobby",
                                        "email": "bob@gmail.com",
                                    }
                                    }
                                }
                                }

get_all_users_query = '''
                    {
                    users{
                        username
                        email
                    }
                    }
                    '''


get_all_users_response = {
                            "data": {
                                "users": [
                                {
                                    "username": "Jackson",
                                    "email": "jacks@gmail.com"
                                }
                                ]
                            }
                            }
