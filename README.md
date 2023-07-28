# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/<ProjectName>/<AppName>  --project=<ProjectName>
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/<ProjectName>/<AppName> --platform managed  --project=<ProjectName> --allow-unauthenticated
```

gcloud builds submit --tag gcr.io/market-garden-394202/demo  --project=smarket-garden-394202

gcloud run deploy --image gcr.io/market-garden-394202/demo --platform managed  --project=market-garden-394202 --allow-unauthenticated

Project name: Market Garden Project ID: market-garden-394202