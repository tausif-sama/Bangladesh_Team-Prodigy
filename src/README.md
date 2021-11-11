Steps
====

Akashe keno eto tara.

## 1. Data Collection

[Notebook](autopilot_data_collection.ipynb)
<br>
The goal is to gather data reflecting correct driving, i.e images with correctly annotated steering and throttle values. While driving with the gamepad, we recorded camera frames and corresponding steering and throttle values. 

## 2. Training

[Notebook](autopilot_training.ipynb)
<br>
Training process consists of iterating over previously gathered datasets and feeding them into the CNN. CNN network is built of the resnet18 backbone and a stack of dropout and fully connected layers.

    self.network = torchvision.models.resnet18(pretrained=pretrained)
    self.network.fc = torch.nn.Sequential(
        torch.nn.Dropout(p=DROPOUT_PROB),
        torch.nn.Linear(in_features=self.network.fc.in_features, out_features=128),
        torch.nn.Dropout(p=DROPOUT_PROB),
        torch.nn.Linear(in_features=128, out_features=64),
        torch.nn.Dropout(p=DROPOUT_PROB),
        torch.nn.Linear(in_features=64, out_features=OUTPUT_SIZE)
    )

## 3. Testing

[Python script](autopilot_testing.py)
<br>
Finally, with the trained model we tested on the track. With the relatively lightweight CNN, Jetson operates at ~30 FPS, successfully drives the track in both directions.


