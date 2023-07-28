# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/<ProjectName>/<AppName>  --project=<ProjectName>
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/<ProjectName>/<AppName> --platform managed  --project=<ProjectName> --allow-unauthenticated
```

gcloud builds submit --tag gcr.io/sandbox-394103/demo  --project=sandbox-394103

gcloud run deploy --image gcr.io/sandbox-394103>/demo --platform managed  --project=sandbox-394103 --allow-unauthenticated