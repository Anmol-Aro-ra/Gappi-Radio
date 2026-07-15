from core.base_skill import BaseSkill
from datetime import datetime

class NotesSkill(BaseSkill):

    def __init__(self , speaker):
        self.filepath = "data/notes.txt"
        self.speaker = speaker

    def get_keywords(self):
        return ["note", "remember", "notes", "याद"]
    
    def handle(self , command:str):
        if "save" in command or "remember" in command:
            self.save_note(command)
        elif "show" in command or "view" in command:
            self.view_notes()
        elif "clear" in command:
            self.clear_notes()
        

    def save_note(self , command):
        trigger_words = ["save notes","note that","remember","note"]
        note = command
        for trigger in trigger_words:
            if trigger in command:
                note = command.split(trigger , 1)[-1].strip()
                break
        if not note:
            self.speaker.say("What should i remember?")
            return
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(self.filepath,'a') as f:
            f.write(f"[{date}] {note}\n")
        self.speaker.say(f"Got it, I will remember: {note}")

    def view_notes(self):
        try:
            with open(self.filepath, 'r') as f:
                lines = f.readlines()
                if not lines:
                    self.speaker.say("No notes found")
                    return
                for line in lines:
                    print(line.strip())
                self.speaker.say(f"You have {len(lines)} notes")
        
        except FileNotFoundError:
            self.speaker.say("No notes found")

    def clear_notes(self):
        with open(self.filepath, 'w') as f:
            pass
        self.speaker.say("All notes cleared") 
            
        


