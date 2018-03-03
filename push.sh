ssh-add -D
ssh-add ../write.key
git add .
git commit
git push
ssh-add -D

