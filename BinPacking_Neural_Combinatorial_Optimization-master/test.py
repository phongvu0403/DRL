import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Environment(object):
    def __init__(self, numServers, numSlots, numDescriptors):
        
        # Environment properties
        self.numServers=numServers
        self.numSlots=numSlots
        self.numDescriptors=numDescriptors
        self.cells=np.empty((numServers,numSlots))
        self.cells[:]=np.nan
        self.service_properties=[{"nVNF": 4} for _ in range(numDescriptors)]
        self.vlinks=np.empty((20,20)) #virtual links
        self.bwlinks=np.empty((20,20)) #bandwidth of link what connect 2 VNF in 1 SFC
        self.links_cap=np.empty((1,5)) #current capacity of each Server

        
        # Placement properties
        self.nVNF = 0   #service length
        self.SFC = None
        self.placement = None
        self.first_slots = None
        self.reward = 1
        self.invalidPlacement = False

        # Assign ns properties within the environment
        self.vlinks_properties() # virtual links properties
        self.bwlinks_properties() # property of bandwidth of physical links between 2 VNF
        self.links_cap_properties() # current capacity properties

    def vlinks_properties(self):
        for i in range(20):
            for j in range(20):
                self.links[i][j] == None
                self.links[i][i] == 0
                self.links[i][j] == self.links[j][i]

    def bwlinks_properties(self):
        for i in range(20):
            self.links[i][i] == 0
            self.links[i][]


    def links_available(self):


    def _placeSubPacket(self,server,link,vnf):
        """ Place subPacket """

        occupied_slot = None
        for slot in range(len(self.cells[server])):
            for i in range(20):
                if self.links[i]
            if np.isnan(self.cells[server][slot]):
                self.cells[server][slot] = vnf
