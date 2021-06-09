# Este arquivo contém custom actions que utilizão código python
# para executar ações no diálogo.
#
# Veja o guia na documentação do RASA em:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests

from random import randint

class ActionTeste(Action):
    def name(self) -> Text:
        return "action_teste"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


class ActionTelefone(Action):
    def name(self) -> Text:
        return "action_telefone"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        telefone = tracker.get_slot('telefone')

        try:
            dispatcher.utter_message("O seu telefone é {}?".format(telefone))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet("telefone", telefone)]


class ActionAdvices(Action):
    def name(self) -> Text:
        return "action_pedir_conselho"

    def run(self, dispatcher, tracker, domain):

        nome = tracker.get_slot('nome')

        req = requests.request('GET', "https://api.adviceslip.com/advice")
        conselho = req.json()["slip"]["advice"]
    
        try:
            if nome:
                dispatcher.utter_message("{} olha que conselho legal: {}".format(nome, conselho))
            else:
                dispatcher.utter_message("Olha que conselho legal: {}".format(conselho))
        except ValueError:
            dispatcher.utter_message(ValueError)

class ActionSortingHat(Action):
    def name(self) -> Text:
        return "action_sorting_hat"

    def run(self, dispatcher, tracker, domain):

        nome = tracker.get_slot('nome')

        req = requests.get("https://www.potterapi.com/v1/sortingHat")
        casa = req.json()

        try:
            if nome:
                dispatcher.utter_message("{} Sua casa de Hogwarts é: {}".format(nome, casa))
            else:
                dispatcher.utter_message("Sua casa de Hogwarts: {}".format(casa))
        except ValueError:
            dispatcher.utter_message(ValueError)

class ActionCatFacts(Action):
    def name(self) -> Text:
        return "action_cat_facts"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("fatos_sobre_gatos") == None:
            req = requests.request('GET', "https://cat-fact.herokuapp.com/facts")
            lista = []
            for n in range(20):
                lista.append(req.json()["all"][n]["text"])
         
            fato = lista[randint(0, 19)]
         
            try:
                 dispatcher.utter_message("{}".format(fato))
            except ValueError:
                 dispatcher.utter_message(ValueError)
            return [SlotSet("fatos_sobre_gatos", lista)]
        else:
            fato = tracker.get_slot("fatos_sobre_gatos")[randint(0, 19)]
            try:
                dispatcher.utter_message("{}".format(fato))
            except ValueError:
                dispatcher.utter_message(ValueError)
            return []

        