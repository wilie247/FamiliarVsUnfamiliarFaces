import torch
import pandas as pan
import urllib
import pathlib

class Behavior:
    def __init__(self, url, fileName):
        self.url = url
        self.fileName = fileName

    def fetchDataset(self):
        response = urllib.request.urlopen(self.url)
        Text = response.read()
        Text = Text.decode("utf-8").split('\n')
        print(len(Text))

    def returnTimeStamps(self):

        return ""


subs = ['S01', 'S02', 'S03']
exps = ['/FaceOnlyExperiment/', '/FaceTextNameExperiment/', '/FaceSoundNameExperiment/']
fName = 'Response.txt'  # EEG.csv
FAurl = 'https://raw.githubusercontent.com/wilie247/MemoryFace_NameEEG_EYE_track_PsychopyReponseDatasets/main/'
FAurl = FAurl + subs[0] + exps[0] + fName
Beh = Behavior(FAurl, fName)

Beh.fetchDataset()