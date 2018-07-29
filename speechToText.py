import json
import uuid
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup


class RequestError(Exception):
    pass


class UnknownValueError(Exception):
    pass


def recognize_bing(audio, key, language="en-US"):
    session = requests.session()
    credential_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
    credential_request = session.post(credential_url, data=b"", headers={
        "Content-type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
        "Ocp-Apim-Subscription-Key": key,
    })
    access_token = BeautifulSoup(credential_request.content, 'html.parser')

    url = "https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?{}".format(urlencode({
        "language": language,
        "locale": language,
        "requestid": uuid.uuid4(),
    }))

    try:
        response = session.post(url, data=stream_audio_file(audio), headers={
            "Authorization": "Bearer {}".format(access_token),
            "Content-type": "audio/ogg; codec=\"audio/pcm\"; samplerate=16000",
            "Transfer-Encoding": "chunked",
        })
    except:
        raise RequestError()

    result = json.loads(str(BeautifulSoup(response.content, 'html.parser')))
    if "RecognitionStatus" not in result or result["RecognitionStatus"] != "Success" or "DisplayText" not in result:
        raise UnknownValueError()

    return result["DisplayText"]


def stream_audio_file(speech_file):
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read(1024)
            if not data:
                break
            yield data
