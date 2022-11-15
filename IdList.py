class IdList:

    def __init__(self, traces):
        self.ids = []       # Preliminary Phase IDs
        self.tids = []      # Trace IDs
        self.idList = {}    # Actual Data Structure
                            #           ID
                            # tid   |   Occurence
        self.RXMap = {}     # Right-eXtention-Map indicate pairwise extention relationship
        self.LXMap = {}     # Left-eXtention-Map indicate pairwise extention relationship
        self.max_gap = 1        # Gap is 1 by default

        self.build_list(self, traces)

    # Construct the Id List given the list of preliminary phases as list of sets: [{phase_1}, {phase_2}, ..., {phase_n}]
    def build_list(self, traces):
        if not isinstance(traces, list):
            print('Input Traces must be list object.')
            raise TypeError

        # Itterate Each Trace
        trace_idx = 0
        for trace in traces:
            for event_idx in range(len(trace)):
                phase = trace[event_idx]

                # Check if phase already exists
                if phase not in self.ids:
                    self.idList[len(self.ids)] = [[] for _ in range(len(traces))]
                    self.RXMap[len(self.ids)] = set()
                    self.LXMap[len(self.ids)] = set()
                    self.ids.append(phase)

                phase_idx = self.ids.index(phase)

                # Insert to IdList
                self.idList[phase_idx][trace_idx].append(self.component_idx)

                # Update Extention Map
                for gap in range(1, self.max_gap + 1):
                    # Left Extention
                    idx = self.component_idx - gap
                    if idx >= 0:
                        self.LXMap[phase_idx].add(self.ids.index(self.components[idx]))
                    # Righ Extention
                    idx = self.component_idx + gap
                    if idx < len(self.components):
                        # Check if phase already exists in ids
                        if self.components[idx] not in self.ids:
                            self.idList[len(self.ids)] = [[] for _ in range(len(traces))]
                            self.LXMap[len(self.ids)] = set()
                            self.RXMap[len(self.ids)] = set()
                            self.ids.append(self.components[idx])
                        self.RXMap[phase_idx].add(self.ids.index(self.components[idx]))

