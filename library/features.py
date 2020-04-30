import numpy as np


def diff(data):
  return data[1:] - data[:-1]
  


################################################### 

def diff_data(data, mean_append = True):
  '''

  this function will return the beat rate of the record
  plus the derivative of the beat rate and also the 
  second derivative of the signal



  Note that you should feed this function with the whole
  channels data -->  (data_points, channels)

  Note that tha batch size should be one. I may implement
  the other one that can handle tha bathces of data

  '''


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

  if mean_append == True:
    
    diff_beat_rate = np.append(diff_beat_rate, np.mean(diff_beat_rate).tolist())
    ddiff_beat_rate = np.append(ddiff_beat_rate, [np.mean(ddiff_beat_rate).tolist()]*2)


  return [beat_rate, diff_beat_rate, ddiff_beat_rate]



#########################################################