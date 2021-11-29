# cs1660-term-project

## 1) Getting the images on GKE

1. pull all the images onto gcp fom my dockerhub
    * e.g. "docker pull pob6/driver"
2. tag all the images with the gcp repo you wish to use and the project ID
    * e.g. "docker tag pob6/driver us.gcr.io/PROJECT_ID/pob6/driver"
3. No we can push the images onto the gcp remote repository
    * e.g. "docker push us.gcr.io/PROJECT_ID/pob6/driver"
4. After all the images are pushed go to the kubernetes engine

## 2) Creating the application
1. Create a cluster - the configuration doesn't matter we just need a cluster to host our application
2. Wait for the cluster to be created
3. Connect to the new cluster and upload [final-yaml/compose-final.yaml](final-yaml/final-compose.yaml)
4. run `kubectl apply -f compose-final.yaml` this will create all the workloads and services
5. You can now grab a link to the gui from the services tab - from the gui you can access any of the other applications