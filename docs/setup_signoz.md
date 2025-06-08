# Setup an opensource collector

[Signoz](https://signoz.io/) is an opensource collector that can be used to collect traces, metrics and logs and display them in a UI.

## Prerequisites

You need to have docker installed and running.

## Install and launch signoz container

#### Step 1: Clone the signoz repository

```bash
git clone https://github.com/SigNoz/signoz.git
cd signoz/deploy/docker
```

#### Step 2: Build the signoz container

```bash
docker compose up
```

#### Step 3: Access the signoz UI

The ui is accessible at [http://localhost:8080](http://localhost:8080) by default.