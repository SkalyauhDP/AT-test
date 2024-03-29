import pytest

from module_request import ApiRequest


@pytest.fixture
def my_api_request():
    result = ApiRequest('POST', 'some info')
    return result


class TestClass:
    @pytest.mark.usefixtures("my_api_request")
    def test_check_request_type(self, my_api_request):
        assert my_api_request.req_type == 'POST', 'Type of request is not POST'

    @pytest.mark.usefixtures("my_api_request")
    def test_check_payload(self, my_api_request):
        assert my_api_request.payload == 'some info', 'incorrect payload'

    @pytest.mark.usefixtures("my_api_request")
    def test_check_change_payload(self, my_api_request):
        my_api_request.change_payload('new payload')
        assert my_api_request.payload == 'new payload', 'wrong change'


if __name__ == '__main__':
    test_class = TestClass()
    test_class.test_check_request_type()
    test_class.test_check_payload()
    test_class.test_check_change_payload()
