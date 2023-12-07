FROM continuumio/miniconda3

WORKDIR /home

EXPOSE 5000

COPY . .

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN pip install Flask

RUN pip install -r requirements.txt

CMD ["python", "app.py"]