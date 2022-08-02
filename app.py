import os

import flask
from flask import Flask, request, jsonify
from python_freeipa import ClientMeta
from dotenv import load_dotenv
import json

app = Flask(__name__)

# Load config from environment file.
load_dotenv('.env')

IPA_BASE_URL = os.getenv("IPA_BASE_URL")
IPA_USERNAME = os.getenv("IPA_USERNAME")
IPA_PASSWORD = os.getenv("IPA_PASSWORD")


@app.route('/')
def root_path():
    return "This is a Okta -> FreeIPA Broker"


@app.route('/add-member', methods=['POST'])
def add_member():
    request_data = json.loads(request.data)
    # Print to console for debugging <REMOVE>
    print("Received Request:")
    print(request_data)

    print("Sending user membership to FreeIPA")
    manage_ipa_group(request_data["group"], request_data["username"])

    status_code = flask.Response(status=200)
    return status_code


# Call FREEIPA API and authenticate w/ Basic Auth.
def manage_ipa_group(ipa_group, ipa_user):
    client = ClientMeta(IPA_BASE_URL, verify_ssl=False)
    client.login(IPA_USERNAME, IPA_PASSWORD)

    # Group Add Member takes in:
    # a_cn - Group Name
    # o_user - Username
    client.group_add_member(a_cn=ipa_group, o_user=ipa_user)


if __name__ == "__main__":
    app.run()
