class Candidate:
    def __init__(self, name, email, phone, location, skills, experience_years, candidate_id=None):
        self.candidate_id = candidate_id
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.skills = skills
        self.__experience_years = experience_years
    def get_experience_years(self):
        return self.__experience_years
    def set_experience_years(self, experience_years):
        if experience_years >= 0:
            self.__experience_years = experience_years
        else:
            raise ValueError("Experience years cannot be negative")

    def __str__(self):
        return f"{self.name} | {self.email} | {self.location} | {self.__experience_years} years experience"