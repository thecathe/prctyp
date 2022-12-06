from enum import Enum

class PrcKind(Enum):
    fail = -1
    none = 0
    term = 1
    send = 2
    recv = 3
    delc = 4
    delt = 5
    sett = 6
    drec = 7
    recc = 8
    buff = 9
    scope = 10

class Prc:
    kind: PrcKind
    cont: int # index of all processes
    
    data = {}
    
    def __init__(self, _kind: PrcKind, _cont: int) -> None:
        self.kind = _kind
        self.cont = _cont

        # load data depending on kind
        if self.kind == PrcKind.fail:
            pass
        elif self.kind == PrcKind.none:
            pass
        elif self.kind == PrcKind.term:
            pass
        elif self.kind == PrcKind.send:
            self.data["chan"] = None
            self.data["msg"] = None
        elif self.kind == PrcKind.recv:
            self.data["chan"] = None
            self.data["msg"] = None
            self.data["time"] = None
            self.data["after"] = None
        elif self.kind == PrcKind.delc:
            self.data["lhs"] = None
            self.data["op"] = None
            self.data["rhs"] = None
        elif self.kind == PrcKind.delt:
            self.data["time"] = None
        elif self.kind == PrcKind.sett:
            self.data["timer"] = None
        elif self.kind == PrcKind.drec:
            pass
        elif self.kind == PrcKind.recc:
            pass
        elif self.kind == PrcKind.buff:
            self.data["sender"] = None
            self.data["recver"] = None
        elif self.kind == PrcKind.scope:
            self.data["p"] = None
            self.data["q"] = None

class Par(Prc):
    lhs: Prc
    rhs: Prc
    
    def __init__(self, _lhs: Prc, _rhs: Prc) -> None:
        self.lhs = _lhs
        self.rhs = _rhs

class Scope:
    endpoints = {}
    prc: Prc

    def __init__(self, _p: str, _q: str, _prc: Prc) -> None:
        self.endpoints["p"] = _p
        self.endpoints["q"] = _q
        
        self.prc = _prc

prcs = [
    Prc(PrcKind.term)
]

test = Scope("p", "q", 
             Par(
                 Prc()
             )
)
