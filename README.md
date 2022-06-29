# insights-etl
Scripts which generate insights from the kgraph and store them in our insight catalog

This repo contains functions which build insights using the kgraph service and deploys them to the insight catalog in S3. The Digital Ocean App Platform can be used to run these functions.

To run/deploy, auth with digital ocean then

```doctl serverless deploy "insight agents" --remote-build```

```doctl serverless functions invoke agents/top_subjects```

Make sure to have a .env file in root directory with
```
AWS_SERVER_PUBLIC_KEY="something2"
AWS_SERVER_SECRET_KEY="something"
```
