
create_query = '''
                mutation{
                createCategory(
                    userId:"2"
                    categoryTitle:"Breakfast",
                    categoryDescription:"First meal of the day"
                    ){
                    category{
                    id
                    categoryTitle
                    categoryDescription
                    }
                }
                }
                '''


create_query_response = {
                            "data": {
                                "createCategory": {
                                "category": {
                                    "id": "3",
                                    "categoryTitle": "Breakfast",
                                    "categoryDescription": "First meal of the day"
                                }
                                }
                            }
                            }



update_query = '''
                    mutation{
                    updateCategory(
                        id:4,
                        categoryTitle:"Lunch",
                        categoryDescription:"Second Meal of the day"
                        ){
                        category{
                        id
                        categoryTitle
                        categoryDescription
                        }
                    }
                    }
                    '''

update_query_response = {
                            "data": {
                                "updateCategory": {
                                "category": {
                                    "id": "4",
                                    "categoryTitle": "Lunch",
                                    "categoryDescription": "Second Meal of the day"
                                }
                                }
                            }
                            }

delete_query = '''
                mutation{
                    deleteCategory(id:4){
                        message
                    }
                    }
'''

delete_query_response = {
                            "data": {
                                "deleteCategory": {
                                "message": "Category with id 4 has been deleted"
                                }
                            }
                            }


all_categories = '''
                    {
                    allCategories{
                        id
                        categoryTitle
                        categoryDescription
                    }
                    }
                    '''

all_categories_response = {
                            "data": {
                                "allCategories": [
                                {
                                    "id": "1",
                                    "categoryTitle": "Breakfast",
                                    "categoryDescription": "First meal of the day",
                                }
                                ]
                            }
                            }