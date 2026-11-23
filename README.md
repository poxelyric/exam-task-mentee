# retospect

## What I planned
Connect github actions aws using oidc

To deploy the app to aws I wanted to use terraform for IaC

use s3 bucket as terraform backend

deploy the app on ecs for simplicity

In order to allow for rollback only changes to app code change the app version and the IaC can reference an older image tag.

## What went wrong

I underestimated the time it would take to write a terraform configuration and started lookng for simpler alternatives when I realized I don't have time.

I wasn't able to do versioning in the pipline in time. If I had more time I think I would have the pyproject.toml be the source for the app versionion and decouple the infra version from the app version. This can be achieved with two tags, one for infra and one for app. A change to the infrastructure should bump
the infra tag but not the app tag.

## What I would do different
I am more familiar with k8s than aws services. In retrospect maybe I should have created a terraform configuration to deploy
an EKS cluster which I already have, configure an argoCD addon and deploy the app in the way I am familiar with.
That would also allow me to decouple my IaC (eks with addon with terraform) from my CaC (argocd app definition).
