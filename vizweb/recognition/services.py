import os
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(os.getenv("IBM_VR_API_KEY"))
visual_recognition = VisualRecognitionV3(
    version="2018-03-19", authenticator=authenticator
)
visual_recognition.set_service_url(os.getenv("IBM_VR_URL"))

# usage:
# recognition_result = visual_recognition.classify(url={url}).get_result()
# json.dumps(recognition_result)