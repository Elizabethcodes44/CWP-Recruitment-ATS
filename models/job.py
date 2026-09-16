class Job:
    def __init__(
        self,
        title,
        department,
        location,
        salary_min,
        salary_max,
        status,
        created_at,
        job_id=None
    ):
        self.job_id = job_id
        self.title = title
        self.department = department
        self.location = location
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.status = status
        self.created_at = created_at

    def validate_salary(self):
        if self.salary_min < 0 or self.salary_max < 0:
            raise ValueError("Salary cannot be negative")

        if self.salary_min > self.salary_max:
            raise ValueError("Minimum salary cannot be greater than maximum salary")

        return True

    def __str__(self):
        return f"{self.title} | {self.department} | {self.location} | {self.status}"
    