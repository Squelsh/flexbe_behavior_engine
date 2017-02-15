#!/usr/bin/env python

from flexbe_core.core.preemptable_state_machine import PreemptableStateMachine


class SemanticPropertiesStateMachine(PreemptableStateMachine):
    """
    A state machine that can collect the properties of all its states.
    """

    def __init__(self, *args, **kwargs):

        super(SemanticPropertiesStateMachine, self).__init__(*args, **kwargs)

    def collect_semantic_properties(self):
        """
        @return: A dictionary of state names and a list of their semantic properties. Empty list if no props are available.
        """
        tmp_semantic_props = {}
        for state in self._ordered_states:
            if state.get_semantic_properties():
                tmp_semantic_props[state.name] = state.get_semantic_properties()
        return tmp_semantic_props
