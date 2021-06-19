from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players

from Utils.Reader import BSMessageReader

from Packets.Messages.Server.OwnHomeData import OwnHomeData

class TeamStartBattleMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.Type = self.read_string()
        self.Event = self.read_string()

    def process(self):
        self.player.tutorialState = 1
        OwnHomeData(self.client, self.player).send()
        print("[*] Friendly battle started")