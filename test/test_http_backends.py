import pytest
import Adyen
from Adyen import settings

@pytest.mark.parametrize("backend", ["requests", "pycurl", "urllib"])
def test_backend_communication(mock_server, backend):
    """Verifies that each HTTP backend correctly places bytes on the wire."""
    ady = Adyen.Adyen()
    ady.client.xapikey = "TEST_XAPI_KEY"
    ady.client.platform = "test"
    ady.client.http_force = backend
    
    # We use a custom endpoint to point to our local mock server
    # Since we are testing the httpclient directly, we can call it from the client
    if not ady.client.http_init:
        ady.client._init_http_client()
    
    request_data = {"test": "data"}
    headers = {"Custom-Header": "Value"}
    
    # We call the http_client.request directly to avoid URL determination logic
    # which might prepend adyen domains.
    result, raw_request, status_code, response_headers = ady.client.http_client.request(
        "POST",
        f"{mock_server}/test-endpoint",
        json=request_data,
        headers=headers,
        xapikey="TEST_XAPI_KEY"
    )
    
    import json
    response_data = json.loads(result)
    
    assert status_code == 200
    assert response_data["method"] == "POST"
    assert response_data["path"] == "/test-endpoint"
    assert response_data["received_body"] == request_data
    
    # Verify common headers
    received_headers = {k.lower(): v for k, v in response_data["received_headers"].items()}
    assert received_headers["x-api-key"] == "TEST_XAPI_KEY"
    assert "adyen-python-api-library" in received_headers["user-agent"]
    assert received_headers["custom-header"] == "Value"

def test_backend_with_real_mock_file(mock_server, mock_server_client):
    """Verifies that backends can handle real mock responses served from files."""
    mock_file = "test/mocks/checkout/paymentmethods-success.json"
    ady, headers = mock_server_client(mock_file=mock_file)
    
    # We manually set the base URL to our mock server for this service
    ady.checkout.payments_api.baseUrl = f"{mock_server}/checkout/v71"
    
    result = ady.checkout.payments_api.payment_methods(
        {"merchantAccount": "Test"}, 
        header_parameters=headers
    )
    
    # Verify the data came from the JSON file
    assert result.message['paymentMethods'][0]['name'] == "AliPay"
    assert result.status_code == 200

    """Verifies that timeouts are handled (using a non-responsive endpoint if possible)."""
    # This is a bit harder with http.server as it is single-threaded and handles one request at a time.
    # But we can verify that the timeout parameter is at least passed correctly.
    ady = Adyen.Adyen()
    ady.client.http_timeout = 0.001
    ady.client.http_force = "requests"
    ady.client._init_http_client()
    
    # We expect a timeout error from the backend
    with pytest.raises(Exception):
        ady.client.http_client.request(
            "GET",
            f"{mock_server}/slow-endpoint",
            xapikey="TEST_XAPI_KEY"
        )
