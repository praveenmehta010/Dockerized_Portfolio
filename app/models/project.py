# from datetime import datetime
# from pydantic import BaseModel, PositiveInt


# class User(BaseModel):
#     id: int  
#     name: str = 'John Doe'  
#     signup_ts: datetime | None  
#     tastes: dict[str, PositiveInt]  


# external_data = {
#     'id': 123,
#     'signup_ts': '2019-06-01 12:22',  
#     'tastes': {
#         'wine': 9,
#         b'cheese': 7,  
#         'cabbage': '1',  
#     },
# }

# user = User(**external_data)  

# print(user.id)  
# #> 123
# print(user.model_dump())  
# """
# {
#     'id': 123,
#     'name': 'John Doe',
#     'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
#     'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
# }
# """

from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt

class Project(BaseModel):
    title : Annotated[
        str, 
        Field(
            max_length=20,
            description="Name of the project",
            examples=["something app"]
        )
        ]
    title : str = "Default_Name"
    description : str = "default@gmail.com"
    tech_stack : list = ["default"]
    github_link : str = "Default Message"
    live_link : str = "unread"
    featured : bool = True
    created_at : datetime | None
    