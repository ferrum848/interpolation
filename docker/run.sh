docker run --rm -it \
			--net=host \
			-v `pwd`/../src:/src_interpolation \
			--entrypoint="" \
			-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/root/.Xauthority \
			-v /opt/pycharm:/pycharm \
    		-v /home/andrew/pycharm-settings/textgen:/root/.PyCharmCE2018.2 \
    		-v /home/andrew/pycharm-settings/textgen__idea:/workdir/.idea \
			interpolation bash

