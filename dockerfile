from Python:3.10

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/deepset-ai/haystack.git

