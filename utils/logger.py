import logging


logging.basicConfig(
    filename="recruitment.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger("recruitment_ats")