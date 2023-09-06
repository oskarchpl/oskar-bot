export TERM=xterm;
rm -rf botrepo;
git clone https://<github_token>:x-oauth-basic@github.com/<username>/<repo>.git botrepo;
cd botrepo;
bash start.sh;

                   