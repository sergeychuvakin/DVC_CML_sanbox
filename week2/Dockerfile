FROM python:3.9
WORKDIR /app 

RUN apt-get update -y && \ 
    apt-get upgrade -y && \
    python -m pip install --upgrade pip

# Boost instalation
RUN wget https://boostorg.jfrog.io/artifactory/main/release/1.63.0/source/boost_1_63_0.zip   && \
    unzip boost_1_63_0.zip && \
    mv boost_1_63_0 /usr/local/bin

# StarSpace installation
RUN git clone https://github.com/facebookresearch/Starspace.git && \
    cd Starspace && \
    make


ARG USER_ID
ARG GROUP_ID
ARG INPUT_DATA

# RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

# ENTRYPOINT [ "/app/Starspace/starspace"]
# CMD ["train", "-trainFile", "/app/vol/starspace_input_file.txt", "-model", "/app/vol/modelSavedFile"]
CMD /app/Starspace/starspace train -trainFile "$INPUT_DATA" -model /app/vol/modelSavedFile