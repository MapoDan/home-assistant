import base64
import os

@service
def b64toImage(b64image=None):
    fh = task.executor(os.open, "/media/image.png", os.O_RDWR)
    task.executor(os.write,fh,base64.b64decode(b64image))
    task.executor(os.close,fh)
