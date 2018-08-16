
delete_query = '''
                mutation{
                deleteRecipe(recipeId:8){
                    message 
                }
                }
                '''

delete_response = {
                    "data": {
                        "deleteRecipe": {
                        "message": "Recipe with id 8 has been deleted"
                        }
                    }
                    }

all_recipes = '''
                    query{
                    allRecipes{
                        id
                        recipeTitle
                        recipeDescription
                        }
                    }
                    '''

all_recipes_response = {
                        "data": {
                            "allRecipes": [
                            {
                                "id": "5",
                                "recipeTitle": "Rolex",
                                "recipeDescription": "Eggs",
                            }
                            ]
                        }
                        }

create_query = '''
                    mutation{
                    createRecipe(
                        categoryId:7,
                        recipeTitle:"Luwombo",
                        recipeDescription:"Chicken"
                    ){
                        recipe{
                        recipeTitle
                        recipeDescription
                        }
                    }
                    }
                    '''

create_query_response = {
                            "data": {
                                "createRecipe": {
                                "recipe": {
                                    "recipeTitle": "Luwombo",
                                    "recipeDescription": "Chicken"
                                }
                                }
                            }
                            }


update_query = '''
                   mutation{
                        updateRecipe(
                            recipeId:8,
                            recipeTitle:"Uga Roll",
                            recipeDescription:"Another Rolex"
                        ){
                            recipe{
                            recipeTitle,
                            recipeDescription
                            } 
                        }
                        }
                    '''

update_query_response = {
                            "data": {
                                "updateRecipe": {
                                "recipe": {
                                    "recipeTitle": "Uga Roll",
                                    "recipeDescription": "Another Rolex"
                                }
                                }
                            }
                            }