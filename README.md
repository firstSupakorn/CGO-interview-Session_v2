# CGO-interview-Session

# How to run docker container
1. pull docker image from docker registry
```
docker pull firstspk1/testcgo:2
docker run -it -p 9999:9999 firstspk1/testcgo:2
```

2. git clone this repository
```
# After clone this repository
docker build -t testcgo .
docker run -it -p 9999:9999 testcgo
```


If the container can work normally, It will show results as follows
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 17, 2020 - 04:05:01
Django version 2.2.6, using settings 'cgoInterviewSession.settings'
Starting development server at http://0.0.0.0:9999/
Quit the server with CONTROL-C.
```


Then create an HTTP GET method on port 9999, Enter x and a value and press submit.
```
x = 5
a = [1,2,3,4,5,7]
http://localhost:9999/testcgo/?x=5&a=1,2,3,4,5,7
output: The earliest time when the frog can jump to the other side of the river is 4
```

```
x = 5
a = [1,3,1,4,2,3,5,4]
http://localhost:9999/testcgo/?x=5&a=1,3,1,4,2,3,5,4
The earliest time when the frog can jump to the other side of the river is 6 
```

### Input screen
![alt text](https://github.com/firstSupakorn/CGO-interview-Session_v2/blob/master/InputScreen.jpg)
### Output screen
![alt text](https://github.com/firstSupakorn/CGO-interview-Session_v2/blob/master/output.ScreenJPG.JPG)
