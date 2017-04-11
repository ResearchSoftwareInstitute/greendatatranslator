 1186  git add __init__.py 
 1187  git commit -am "api"
 1188  git push origin master
 1189  emacs setup.py 
 1190  git commit -am "api"
 1191  git push origin master
 1192  git tag 0.5 -m "with med/biochem"
 1193  git push --tags origin master
 1194  python setup.py register -r pypitest
 1195  python setup.py sdist upload -r pypitest
 1196  python setup.py register -r pypi
 1197  python setup.py sdist upload -r pypi
 1198  python -m pip --no-cache-dir uninstall greentranslator
 1199  python -m pip --no-cache-dir install greentranslator==0.5
 1200  /projects/stars/venv/bin/python -c "from greentranslator.api import GreenTranslator"
 1201  pwd
 1202  cd ../../datatranslator/python-client/
 1203  python setup.py install
