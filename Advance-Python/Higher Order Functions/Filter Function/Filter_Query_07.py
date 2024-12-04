# Problem 8: Filtering Dictionary Keys
# You are working with a configuration file in the form of a dictionary 
# where the keys represent feature toggles for a new product release.
# You need to filter out keys that are not enabled (i.e., where the value is False).

config = {
    "feature_a": True,
    "feature_b": False,
    "feature_c": True,
    "feature_d": False
}

filter_disabled = {k:v for k,v in filter(lambda x:x[1]==False,config.items())}
print(filter_disabled)