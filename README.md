# Style Transfer

The [style transfer](https://en.wikipedia.org/wiki/Neural_Style_Transfer) application is based on the [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://cs.stanford.edu/people/jcjohns/eccv16/) paper and [Justin Johnson](https://web.eecs.umich.edu/~justincj/) 's [pre-trained models](https://github.com/jcjohnson/fast-neural-style).

We'll use FastAPI as the backend to serve the predictions, Streamlit for the user interface, and OpenCV to do the actual prediction. Docker will be used to containerize the application.


Download the style transfer models:
```shell
sh download_models.sh
```

To build the backend image and run the container:
```shell
cd backend
docker build -t backend .
docker run -p 8080:8080 backend
```

To build the frontend image and run the container:
```shell
cd frontend
docker build -t frontend .
docker run -p 8081:8081 frontend
```

