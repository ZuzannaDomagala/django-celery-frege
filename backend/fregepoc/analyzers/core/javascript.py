from fregepoc.analyzers.core.base import AnalyzerFactory
from fregepoc.analyzers.core.generic import GenericAnalyzer
from fregepoc.repositories.constants import ProgrammingLanguages


@AnalyzerFactory.register(ProgrammingLanguages.JS)
class JavascriptAnalyzer(GenericAnalyzer):
    pass
