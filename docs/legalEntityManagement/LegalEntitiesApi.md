# legalEntityManagement

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_legal_entity**](LegalEntitiesApi.md#get_legal_entity) | **GET** /legalEntities/{id} | Get a legal entity
[**get_all_business_lines_under_legal_entity**](LegalEntitiesApi.md#get_all_business_lines_under_legal_entity) | **GET** /legalEntities/{id}/businessLines | Get all business lines under a legal entity
[**update_legal_entity**](LegalEntitiesApi.md#update_legal_entity) | **PATCH** /legalEntities/{id} | Update a legal entity
[**create_legal_entity**](LegalEntitiesApi.md#create_legal_entity) | **POST** /legalEntities | Create a legal entity




# get_legal_entity
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.legal_entities_api.get_legal_entity()

```




# get_all_business_lines_under_legal_entity
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
response = apiClient.legal_entities_api.get_all_business_lines_under_legal_entity()

```




# update_legal_entity
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;documentDetails&quot; : [ {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  }, {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  } ],
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;soleProprietorship&quot; : {
    &quot;dateOfIncorporation&quot; : &quot;dateOfIncorporation&quot;,
    &quot;registeredAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;doingBusinessAs&quot; : &quot;doingBusinessAs&quot;,
    &quot;registrationNumber&quot; : &quot;registrationNumber&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;principalPlaceOfBusiness&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;vatAbsenceReason&quot; : &quot;industryExemption&quot;,
    &quot;countryOfGoverningLaw&quot; : &quot;countryOfGoverningLaw&quot;,
    &quot;vatNumber&quot; : &quot;vatNumber&quot;
  },
  &quot;capabilities&quot; : {
    &quot;key&quot; : {
      &quot;requested&quot; : true,
      &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
      &quot;allowed&quot; : true,
      &quot;allowedSettings&quot; : {
        &quot;authorizedCardUsers&quot; : true,
        &quot;interval&quot; : &quot;daily&quot;,
        &quot;fundingSource&quot; : [ &quot;credit&quot;, &quot;credit&quot; ],
        &quot;maxAmount&quot; : {
          &quot;currency&quot; : &quot;currency&quot;,
          &quot;value&quot; : 0
        },
        &quot;amountPerIndustry&quot; : {
          &quot;key&quot; : {
            &quot;currency&quot; : &quot;currency&quot;,
            &quot;value&quot; : 0
          }
        }
      },
      &quot;allowedLevel&quot; : &quot;high&quot;,
      &quot;requestedLevel&quot; : &quot;high&quot;,
      &quot;requestedSettings&quot; : {
        &quot;authorizedCardUsers&quot; : true,
        &quot;interval&quot; : &quot;daily&quot;,
        &quot;fundingSource&quot; : [ &quot;credit&quot;, &quot;credit&quot; ],
        &quot;maxAmount&quot; : {
          &quot;currency&quot; : &quot;currency&quot;,
          &quot;value&quot; : 0
        },
        &quot;amountPerIndustry&quot; : {
          &quot;key&quot; : {
            &quot;currency&quot; : &quot;currency&quot;,
            &quot;value&quot; : 0
          }
        }
      },
      &quot;transferInstruments&quot; : [ {
        &quot;requested&quot; : true,
        &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
        &quot;allowed&quot; : true,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;requested&quot; : true,
        &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
        &quot;allowed&quot; : true,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;problems&quot; : [ {
        &quot;verificationErrors&quot; : [ {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        }, {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        } ],
        &quot;entity&quot; : {
          &quot;owner&quot; : {
            &quot;id&quot; : &quot;id&quot;,
            &quot;type&quot; : &quot;BankAccount&quot;
          },
          &quot;id&quot; : &quot;id&quot;,
          &quot;type&quot; : &quot;BankAccount&quot;
        }
      }, {
        &quot;verificationErrors&quot; : [ {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        }, {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        } ],
        &quot;entity&quot; : {
          &quot;owner&quot; : {
            &quot;id&quot; : &quot;id&quot;,
            &quot;type&quot; : &quot;BankAccount&quot;
          },
          &quot;id&quot; : &quot;id&quot;,
          &quot;type&quot; : &quot;BankAccount&quot;
        }
      } ]
    }
  },
  &quot;individual&quot; : {
    &quot;identificationData&quot; : {
      &quot;expiryDate&quot; : &quot;expiryDate&quot;,
      &quot;issuerCountry&quot; : &quot;issuerCountry&quot;,
      &quot;issuerState&quot; : &quot;issuerState&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;nationalIdExempt&quot; : true,
      &quot;type&quot; : &quot;bankStatement&quot;,
      &quot;cardNumber&quot; : &quot;cardNumber&quot;
    },
    &quot;nationality&quot; : &quot;nationality&quot;,
    &quot;phone&quot; : {
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    },
    &quot;residentialAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;name&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;,
      &quot;infix&quot; : &quot;infix&quot;
    },
    &quot;birthData&quot; : {
      &quot;dateOfBirth&quot; : &quot;dateOfBirth&quot;
    },
    &quot;webData&quot; : {
      &quot;webAddressId&quot; : &quot;webAddressId&quot;,
      &quot;webAddress&quot; : &quot;webAddress&quot;
    },
    &quot;taxInformation&quot; : [ {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    }, {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    } ],
    &quot;email&quot; : &quot;email&quot;
  },
  &quot;documents&quot; : [ {
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;organization&quot; : {
    &quot;taxReportingClassification&quot; : {
      &quot;financialInstitutionNumber&quot; : &quot;financialInstitutionNumber&quot;,
      &quot;mainSourceOfIncome&quot; : &quot;businessOperation&quot;,
      &quot;businessType&quot; : &quot;other&quot;,
      &quot;type&quot; : &quot;nonFinancialNonReportable&quot;
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;taxInformation&quot; : [ {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    }, {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    } ],
    &quot;type&quot; : &quot;associationIncorporated&quot;,
    &quot;stockData&quot; : {
      &quot;stockNumber&quot; : &quot;stockNumber&quot;,
      &quot;tickerSymbol&quot; : &quot;tickerSymbol&quot;,
      &quot;marketIdentifier&quot; : &quot;marketIdentifier&quot;
    },
    &quot;vatAbsenceReason&quot; : &quot;industryExemption&quot;,
    &quot;legalName&quot; : &quot;legalName&quot;,
    &quot;dateOfIncorporation&quot; : &quot;dateOfIncorporation&quot;,
    &quot;registeredAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;doingBusinessAs&quot; : &quot;doingBusinessAs&quot;,
    &quot;phone&quot; : {
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    },
    &quot;registrationNumber&quot; : &quot;registrationNumber&quot;,
    &quot;webData&quot; : {
      &quot;webAddressId&quot; : &quot;webAddressId&quot;,
      &quot;webAddress&quot; : &quot;webAddress&quot;
    },
    &quot;principalPlaceOfBusiness&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;email&quot; : &quot;email&quot;,
    &quot;vatNumber&quot; : &quot;vatNumber&quot;
  },
  &quot;entityAssociations&quot; : [ {
    &quot;associatorId&quot; : &quot;associatorId&quot;,
    &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
    &quot;entityType&quot; : &quot;entityType&quot;,
    &quot;jobTitle&quot; : &quot;jobTitle&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;type&quot; : &quot;pciSignatory&quot;
  }, {
    &quot;associatorId&quot; : &quot;associatorId&quot;,
    &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
    &quot;entityType&quot; : &quot;entityType&quot;,
    &quot;jobTitle&quot; : &quot;jobTitle&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;type&quot; : &quot;pciSignatory&quot;
  } ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;transferInstruments&quot; : [ {
    &quot;accountIdentifier&quot; : &quot;accountIdentifier&quot;,
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;accountIdentifier&quot; : &quot;accountIdentifier&quot;,
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;type&quot; : &quot;individual&quot;
}

response = apiClient.legal_entities_api.update_legal_entity(request)

```




# create_legal_entity
### Example

```python
from Adyen import legalEntityManagement

apiClient = legalEntityManagement
apiClient.client.xapikey = "YourApiKey"
apiClient.client.platform = "test"
request = {
  &quot;documentDetails&quot; : [ {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  }, {
    &quot;fileName&quot; : &quot;fileName&quot;,
    &quot;modificationDate&quot; : &quot;2000-01-23T04:56:07.000+00:00&quot;,
    &quot;active&quot; : true,
    &quot;description&quot; : &quot;description&quot;,
    &quot;id&quot; : &quot;id&quot;,
    &quot;type&quot; : &quot;type&quot;
  } ],
  &quot;reference&quot; : &quot;reference&quot;,
  &quot;soleProprietorship&quot; : {
    &quot;dateOfIncorporation&quot; : &quot;dateOfIncorporation&quot;,
    &quot;registeredAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;doingBusinessAs&quot; : &quot;doingBusinessAs&quot;,
    &quot;registrationNumber&quot; : &quot;registrationNumber&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;principalPlaceOfBusiness&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;vatAbsenceReason&quot; : &quot;industryExemption&quot;,
    &quot;countryOfGoverningLaw&quot; : &quot;countryOfGoverningLaw&quot;,
    &quot;vatNumber&quot; : &quot;vatNumber&quot;
  },
  &quot;capabilities&quot; : {
    &quot;key&quot; : {
      &quot;requested&quot; : true,
      &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
      &quot;allowed&quot; : true,
      &quot;allowedSettings&quot; : {
        &quot;authorizedCardUsers&quot; : true,
        &quot;interval&quot; : &quot;daily&quot;,
        &quot;fundingSource&quot; : [ &quot;credit&quot;, &quot;credit&quot; ],
        &quot;maxAmount&quot; : {
          &quot;currency&quot; : &quot;currency&quot;,
          &quot;value&quot; : 0
        },
        &quot;amountPerIndustry&quot; : {
          &quot;key&quot; : {
            &quot;currency&quot; : &quot;currency&quot;,
            &quot;value&quot; : 0
          }
        }
      },
      &quot;allowedLevel&quot; : &quot;high&quot;,
      &quot;requestedLevel&quot; : &quot;high&quot;,
      &quot;requestedSettings&quot; : {
        &quot;authorizedCardUsers&quot; : true,
        &quot;interval&quot; : &quot;daily&quot;,
        &quot;fundingSource&quot; : [ &quot;credit&quot;, &quot;credit&quot; ],
        &quot;maxAmount&quot; : {
          &quot;currency&quot; : &quot;currency&quot;,
          &quot;value&quot; : 0
        },
        &quot;amountPerIndustry&quot; : {
          &quot;key&quot; : {
            &quot;currency&quot; : &quot;currency&quot;,
            &quot;value&quot; : 0
          }
        }
      },
      &quot;transferInstruments&quot; : [ {
        &quot;requested&quot; : true,
        &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
        &quot;allowed&quot; : true,
        &quot;id&quot; : &quot;id&quot;
      }, {
        &quot;requested&quot; : true,
        &quot;verificationStatus&quot; : &quot;verificationStatus&quot;,
        &quot;allowed&quot; : true,
        &quot;id&quot; : &quot;id&quot;
      } ],
      &quot;problems&quot; : [ {
        &quot;verificationErrors&quot; : [ {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        }, {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        } ],
        &quot;entity&quot; : {
          &quot;owner&quot; : {
            &quot;id&quot; : &quot;id&quot;,
            &quot;type&quot; : &quot;BankAccount&quot;
          },
          &quot;id&quot; : &quot;id&quot;,
          &quot;type&quot; : &quot;BankAccount&quot;
        }
      }, {
        &quot;verificationErrors&quot; : [ {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        }, {
          &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
          &quot;code&quot; : &quot;code&quot;,
          &quot;message&quot; : &quot;message&quot;,
          &quot;type&quot; : &quot;dataMissing&quot;,
          &quot;remediatingActions&quot; : [ {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          }, {
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;
          } ],
          &quot;subErrors&quot; : [ {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          }, {
            &quot;capabilities&quot; : [ &quot;acceptExternalFunding&quot;, &quot;acceptExternalFunding&quot; ],
            &quot;code&quot; : &quot;code&quot;,
            &quot;message&quot; : &quot;message&quot;,
            &quot;type&quot; : &quot;dataMissing&quot;,
            &quot;remediatingActions&quot; : [ {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            }, {
              &quot;code&quot; : &quot;code&quot;,
              &quot;message&quot; : &quot;message&quot;
            } ]
          } ]
        } ],
        &quot;entity&quot; : {
          &quot;owner&quot; : {
            &quot;id&quot; : &quot;id&quot;,
            &quot;type&quot; : &quot;BankAccount&quot;
          },
          &quot;id&quot; : &quot;id&quot;,
          &quot;type&quot; : &quot;BankAccount&quot;
        }
      } ]
    }
  },
  &quot;individual&quot; : {
    &quot;identificationData&quot; : {
      &quot;expiryDate&quot; : &quot;expiryDate&quot;,
      &quot;issuerCountry&quot; : &quot;issuerCountry&quot;,
      &quot;issuerState&quot; : &quot;issuerState&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;nationalIdExempt&quot; : true,
      &quot;type&quot; : &quot;bankStatement&quot;,
      &quot;cardNumber&quot; : &quot;cardNumber&quot;
    },
    &quot;nationality&quot; : &quot;nationality&quot;,
    &quot;phone&quot; : {
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    },
    &quot;residentialAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;name&quot; : {
      &quot;firstName&quot; : &quot;firstName&quot;,
      &quot;lastName&quot; : &quot;lastName&quot;,
      &quot;infix&quot; : &quot;infix&quot;
    },
    &quot;birthData&quot; : {
      &quot;dateOfBirth&quot; : &quot;dateOfBirth&quot;
    },
    &quot;webData&quot; : {
      &quot;webAddressId&quot; : &quot;webAddressId&quot;,
      &quot;webAddress&quot; : &quot;webAddress&quot;
    },
    &quot;taxInformation&quot; : [ {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    }, {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    } ],
    &quot;email&quot; : &quot;email&quot;
  },
  &quot;documents&quot; : [ {
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;organization&quot; : {
    &quot;taxReportingClassification&quot; : {
      &quot;financialInstitutionNumber&quot; : &quot;financialInstitutionNumber&quot;,
      &quot;mainSourceOfIncome&quot; : &quot;businessOperation&quot;,
      &quot;businessType&quot; : &quot;other&quot;,
      &quot;type&quot; : &quot;nonFinancialNonReportable&quot;
    },
    &quot;description&quot; : &quot;description&quot;,
    &quot;taxInformation&quot; : [ {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    }, {
      &quot;country&quot; : &quot;country&quot;,
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    } ],
    &quot;type&quot; : &quot;associationIncorporated&quot;,
    &quot;stockData&quot; : {
      &quot;stockNumber&quot; : &quot;stockNumber&quot;,
      &quot;tickerSymbol&quot; : &quot;tickerSymbol&quot;,
      &quot;marketIdentifier&quot; : &quot;marketIdentifier&quot;
    },
    &quot;vatAbsenceReason&quot; : &quot;industryExemption&quot;,
    &quot;legalName&quot; : &quot;legalName&quot;,
    &quot;dateOfIncorporation&quot; : &quot;dateOfIncorporation&quot;,
    &quot;registeredAddress&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;doingBusinessAs&quot; : &quot;doingBusinessAs&quot;,
    &quot;phone&quot; : {
      &quot;number&quot; : &quot;number&quot;,
      &quot;type&quot; : &quot;type&quot;
    },
    &quot;registrationNumber&quot; : &quot;registrationNumber&quot;,
    &quot;webData&quot; : {
      &quot;webAddressId&quot; : &quot;webAddressId&quot;,
      &quot;webAddress&quot; : &quot;webAddress&quot;
    },
    &quot;principalPlaceOfBusiness&quot; : {
      &quot;country&quot; : &quot;country&quot;,
      &quot;stateOrProvince&quot; : &quot;stateOrProvince&quot;,
      &quot;city&quot; : &quot;city&quot;,
      &quot;street&quot; : &quot;street&quot;,
      &quot;postalCode&quot; : &quot;postalCode&quot;,
      &quot;street2&quot; : &quot;street2&quot;
    },
    &quot;email&quot; : &quot;email&quot;,
    &quot;vatNumber&quot; : &quot;vatNumber&quot;
  },
  &quot;entityAssociations&quot; : [ {
    &quot;associatorId&quot; : &quot;associatorId&quot;,
    &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
    &quot;entityType&quot; : &quot;entityType&quot;,
    &quot;jobTitle&quot; : &quot;jobTitle&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;type&quot; : &quot;pciSignatory&quot;
  }, {
    &quot;associatorId&quot; : &quot;associatorId&quot;,
    &quot;legalEntityId&quot; : &quot;legalEntityId&quot;,
    &quot;entityType&quot; : &quot;entityType&quot;,
    &quot;jobTitle&quot; : &quot;jobTitle&quot;,
    &quot;name&quot; : &quot;name&quot;,
    &quot;type&quot; : &quot;pciSignatory&quot;
  } ],
  &quot;id&quot; : &quot;id&quot;,
  &quot;transferInstruments&quot; : [ {
    &quot;accountIdentifier&quot; : &quot;accountIdentifier&quot;,
    &quot;id&quot; : &quot;id&quot;
  }, {
    &quot;accountIdentifier&quot; : &quot;accountIdentifier&quot;,
    &quot;id&quot; : &quot;id&quot;
  } ],
  &quot;type&quot; : &quot;individual&quot;
}

response = apiClient.legal_entities_api.create_legal_entity(request)

```


