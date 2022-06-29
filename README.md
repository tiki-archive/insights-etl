# insights-etl
Scripts which generate insights from the kgraph and store them in our insight catalog

This repo contains functions which build insights using the kgraph service and deploys them to the insight catalog in S3. The Digital Ocean App Platform can be used to run these functions.

# Current setup

## Deployment
To run/deploy, auth with digital ocean using doctl then

```doctl serverless deploy "insight agents" --remote-build```

```doctl serverless functions invoke agents/top_subjects```

Make sure to have a .env file in repo root directory with
```
AWS_SERVER_PUBLIC_KEY="something2"
AWS_SERVER_SECRET_KEY="something"
```

## Dailing Running 
(For some future TIKI employee who drew the short stick and is looking at this) Right now the function is run daily through a crontab on a dig ocean cloud droplet. The ssh key for it is in tiki password manager, though you can just open the console through dig ocean cloud panel. The cron tab calls a script which runs the cloud function once per day. 
