


t = "\t"
class PyFlow:
    def __init__(self, data):
        self.data= data
        self.tunnel= []
        self.Listeners= 0
        self.Updates= 0
        self.snapshots = [*self.data] if type(self.data) is list else [self.data]
        
        
    def update(self, transformer):
        update = transformer(self.data)
        newUpdate = update[len(self.data):] if type(self.data) is list else update
        self.data = update
        if self.snapshots[0] != self.data:
            match self.data:
               case list():
                    self.snapshots.extend(newUpdate)
               case _:
                   self.snapshots.append(newUpdate)
        self.Updates = self.Updates+1
        for listener in self.tunnel:
            listener(self.data)

            
    def collect(self, collector):
        collector(self.data)
        self.tunnel.append(collector)
        self.Listeners = len(self.tunnel)
        
    def collectBegin(self, snapCollector):
        for shots in range(len(self.snapshots)):
            snapCollector(self.snapshots[:shots+1]) if type(self.data) is list else snapCollector(self.snapshots[shots])
        self.tunnel.append(snapCollector)
        
    def snapshot(self):
        return self.snapshots

    
        

x = PyFlow([10])

x.collect(
lambda state: print("Displayer: ", state)
)


x.update(
lambda state: state + [20]
)

x.update(
lambda state: state + [30]
)

x.update(
lambda state: state + [40]
)

x.collectBegin(
lambda state: print("Snapshots: ", state)
)


x.update(
lambda state: state + [50]
)
x.update(
lambda state: state + [60]
)



