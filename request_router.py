from music_player.getMusic import playMusic
from rasa.nlu.model import Interpreter

#model_directory = "entity_extraction_model"
#interpreter = Interpreter.load(model_directory)


def router(request):
    request = request.lower()
    #print(interpreter.parse(request))
    if ('music' in request):
        music = request.split(" ", 1)[1]
        playMusic(music)
    elif request.lower() == 'finish app':
        return False
    return True