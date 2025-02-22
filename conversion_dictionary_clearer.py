"""
About Dictionary
----------------
Phyton dictionary denoted with curly braces {}. It contains a pair of data consisting
of key and value {key:value}.

  d = {"coding" : "Phyton"}
  d["coding"]
  output: "Phyton"
  
  The value of dictionary could be another "child" dictionary. Then to access the value of
  "child" dictionary, we need to use two key:
  d =  {"coding" : {"Phyton": "Easy", "C": "Medium", "Java", "Hard"} }
  d["coding"]["C"]
  output: "Medium"
"""

conversion_factors = {"distance": {"mm":1,
                                   "cm":0.1,
                                   "m":0.001,
                                   "km":0.000001,
                                   "inch": 0.0393701,
                                   "feet":0.00328084,
                                   "yard":0.00109361,
                                   "miles":6.21371e-7},
                      
                      "weight": {"mg":1,
                                 "gr":0.01,
                                 "kg":0.000001},
                      
                      "time":   {"hour": 1,
                                 "minute": 60,
                                 "second": 60*60,
                                 "day":1/24,
                                 "week":1/(24*7),
                                 "month":1/(24*7*4),
                                 "year":1/(365*24),
                                 "decade":1/(24*7*4*12*10),
                                 "century":1/(24*7*4*12*10*10)}
                     }

input number = 1
base_factor = conversion_factors["time"]["year"]
convert_factor = conversion_factors["time"]["day"]
converted_value = input_number / base_factor * conver factor
print(converted value)