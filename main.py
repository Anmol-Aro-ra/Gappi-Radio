from core.speaker import Speaker
from core.dispatcher import Dispatcher      
from core.listen import Listener

def main():
    speaker = Speaker()
    listener = Listener()
    dispatcher = Dispatcher(speaker)

    speaker.say("Hello! I am your personal assistant. How can I help you today?")

    while True:
        command = listener.listen()

        if not command:
            speaker.say("I didn't catch that. Could you please repeat?")
            continue
        if "exit" in command or "bye"in command:
            speaker.say("Goodbye!")
            break

        dispatcher.dispatch(command)

if __name__ == "__main__":
    main()
