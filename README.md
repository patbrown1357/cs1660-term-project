# cs1660-term-project

## To run the docker images on kubernetes

1. pull all the images onto gcp
    * e.g. "docker pull pob6/driver"
2. tag all the images with the gcp repo you wish to use and the project ID
    * e.g. "docker tag pob6/driver us.gcr.io/PROJECT_ID/pob6/driver"
3. No we can push the images onto the gcp remote repository
    * e.g. "docker push us.gcr.io/PROJECT_ID/pob6/driver"
4. After all the images are pushed go to the kubernetes engine
5. Create a new deployment
6. Create a container for each of the images using the "select from preexisting image option"
7. Create the deployment by hitting the "Deploy" button