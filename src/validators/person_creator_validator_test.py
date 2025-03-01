from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self,body) -> None:
        self.body = body
        

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "Fulano",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 3
    })

    person_creator_validator(request)
