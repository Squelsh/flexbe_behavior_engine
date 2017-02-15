#!/usr/bin/env python
import rospy

from flexbe_core.core.preemptable_state import PreemptableState


class SemanticPropertiesState(PreemptableState):
    """
    A state that has semantic properties, like Hardware requirements
    """

    def __init__(self, *args, **kwargs):
        super(SemanticPropertiesState, self).__init__(*args, **kwargs)
        self.__execute = self.execute
        self.execute = self._semantic_props_execute

        self._semantic_properties = []

    def set_semantic_properties(self, semantic_properties):
        self._semantic_properties = semantic_properties

    def get_semantic_properties(self):
        return self._semantic_properties

    def _semantic_props_execute(self, *args, **kwargs):
        outcome = self.__execute(*args, **kwargs)
        return outcome
