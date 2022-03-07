from music_player.getMusic import playMusic
from rasa.nlu.model import Interpreter

model_directory = "entity_extraction_model"
interpreter = Interpreter.load(model_directory)

'''

=> interpreter.parse(text) output EXAMPLE:

{
    'text': 'music starships', 
    'intent': {
        'id': -612741962261129928, 
        'name': 'AddToPlaylist', 
        'confidence': 1.0
    }, 
    'entities': [{'entity': 'playlist', 'start': 0, 'end': 5, 'confidence_entity': 0.48056355118751526, 'value': 'music', 'extractor': 'DIETClassifier'}, 
                 {'entity': 'entity_name', 'start': 6, 'end': 15, 'confidence_entity': 0.8257302045822144, 'value': 'starships', 'extractor': 'DIETClassifier'}], 

    'intent_ranking': [{'id': -612741962261129928, 'name': 'AddToPlaylist', 'confidence': 1.0}, 
                       {'id': -7846782904660757827, 'name': 'AddToPlaylist2', 'confidence': 3.508607293589705e-10}],

    'response_selector': {'all_retrieval_intents': [], 'default': {'response': {'id': None, 'responses': None, 'response_templates': None, 'confidence': 0.0, 'intent_response_key': None, 'utter_action': 'utter_None', 'template_name': 'utter_None'}, 'ranking': []}}
}

'''

def router(request):
    request = request.lower()
    print(interpreter.parse(request))
    if ('music' in request):
        music = request.split(" ", 1)[1]
        playMusic(music)
    elif request.lower() == 'finish app':
        return False
    return True