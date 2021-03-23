def rename(value):
  value2 = ''.join(str(value))
  newname = value2.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace(" ", "")
  return str(newname)