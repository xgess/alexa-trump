class HelpResponder(object):
    TEXT = "Just ask Alexa to Ask Trump your question. " \
                "Think of it like a magic 8 ball but helpful."

    def response(self):
        return self._build_response()

    def _build_response(self):
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": self.TEXT
                },
                "shouldEndSession": True,
                "card": {
                    "type": "Simple",
                    "title": "Ask Trump a question!",
                    "content": "There's just so much he can help you with."
                }
            }
        }
