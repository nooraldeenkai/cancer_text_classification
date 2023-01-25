from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
import pytest


client = TestClient(app)


#list of testing inputs
test_inputs = [("Hur mår du?", {'language':"Sweedish"}), ("Hey there how are you ?", {'language':"English"}),("Comment allez-vous ?", {'language':"French"}), ("എങ്ങനെയിരിക്കുന്നു", {'language':"Malayalam"}),
               ("как дела?", {'language':"Russian"}), ("எப்படி இருக்கிறீர்கள்?", {'language':"Tamil"}), ("كيف حالك", {'language':"Arabic"}), ("wie gehts?", {'language':"German"})]


#test if healthcheck endpoint is working fne
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'healthcheck': 'OK'}



#test if language endpoint is working fine , tests the iutput and status code
#using pytest parametrize to test multiple inputs
@pytest.mark.parametrize("sample, expected_output", test_inputs)
def test_prediction(sample, expected_output):
    response = client.post(
            "language",
            json={"text":sample}
        )
    assert response.status_code == 200
    assert response.json() == expected_output
