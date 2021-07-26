from typing import overload

class StatSummarizer:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetOutputString(self) -> str: ...
    def PrintStepStats(self) -> None: ...
    def ProcessStepStats(self, arg0) -> None: ...
    def ProcessStepStatsStr(self, arg0: str) -> None: ...
