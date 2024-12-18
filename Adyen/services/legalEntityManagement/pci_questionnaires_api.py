from ..base import AdyenServiceBase


class PCIQuestionnairesApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PCIQuestionnairesApi, self).__init__(client=client)
        self.service = "legalEntityManagement"
        self.baseUrl = "https://kyc-test.adyen.com/lem/v3"

    def calculate_pci_status_of_legal_entity(self, request, id, idempotency_key=None, **kwargs):
        """
        Calculate PCI status of a legal entity
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/pciQuestionnaires/signingRequired"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def generate_pci_questionnaire(self, request, id, idempotency_key=None, **kwargs):
        """
        Generate PCI questionnaire
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/pciQuestionnaires/generatePciTemplates"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_pci_questionnaire(self, id, pciid, idempotency_key=None, **kwargs):
        """
        Get PCI questionnaire
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/pciQuestionnaires/{pciid}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_pci_questionnaire_details(self, id, idempotency_key=None, **kwargs):
        """
        Get PCI questionnaire details
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/pciQuestionnaires"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def sign_pci_questionnaire(self, request, id, idempotency_key=None, **kwargs):
        """
        Sign PCI questionnaire
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/pciQuestionnaires/signPciTemplates"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

