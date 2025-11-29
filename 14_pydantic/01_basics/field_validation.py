from pydantic import BaseModel, field_validator, model_validator
class User(BaseModel):
    username: str

    @field_validator("username")
    def username_must_not_contain_space(cls, v):
        if " " in v:
            raise ValueError("username must not contain space")
        return v
    
    @field_validator("username")
    def username_must_not_contain_special_characters(cls, v):
        if "!" in v:
            raise ValueError("username must not contain special characters")
        return v
    
    @field_validator("username")
    def username_must_not_contain_numbers(cls, v):
        if "1" in v:
            raise ValueError("username must not contain numbers")
        return v
    
    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 5:
            raise ValueError("username must be at least 5 characters long")
        return v

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords do not match")
        return self


# try:    
#     user = User(username="pulkit.gupta!")
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)    

try:
    data=SignupData(password="12345", confirm_password="12345")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

