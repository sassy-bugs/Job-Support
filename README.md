# Student Support Bot
 A conversational AI , built using Rasa open source framework, with a purpose to solve educational queries. 
<img src="https://github.com/sassy-bugs/Job-Support/assets/97380939/0cdb1674-355a-4368-93ba-a9e2429120c7" alt = "botAvatar" width="300" height="300" />

Hers is a demo video ~ [Video link](https://drive.google.com/file/d/1gp3jthtlclZCjlK33guDg54gv8f20VAl/view?usp=sharing)
### Create a virtual environment and install dependencies

`python3 -m venv venv`

`source venv/bin/activate` (Linux/UNIX)

`venv\Scripts\activate` (Windows)

`pip install -r requirements.txt`

### Train model
`python3 -m rasa train`

### Run rasa in terminal
`python3 -m rasa shell`

### Train rasa with examples while running it on terminal
`python3 -m rasa interactive`

### Run RASA on web (needs to be updated, use shell/interactive in the meantime)

Clone this repository and run the following command in the terminal -  

`rasa run actions`  

`python3 -m rasa run --enable-api --cors="*"`  

Run the index.html file in Frontend-Widget.

## How to add data to dataset

### Add intent examples to `data/nlu.yml`
```yml
- intent: new_intent_name
  examples: |
    - some intent examples
    - make sure the examples help train the AI
    - and has all necessary keywords as well as variations of the keywords
    - minimum 5 examples are recommended
    - these examples all correspond to the same intent and will be mapped to a particular response so kindly do not club various examples together.
```
### Add intent name and response to `domain.yml`
```yml
intents:
  - existing_intent_name
  - new_intent_name
  .
  .
  .
responses:
  utter_new_intent_name:
  - text: "The response to new_intent_name"
  - image: "https://image.com/image.png" # optional
```

### Add rules to `data/rules.yml` to map the intent and response
```yml
- rule: Do action when asked about intent
  steps:
  - intent: new_intent_name
    action: utter_new_intent_name
  ``` 
