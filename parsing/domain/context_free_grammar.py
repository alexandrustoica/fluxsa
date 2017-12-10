from typing import List

from parsing.domain.non_terminal import NonTerminal
from parsing.domain.symbol import Symbol
from parsing.domain.terminal import Terminal
from parsing.domain.rule import Rule


class ContextFreeGrammar:

    def __init__(self, non_terminals: List[NonTerminal],
                 alphabet: List[Terminal],
                 rules: List[Rule],
                 start: NonTerminal):
        self._non_terminals = non_terminals
        self._alphabet = alphabet
        self._rules = rules
        self._start = start

    @property
    def rules(self):
        return self._rules

    def rules_of(self, source: Symbol) -> List[Rule]:
        return [] if source.type == Terminal else \
            list(filter(lambda rule: rule.left == source, self._rules))

    def __str__(self):
        return "NonTerminals: {}\nAlphabet: {}\nRules: {}\nStart: {}"\
            .format("".join(str(non_terminal) + " " for non_terminal in self._non_terminals),
                    "".join(str(terminal) + " " for terminal in self._alphabet),
                    "".join("\n\t{}".format(str(rule)) for rule in self._rules),
                    "" + str(self._start))

    def extend(self):
        return ContextFreeGrammar(self._non_terminals + [NonTerminal("E")],
                                  self._alphabet,
                                  self._rules + [Rule(NonTerminal("E"), [self._start])],
                                  NonTerminal("E"))

    @staticmethod
    def from_dictionary(source: dict):
        non_terminals = [NonTerminal(item) for item in source.get('non-terminals')]
        terminals = [Terminal(item) for item in source.get('terminals')]
        rules = [Rule.from_string(rule) for rule in source.get('rules')]
        start = NonTerminal(source.get('start'))
        return ContextFreeGrammar(non_terminals, terminals, rules, start)
