ssh-add -D
ssh-add ../rsa.key
git pull
gcloud app deploy $PWD/app.yaml
