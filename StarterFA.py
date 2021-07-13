import torch
import urllib
import math
import pandas as pd
import requests
import io


dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0") # Uncomment this to run on GPU

# Create random input and output data
folder = "S02/FaceOnlyExperiment/"

url = 'https://raw.githubusercontent.com/wilie247/MemoryFace_NameEEG_EYE_track_PsychopyReponseDatasets/main/S02/FaceOnlyExperiment/EEG.csv?token=AG6DRHQ65DKNLTLSNYPPYEDA5IAWI'
FAurl = 'https://raw.githubusercontent.com/wilie247/MemoryFace_NameEEG_EYE_track_PsychopyReponseDatasets/main/'
Response = 'Response.txt'
EEGfile = 'EEG.csv'
myurl = FAurl + folder + EEGfile

p = pd.read_csv(myurl)
print(p.head())

#download = requests.get().content

# Reading the downloaded content and turning it into a pandas dataframe

response = urllib.request.urlopen(myurl)
Text = response.read()
Text=Text.decode("utf-8")
print(Text)