from pydantic import BaseModel

#Input and Output pydantic models inherting Basemodel 


class Input(BaseModel):
    text: str
    model:str


class Output(BaseModel):
    cancer_type: str

    