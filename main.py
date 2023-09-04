module = __import__("models", fromlist=[""]) 
model = getattr(module, 'Myobject')() # optional with config

print(model)
print(model.tmp)
