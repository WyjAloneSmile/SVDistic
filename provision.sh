# Move git away.
mv ./.git ../

# Create run.sh file.
python3 misc/infer.py 6 > misc/run.sh

# Provision p2.xlarge on AWS.
docker-machine create --driver amazonec2 \
                      --amazonec2-region us-west-2 \
                      --amazonec2-zone b \
                      --amazonec2-ami ami-db710fa3 \
                      --amazonec2-instance-type m4.2xlarge \
                      --amazonec2-vpc-id REPLACE_THIS \
                      --amazonec2-access-key REPLACE_THIS \
                      --amazonec2-secret-key REPLACE_THIS \
                      --amazonec2-root-size 100 \
                      --amazonec2-security-group REPPLACE_THIS \
                      aws$1

# Restart the instance first, to be sure we are running the latest installed kernel
docker-machine restart aws$1

# Send our files over
docker-machine scp -r . aws$1:/home/ubuntu
# Send the resources
docker-machine scp ./remote_setup.sh aws$1:/home/ubuntu/remote_setup.sh
docker-machine scp ./misc/run.sh aws$1:/home/ubuntu/run.sh

# Download dataset
docker-machine ssh aws$1 -- "sudo bash /home/ubuntu/remote_setup.sh"

