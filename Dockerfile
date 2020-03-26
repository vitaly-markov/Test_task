FROM python:3.6
LABEL maintainer="Vitali Markau <vitali_markau@epam.com>"
COPY . /app
WORKDIR /app
RUN pip install Flask==1.0.2 
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
