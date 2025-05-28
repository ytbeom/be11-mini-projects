import os

from dotenv import load_dotenv


load_dotenv()

class Mentee:
    def __init__(self, name: str, location: str, desired_position: str, level: str, available_days: list[str], mbti: str):
        self.name = name
        self.location = location
        self.desired_position = desired_position
        self.level = level
        self.available_days = available_days
        self.mbti = mbti
        self.owner_id = os.environ["OWNER_ID"]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            location=data.get("location"),
            desired_position=data.get("desired_position"),
            level=data.get("level"),
            available_days=data.get("available_days", []),
            mbti=data.get("mbti")
        )

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "desired_position": self.desired_position,
            "level": self.level,
            "available_days": self.available_days,
            "mbti": self.mbti
        }


class Mentor:
    def __init__(self, name: str, company: str, position: str, location: str, skills: list[str], available_days: list[str], mbti: str):
        self.name = name
        self.company = company
        self.position = position
        self.location = location
        self.skills = skills
        self.available_days = available_days
        self.mbti = mbti

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            company=data.get("company"),
            position=data.get("position"),
            location=data.get("location"),
            skills=data.get("skills", []),
            available_days=data.get("available_days", []),
            mbti=data.get("mbti")
        )
