

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