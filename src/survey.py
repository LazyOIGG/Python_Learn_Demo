class AnonymousSurvey:
    """收集匿名调查的问卷"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_responses(self):
        print("Survey result:")
        for response in self.responses:
            print(f"\t{response}")
