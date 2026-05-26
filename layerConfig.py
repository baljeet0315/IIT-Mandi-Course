layer_config={
    "units" : 64,
    "activation" : "relu",
    "dropout" : 0.5
}

layer_config["dropout"] = 0.3
layer_config["use_bias"] = True


print("All config settings:", layer_config)

for key,value in layer_config.items():
    print(f"{key}:{value}")