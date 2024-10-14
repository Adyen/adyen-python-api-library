from ..base import AdyenServiceBase


class TaxEDeliveryConsentApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TaxEDeliveryConsentApi, self).__init__(client=client)
        self.service = "legalEntityManagement"
        self.baseUrl = "https://kyc-test.adyen.com/lem/v3"

    def check_status_of_consent_for_electronic_delivery_of_tax_forms(self, id, idempotency_key=None, **kwargs):
        """
        Check the status of consent for electronic delivery of tax forms
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/checkTaxElectronicDeliveryConsent"
        method = "POST"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def set_consent_status_for_electronic_delivery_of_tax_forms(self, request, id, idempotency_key=None, **kwargs):
        """
        Set the consent status for electronic delivery of tax forms
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/setTaxElectronicDeliveryConsent"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

