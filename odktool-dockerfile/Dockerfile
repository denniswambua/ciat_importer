FROM ubuntu:18.04
RUN apt update && apt install -y build-essential qt5-default qtbase5-private-dev qtdeclarative5-dev libqt5sql5-mysql cmake mongodb jq libboost-all-dev unzip zlib1g-dev automake npm

WORKDIR /opt
RUN apt install -y git
RUN git clone https://github.com/qlands/odktools.git

RUN mkdir odktools-deps
WORKDIR /opt/odktools-deps
RUN apt install -y wget
RUN wget https://github.com/mongodb/mongo-c-driver/releases/download/1.6.1/mongo-c-driver-1.6.1.tar.gz && wget https://github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz && wget https://github.com/jmcnamara/libxlsxwriter/archive/RELEASE_0.7.6.tar.gz && wget https://downloads.sourceforge.net/project/quazip/quazip/0.7.3/quazip-0.7.3.tar.gz && git clone https://github.com/rgamble/libcsv.git


WORKDIR /opt/odktools-deps
RUN tar xvfz mongo-c-driver-1.6.1.tar.gz
WORKDIR /opt/odktools-deps/mongo-c-driver-1.6.1
RUN ./configure && make && make install

WORKDIR /opt/odktools-deps
RUN tar xvfz quazip-0.7.3.tar.gz
WORKDIR /opt/odktools-deps/quazip-0.7.3
RUN mkdir build
WORKDIR /opt/odktools-deps/quazip-0.7.3/build
RUN cmake -DCMAKE_C_FLAGS:STRING="-fPIC" -DCMAKE_CXX_FLAGS:STRING="-fPIC" ..
RUN make && make install

RUN ln -s /usr/bin/aclocal-1.15 /usr/bin/aclocal-1.14 && ln -s /usr/bin/automake-1.15 /usr/bin/automake-1.14

WORKDIR /opt/odktools-deps
RUN tar xvfz RELEASE_0.7.6.tar.gz
WORKDIR /opt/odktools-deps/libxlsxwriter-RELEASE_0.7.6
RUN mkdir build
WORKDIR /opt/odktools-deps/libxlsxwriter-RELEASE_0.7.6/build
RUN cmake .. && make && make install

WORKDIR /opt/odktools-deps/libcsv
RUN ./configure && make && make install

WORKDIR /opt/odktools/dependencies/mongo-cxx-driver-r3.1.1
RUN mkdir build
WORKDIR /opt/odktools/dependencies/mongo-cxx-driver-r3.1.1/build
RUN  cmake -DCMAKE_C_FLAGS:STRING="-O2 -fPIC" -DCMAKE_CXX_FLAGS:STRING="-O2 -fPIC" -DBSONCXX_POLY_USE_BOOST=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
RUN make && make install

WORKDIR /opt/odktools/dependencies/json2csv-cpp
RUN apt install -y libjsoncpp-dev
RUN ln -s /usr/include/jsoncpp/json/ /usr/include/json
RUN qmake && make
RUN cp json2csv /usr/bin

WORKDIR /opt/odktools
RUN apt install -y libtclap-dev
RUN qmake && make
ENV LD_LIBRARY_PATH=/usr/local/lib