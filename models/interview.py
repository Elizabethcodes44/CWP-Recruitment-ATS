class Interview:
    VALID_TYPES = [
        "Phone",
        "Online",
        "In-person",
        "Technical"
    ]

    def __init__(
        self,
        application_id,
        interview_date,
        interview_type,
        interviewer,
        notes=None,
        interview_id=None
    ):
        self.interview_id = interview_id
        self.application_id = application_id
        self.interview_date = interview_date
        self.interviewer = interviewer
        self.notes = notes
        self.__interview_type = None

        self.set_interview_type(interview_type)

    def get_interview_type(self):
        return self.__interview_type

    def set_interview_type(self, interview_type):
        if interview_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid interview type: {interview_type}")

        self.__interview_type = interview_type

    def __str__(self):
        return (
            f"Interview {self.interview_id} | "
            f"Application {self.application_id} | "
            f"{self.interview_date} | "
            f"{self.__interview_type} | "
            f"Interviewer: {self.interviewer}"
        )