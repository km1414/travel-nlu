# travel-nlu

### Intro
Tool, trained for entity recognition (_source, destination_) in travel domain.

**Used tools:**
* https://rasa.com/docs/rasa/
* https://pypi.org/project/chatette/
* https://spacy.io/

**Used datasets:**
* https://www.kaggle.com/open-flights/airports-train-stations-and-ferry-terminals/data
* https://github.com/first20hours/google-10000-english

**Input example:**
```
Hi I’m going from London to Tokyo tomorrow morning very early
```
**Output example:**
```
{
  "intent": {
    "name": null,
    "confidence": 0.0
  },
  "entities": [
    {
      "start": 18,
      "end": 24,
      "value": "London",
      "entity": "source",
      "confidence": 0.9842661731474959,
      "extractor": "CRFEntityExtractor",
      "processors": [
        "EntitySynonymMapper"
      ]
    },
    {
      "start": 28,
      "end": 33,
      "value": "Tokyo",
      "entity": "destination",
      "confidence": 0.9600808000644201,
      "extractor": "CRFEntityExtractor",
      "processors": [
        "EntitySynonymMapper"
      ]
    }
  ],
  "text": "Hi I’m going from London to Tokyo tomorrow morning very early"
}
```

### Run locally:
```
### Setup:
git clone https://github.com/km1414/travel-nlu.git
cd travel-nlu
conda create -n travel-nlu python=3.7
conda activate travel-nlu
pip install -r requirements.txt
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

### Run shell:
rasa shell nlu

### Run API:
rasa run --enable-api

### Test API:
curl localhost:5005/model/parse -d '{"text":"i want to go from berlin to london"}'

### Retrain (see instruction in data_generator.py before training):
python data_generator.py
rasa train nlu
```


### Run in Docker:
```
### Build:
git clone https://github.com/km1414/travel-nlu.git
cd travel-nlu
docker build . -t travel-nlu:tag1

### Run shell:
docker run --rm -it travel-nlu:tag1

### Pull from Docker Hub and run shell (no building)
docker run --rm -it km1414/travel-nlu
```


### Query examples:
```
I’m going from Tokyo to London tomorrow
I’m going from London to Tokyo tomorrow morning very early
Tokyo to London
Tokyo London
from London to Rio de Janeiro on Monday
i need tickets from from london to vilnius
I want to go from Dublin to Riga
from new york to los angeles
Tallin to Rome
Helsinki Amsterdam
flight to Oslo from Ljubljana
i want to go from table to bed
from January to March
from 8am
Winter to Summer
i dong go anywhere, thank you
I want to go from Berlin to London, after that I go to Vilnius, and finally go to Tallin
```

### Results
Training and testing sets are randomly generated using exactly same rules and same possible locations.
```
{
  "destination": {
    "precision": 0.9849583182312432,
    "recall": 0.989080982711556,
    "f1-score": 0.9870153455007719,
    "support": 5495
  },
  "source": {
    "precision": 0.9717965800577393,
    "recall": 0.9981751824817519,
    "f1-score": 0.9848092719702937,
    "support": 4384
  }
}
```