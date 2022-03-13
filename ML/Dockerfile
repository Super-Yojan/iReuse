FROM python


COPY . .

RUN pip install tensorflow

RUN pip install keras numpy pillow scipy h5py matplotlib opencv-python keras-resnet

RUN pip install imageai --upgrade

CMD ["python", "main.py"]
