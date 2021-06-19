from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        self.writeVInt(2021122)  # Timestamp (Year * 1000 + DayOfYear)
        self.writeVInt(75735)  # Second Timestamp
        self.writeVInt(5000)  # Score
        self.writeVInt(5000)  # Highest Score
        
        self.writeVInt(100)
        self.writeVInt(97)  # Trophy Road rewardnik
        self.writeVInt(5000)  # Exp
        
        self.writeDataReference(28, 0)  # Player Icon
        self.writeDataReference(43, 0)  # Name Color
        
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0)
        self.writeVInt(1000)
        self.writeVInt(10)
        self.writeVInt(20)
        self.writeVInt(30)
        
        #===sub_53AF00===#
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Array
        #================#
        
        self.writeByte(0)  # 3 Boolean
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)  # Array (v16)
        
        self.writeVInt(0)  # Array (v20)
        
        self.writeVInt(200)
        self.writeVInt(0)
        
        self.writeVInt(0)  # Array (v23)
        
        self.writeVInt(99999)
        self.writeVInt(0)
        
        self.writeDataReference(16, 0)  # Selected Brawler
        
        self.writeString("RU")
        self.writeString("ServerBSvvv")  # content creator
        
        self.writeVInt(1)  # Array (v25)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1)  # Array (v28)
        self.writeVInt(0)
        self.writeDataReference(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(1)  # Array (v31) Season Data
        for x in range(1):
            self.writeVInt(4)
            self.writeVInt(0)
            self.writeByte(0)
            self.writeVInt(1)
            self.writeByte(0)
        
        self.writeVInt(0)  # Array (v34)
        
        self.writeByte(1)
        self.writeVInt(0)
        
        self.writeByte(1)
        self.writeVInt(0)
        
        # LogicClientHome CHUNK 2
        
        self.writeVInt(0)  # v4
        
        self.writeVInt(16)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24]:
            self.writeVInt(x)
        
        self.writeVInt(1)  # Events
        #Event Start
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(75992)
        self.writeVInt(10)
        self.writeDataReference(15, 7)
        self.writeVInt(3)
        self.writeVInt(3)
        self.writeString("TID_WEEKEND_EVENT")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Array (v4) modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0)  #sub_5F0248
        self.writeVInt(0)
        #Event End
        
        self.writeVInt(0)  # Upcoming Events
        
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        self.writeVInt(0)  # Array
        
        self.writeByte(0)
        
        self.writeVInt(0)  # Array (v18)
        
        self.writeVInt(0)  # Array (v21)
        
        self.writeVInt(0)  # Array (v24)
        
        self.writeVInt(0)  # Array (v27)
        
        self.writeByte(0)  # 2 boolean arrays
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeVInt(0)  # v8 (Notification Factory)
        self.writeVInt(0)  # v9
        # Array for v8 Here (yes, under v9)
        
        self.writeByte(0)  # v10
        self.writeVInt(0)  # Array (v11)
        
        self.writeVInt(0)  # Array result
        
        # LogicClientAvatar
        
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString(None)  # Name
        self.writeByte(0)  # NameSetByUser
        self.writeInt(0)
        
        self.writeVInt(8)  # Commodity Array Count
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(self.player.tutorialState)  # Tutorial State
        
        self.writeVInt(2)
        
        print("[*] Message OwnHomeData has been sent.")
