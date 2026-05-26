FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    libgdal-dev \
    gdal-bin \
    libproj-dev \
    proj-data \
    proj-bin \
    libgeos-dev \
    libspatialindex-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────────────────────────────────────────
# PyTorch – pick ONE block below and comment out the other two.
# ─────────────────────────────────────────────────────────────────────────────

# ── Option 1: NVIDIA GPU (CUDA 12.4) ← ACTIVE ────────────────────────────────
#RUN pip install --no-cache-dir \
#    torch torchvision torchaudio \
#    --index-url https://download.pytorch.org/whl/cu124

# ── Option 2: CPU only ───────────────────────────────────────────────────────
RUN pip install --no-cache-dir \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cpu

# ── Option 3: Apple Silicon (MPS) ────────────────────────────────────────────
# NOTE: Requires running the container natively on macOS (not via Rosetta).
#       Use the standard PyPI build; MPS support is built in.
# RUN pip install --no-cache-dir \
#     torch torchvision torchaudio
# ─────────────────────────────────────────────────────────────────────────────

# Jupyter Lab and TensorBoard ports
EXPOSE 8888
EXPOSE 6006

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
