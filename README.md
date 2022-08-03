
# Okta <-> FreeIPA Broker Example

This example was created to demonstrate how Okta's workflow engine can be utilized to interact with FreeIPA's JSON RPC API. This is a reference example and is NOT a secure implementation of such a broker. Ideally, Okta workflows would authenticate to the broker utilizing either OAuth or other secret mechanism. Additionally, basic authentication is used for the FreeIPA client, where Kerberos would be preferred. To start, create an .env file. It should contain the following variables:


IPA_BASE_URL = 'host.mydomain.com'

IPA_USERNAME = 'ipa service account'

IPA_PASSWORD = 'password'

**Created with <3 at Okta** by Pedro Santos (pedro.santos@okta.com)
