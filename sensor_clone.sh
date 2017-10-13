git init
git remote add -f origin https://github.com/bambookchos/Weather-serv.git
git config core.sparseCheckout true
echo "Sensor/" >> .git/info/sparse-checkout
git pull origin dev
