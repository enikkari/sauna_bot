# sauna_bot
Saunabot posts Futurice Helsinki offices friday sauna shifts and a reminder to turn on the sauna to slack; and serves a website showing the shifts for the current week.

The project uses python3.7 and other package requirements are in requirements.txt

To run the website locally run

```python app.py```

the website will run at http://127.0.0.1:8000/sauna


To run the page in a docker container run

```
docker build . -t sauna
docker run -p 8000:8000 -t sauna
```
the website will run at http://127.0.0.1:8000/sauna

To run the scheduler that posts messages to slack (bot_main.py)  you need to define a slack token in
```
environment_vars.sh
```