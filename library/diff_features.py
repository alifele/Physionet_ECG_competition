import numpy as np
from scipy.signal import argrelextrema

def diff(data):
  return data[1:] - data[:-1]
  


################################################### 

def diff_data(data, append_mode = 'same_append'):
  '''

  this function will return the beat rate of the record
  plus the derivative of the beat rate and also the 
  second derivative of the signal



  Note that you should feed this function with the whole
  channels data -->  (data_points, channels)

  Note that tha batch size should be one. I may implement
  the other one that can handle tha bathces of data




  the append modes can be :
  -> same_append
  -> mean_append
  '''
  fs = 500
  N = data.shape[0]
  t = np.linspace(0, N/fs, N)

  Sumed = np.zeros(data.shape[0])
  for i in range(12):
    Sumed += np.abs(data[:,i])

  #plt.figure(figsize=(15,4))
  #plt.plot(t,Sumed)
  peaks_arg = argrelextrema(Sumed, np.greater, order=150)
  #plt.plot(t[peaks_arg], Sumed[peaks_arg],'o')
  #plt.grid()
  beat_times = t[peaks_arg]

  beat_rate = 1/diff(beat_times)
  diff_beat_rate  = diff(beat_rate)
  ddiff_beat_rate  = diff(diff_beat_rate)


  if append_mode == 'mean_append':

    diff_beat_rate = np.append(diff_beat_rate, np.mean(diff_beat_rate).tolist())
    ddiff_beat_rate = np.append(ddiff_beat_rate, [np.mean(ddiff_beat_rate).tolist()]*2)

  if append_mode == 'same_append':
    
    diff_beat_rate = np.append(diff_beat_rate, [diff_beat_rate[-1]])
    ddiff_beat_rate = np.append(ddiff_beat_rate, [ddiff_beat_rate[-1]]*2)

  return [beat_rate, diff_beat_rate, ddiff_beat_rate]



#########################################################

def diff_feature_batch(data, all_same_size = True, size_ = 50):
  diff_data_batch = []
  for data_elem in data:
    diff_data_val = diff_data(data_elem, append_mode='mean_append')
    diff_data_batch.append(diff_data_val)

  if all_same_size == True:
    clear_diff_features_batch = diff_feature_appender(diff_data_batch)
    return clear_diff_features_batch

  return diff_data_batch



def diff_feature_appender(diff_data_batch):
  clear_features_batch = []
  for elem in diff_data_batch:
    sub_dummy = []
    for diff_order in range(3):
      dummy = elem[diff_order]
      if len(dummy)<50:
        dummy = np.append(dummy, [dummy[-1]]*(50-len(dummy)))
      else:
        dummy = dummy[:50]
      sub_dummy.append(dummy)

    sub_dummy = np.array(sub_dummy)
    #print(sub_dummy.T.shape)
    clear_features_batch.append(sub_dummy.T)

  return np.array(clear_features_batch)



