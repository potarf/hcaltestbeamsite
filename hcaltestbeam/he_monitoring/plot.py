# plot temperature and humidity

import matplotlib.pyplot as plt
import numpy as np
import imageio

def plot(filename,unit,plot_directory):
  data_directory = "measurements/"
  data = open(data_directory+filename+'.txt','r')
  values = []
  num_rm = 0
  for line in data:
    parsed = line.split(" ")
    if parsed[0] == "#":  continue
    #print parsed
    val = float((parsed[-1].split("\n"))[0])
    values.append(val)
    num_rm += 1
  
  data.close()
  
  mean = np.round(np.mean(values), 3)
  std  = np.round(np.std(values), 3)

  vmin, vmax = 0.0, 100.0
  if "Temperature" in unit:
    vmin, vmax = 0.0, 50.0 # deg C
  elif "Humidity" in unit:
    vmin, vmax = 0.0, 10.0 # percent

  fig = plt.figure()
  
  # line graph (value vs readout modudle)
  plt.plot(values)
  plt.text(10, 9, filename)
  plt.text(10, 9, filename)
  plt.text(40, 9, r'$\mu='+str(mean)+',\ \sigma='+str(std)+'$')
  plt.axis([0,num_rm,vmin,vmax])
  plt.ylabel(unit)
  plt.xlabel("Readout Module")
  plt.title("Monitoring "+unit)
  plt.grid(True)
  #plt.show()
  fig.savefig(plot_directory+filename+"_1.png")
  plt.clf()
  
  # histogram (count vs value)
  n, bins, patches = plt.hist(values, 20, facecolor='g', alpha=0.75)
  plt.text(2, 18, filename)
  plt.text(2, 16, r'$\mu='+str(mean)+',\ \sigma='+str(std)+'$')
  plt.axis([vmin,vmax,0,20])
  plt.ylabel("Number of Readout Modules")
  plt.xlabel(unit)
  plt.title("Monitoring "+unit)
  plt.grid(True)
  #plt.show()
  fig.savefig(plot_directory+filename+"_2.png")
  plt.clf()

def makeGif(filenames, gifname, unit):
  plot_directory = "images/"
  for append in [1,2]:
    with imageio.get_writer(gifname+'_'+str(append)+'.gif', mode='I',duration=1) as writer:
      for filename in filenames:
        plot(filename, unit, plot_directory)
        image = imageio.imread(plot_directory+filename+"_"+str(append)+".png")
        writer.append_data(image)

def getFiles(file_set):
  file_list = []
  files = open(file_set,'r')
  for f in files:
    line = f.split('\n')[0]
    file_list.append(line)
    print line
  return file_list

if __name__ == "__main__":
  #plot("humidity-5-JUL-2017","Relative Humidity")
  #plot("temperature-5-JUL-2017","Temperature deg C")
  files = getFiles("humidity_files.txt")
  makeGif(files,"humidity","Relative Humidity")






