from skills.expense_skills import ExpenseSkill
from skills.notes_skills import NotesSkill  
from skills.weather_skill import WeatherSkill

class Dispatcher:
    def __init__(self, speaker):
        self.speaker = speaker
        self.skills = [
            ExpenseSkill(speaker),
            NotesSkill(speaker),
            WeatherSkill(speaker)
        ]

    def dispatch(self , command: str):

        
        for skill in self.skills:
            if skill.can_handle(command):
                skill.handle(command)
                return
        self.speaker.say("Sorry, I don't understand that command.")

    