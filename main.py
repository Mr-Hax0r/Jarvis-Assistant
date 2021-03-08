from assistant.jarvis import Assistant
from  assistant import config


assistant = Assistant(model=config.MODEL_DIR,

                        command_mode_time = config.COMMAND_MODE_TIME,
                        
                        )

assistant.main()




