import json


class RollingGame:

    def __init__(self):
        with open('rules.json', 'r', encoding='utf-8') as r:
            self.rules = json.load(r)
        with open('attributes.json', 'r', encoding='utf-8') as attributes_file:
            self.attributes = json.load(attributes_file)
        self.first_question = self.rules[0]['if'][0]['attribute']
        self.rules_list = [self.first_question]
        _, self.first_answers = self.find_rule(self.rules, self.attributes, self.rules_list)

    def get_rules(self):
        myfile = open('rules.json', 'r', encoding='utf-8')
        with  open('attributes.json', 'r', encoding='utf-8') as attributes_file:
            attributes_file = json.load(attributes_file)
        rules = json.load(myfile)
        return rules, attributes_file

    def find_rule(self, rules, attributes, rules_list):
        question = rules_list[-1]
        answers = []
        for i in attributes:
            if i['key'] == question:
                answers = i['values']
                break
        return question, answers
