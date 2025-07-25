rm -rf /opt/ANDRAX/john

cd src

./configure

if [ $? -eq 0 ]
then
  # Result is OK! Just continue...
  echo "Configure... PASS!"
else
  # houston we have a problem
  exit 1
fi

make -s clean

if [ $? -eq 0 ]
then
  # Result is OK! Just continue...
  echo "Make clean... PASS!"
else
  # houston we have a problem
  exit 1
fi

make

if [ $? -eq 0 ]
then
  # Result is OK! Just continue...
  echo "Make... PASS!"
else
  # houston we have a problem
  exit 1
fi

cd ..

cp -Rf run /opt/ANDRAX/john

if [ $? -eq 0 ]
then
  # Result is OK! Just continue...
  echo "Copy PACKAGE... PASS!"
else
  # houston we have a problem
  exit 1
fi

python3 -m venv /opt/ANDRAX/john/venv

source /opt/ANDRAX/john/venv/bin/activate

/opt/ANDRAX/john/venv/bin/pip3 install -r requirements.txt

cp -Rf andraxbin/* /opt/ANDRAX/bin

chown -R andrax:andrax /opt/ANDRAX
