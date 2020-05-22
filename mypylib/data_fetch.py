from scipy.io import loadmat

global Age, Sex, D, D_list, Sex_list, fs
Sex = 14
Age = 13
D = 15
fs = 500
D_list = ['AF', 'I-AVB', 'LBBB', 'Normal',
'PAC', 'PVC', 'RBBB', 'STD', 'STE']
Sex_list = ['Female','Male']



def data_loader(file_name, file_path = 'Training_WFDB/'):

  ''' 
  Note that the standard data format for machine learning 
  with sklearn and tensorflow is the following:

    (bactch size, data_points, channels)
    
    for example -> (32, 9500, 12)

  So this function will return one batch of data
  with the standard format i.e.

    (data_points, channels)

    for example -> (9500, 12)


  '''


  data = loadmat('Training_WFDB/A6349.mat')['val']
  return data.T


def Get_Info(file_name, file_path='Training_WFDB/', encoded = True):
  with open(file_path + file_name) as f:
    lines = f.readlines()

  age = lines[Age][6:8]

  sex = lines[Sex]

  d = lines[D]

  if encoded == True:
    return age, sex_encoder(sex), disease_encoder(d)


  return age, sex, d



'''
Here is the order of the classes:


 0   AF - Atrial fibrillation
 1   I-AVB - First-degree atrioventricular block
 2   LBBB - Left bundle branch block
 3   Normal - Normal sinus rhythm
 4   PAC - Premature atrial complex
 5   PVC - Premature ventricular complex
 6   RBBB - Right bundle branch block
 7   STD - ST-segment depression
 8   STE - ST-segment elevation



Sex:

 0 --> Female
 1 --> Male

'''

def disease_encoder(d_info):
  for index, elem in enumerate(D_list):
    if elem in d_info:
      return index



def sex_encoder(age_info):
  for index, elem in enumerate(Sex_list):
    if elem in age_info:
      return index

def disease_decoder(disease_number):
  return D_list[disease_number]

def sex_decoder(sex_number):
  return Sex_list[sex_number]


  