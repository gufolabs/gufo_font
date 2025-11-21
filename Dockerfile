FROM python:3.14-slim-trixie AS dev
COPY requirements.txt /tmp/
RUN\
    set -ex\
    && apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get -y autoremove\      
    && apt-get install -y --no-install-recommends\
    git\
    curl\
    ca-certificates\
    && (curl -fsSL https://deb.nodesource.com/setup_22.x | bash -)\
    && apt-get install -y --no-install-recommends\
    nodejs \    
    && npm install -g sass\
    && (curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local/bin sh)\
    && uv pip install --system -r /tmp/requirements.txt