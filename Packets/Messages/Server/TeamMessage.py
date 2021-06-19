from Utils.Writer import Writer
from database.DataBase import DataBase
import random


class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeByte(0)
        self.writeVInt(1)
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeVInt(100)  # Timestamp
        self.writeByte(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(15, 7)
        self.writeByte(0)
        
        self.writeVInt(1)  # Players Array
        self.writeByte(1)  # Boolean
        self.writeInt(0)
        self.writeInt(1)
        self.writeDataReference(16, 0)
        self.writeVInt(0)  # Datareference NULL
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(3)
        self.writeByte(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("Ultracore")
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)  # Array v9
        
        self.writeVInt(0)  # Array v14
        
        self.writeVInt(0)  # Array v19
        
        self.writeByte(0)
        
        print("[*] Message TeamMessage has been sent.")
