class Application:
    VALID_STATUSES = [
        "Applied",
        "Screening",
        "Interview",
        "Technical Interview",
        "Offer",
        "Rejected",
        "Withdrawn"
    ]

    def __init__(
        self,
        candidate_id,
        job_id,
        date_applied,
        status="Applied",
        notes=None,
        application_id=None
    ):
        self.application_id = application_id
        self.candidate_id = candidate_id
        self.job_id = job_id
        self.date_applied = date_applied
        self.notes = notes
        self.__status = None

        self.set_status(status)

    def get_status(self):
        return self.__status

    def set_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid application status: {status}")

        self.__status = status

    def __str__(self):
        return (
            f"Application {self.application_id} | "
            f"Candidate {self.candidate_id} | "
            f"Job {self.job_id} | "
            f"{self.__status}"
        )