# My pyscript
Here I'll store my pyscript that helped me to solve some issues

## save_base64_image
I had an issue, I was trying to send an image attached to a mobile notification, but the image was in base64 and the companion app for HA requires a png/jpg.
Since there is no dedicated service to perform this conversion in HA and I wasn't able to find an easy, fast and working solution I've prepared this script.
Thanks to pyscript it is shown as a service in HA, you have just to pass it the base64 string as data and it will save the image in the media folder with the name image.png (it is overwritten at every request)

```yaml
data:
  b64image: str
```
in my case I've created an automation that is forwarding the persistent notification in HA to the mobile. So the automation checks if the persistent notification include an image, if so calls the pyscript giving to it the string. Then the second step of the automation is creating the mobile notification set as attachment the image at /media/local/image.png

##### Example
```yaml
service: pyscript.b64toimage
data:
  b64image: >-
    {% set messaggio= trigger.notification.message %}{{messaggio[messaggio.index('![image](data:')+31:-1]}}
```
