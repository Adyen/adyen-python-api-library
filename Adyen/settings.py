BASE_PAL_URL = "https://pal-{}.adyen.com/pal/servlet"
BASE_HPP_URL = "https://{}.adyen.com/hpp"
ENDPOINT_CHECKOUT_TEST = "https://checkout-test.adyen.com"
ENDPOINT_CHECKOUT_LIVE_SUFFIX = "https://{}-checkout-live" \
                                ".adyenpayments.com/checkout"
API_CHECKOUT_VERSION = "v40"
API_CHECKOUT_UTILITY_VERSION = "v1"
API_PAYOUT_VERSION = "v30"
API_RECURRING_VERSION = "v25"


@property
def API_VERSION():
    import warnings
    warnings.warn("this constant is deprecated use API_PAYOUT_VERSION",
                  DeprecationWarning)
    return "v30"
