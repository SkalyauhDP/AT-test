import json
import pytest

from model_module import PetModel


class TestClass:
    @pytest.mark.POST_test
    def test_successful_add_new_pet(self, create_api_client):
        with open('success_add_pet.json', 'r', encoding='utf-8') as df:
            pet_data = df.read()
        pet_unit = PetModel(**json.loads(pet_data))
        response = create_api_client.call_api_post(None, pet_unit.model_dump_json())
        assert response.status_code == 200

    @pytest.mark.POST_test
    def test_failed_add_new_pet(self, create_api_client):
        with open('failed_add_pet.json', 'r', encoding='utf-8') as df:
            pet_data = df.read()
        pet_unit = PetModel(**json.loads(pet_data))
        response = create_api_client.call_api_post(None, pet_unit.model_dump_json())
        assert response.status_code != 200

    @pytest.mark.POST_test
    def test_successful_update_pet_with_form(self, create_api_client):
        form = {"name": "new_name",
                "status": "sold"}
        response = create_api_client.call_api_post('5000', form)
        assert response.status_code == 200

    @pytest.mark.POST_test
    def test_failed_update_pet_with_form(self, create_api_client):
        form = {"name": "new_name",
                "status": "sold"}
        response = create_api_client.call_api_post('99223372036854752000', form)
        assert response.status_code != 200

    @pytest.mark.PUT_test
    def test_success_update_pet(self, create_api_client):
        with open('success_update_pet.json', 'r', encoding='utf-8') as df:
            pet_data = df.read()
        pet_unit = PetModel(**json.loads(pet_data))
        response = create_api_client.call_api_put(pet_unit.model_dump_json())
        assert response.status_code == 200

    @pytest.mark.PUT_test
    def test_failed_update_pet(self, create_api_client):
        with open('failed_update_pet.json', 'r', encoding='utf-8') as df:
            pet_data = df.read()
        pet_unit = PetModel(**json.loads(pet_data))
        response = create_api_client.call_api_put(pet_unit.model_dump_json())
        assert response.status_code != 200

    @pytest.mark.GET_test
    def test_successful_find_pet_by_id(self, create_api_client):
        response = create_api_client.call_api_get('5000')
        assert response.status_code == 200

    @pytest.mark.GET_test
    def test_failed_find_pet_by_id(self, create_api_client):
        response = create_api_client.call_api_get('5678')
        assert response.status_code == 404

    @pytest.mark.GET_test
    def test_successful_find_pet_by_status(self, create_api_client):
        response = create_api_client.call_api_get('findByStatus', 'pending')
        assert len(response.json()) != 0

    @pytest.mark.GET_test
    def test_failed_find_pet_by_status(self, create_api_client):
        response = create_api_client.call_api_get('findByStatus', 'ill')
        assert len(response.json()) == 0

    @pytest.mark.DELETE_test
    def test_successful_delete_pet(self, create_api_client):
        response = create_api_client.call_api_delete('5000')
        assert response.status_code == 200

    @pytest.mark.DELETE_test
    def test_failed_delete_pet(self, create_api_client):
        response = create_api_client.call_api_delete('5678')
        assert response.status_code == 404
