hyperparams = {
    "learning_rate": 0.01,
    "epochs": 100,
    "batch_size": 32
}


print("Learning Rate:", hyperparams["learning_rate"])

hyperparams["optimizer"] = "Adam"

print("All Hyperparams:", hyperparams)

print("\nAll settings:")

for key, value in hyperparams.items():
    print(f"  {key}: {value}")