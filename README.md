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

### Results
```
{
  "source": {
    "precision": 0.932624693376942,
    "recall": 0.9700629358734478,
    "f1-score": 0.9509754877438719,
    "support": 5879
  },
  "destination": {
    "precision": 0.9318258521768478,
    "recall": 0.9583477959041999,
    "f1-score": 0.9449007529089665,
    "support": 5762
  },
  "micro avg": {
    "precision": 0.9322315422307117,
    "recall": 0.9642642384674857,
    "f1-score": 0.9479773667764547,
    "support": 11641
  },
  "macro avg": {
    "precision": 0.9322252727768949,
    "recall": 0.9642053658888239,
    "f1-score": 0.9479381203264192,
    "support": 11641
  },
  "weighted avg": {
    "precision": 0.9322292872267021,
    "recall": 0.9642642384674857,
    "f1-score": 0.9479686479432771,
    "support": 11641
  }
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
docker build . -t travel-nlu:tag1

### Run shell:
docker run --rm -it travel-nlu:tag1

### Pull from Docker Hub and run shell (nu building)
docker run --rm -it km1414/travel-nlu
```


### Query examples:
```
I’m going from Tokyo to London tomorrow
I’m going to London from Tokyo tomorrow morning very early
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