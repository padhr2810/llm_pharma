# Medicine Safety

A suite of tools to monitor and enhance medicines safety.

Features backlog:
1. Object detection to identify a medicines package / tablet or capsule. Fine-tune a model.
2. Matching drug name to list of side effects
3. Questionnaire to report drug side effects to pharmacovigilance authorities
4. Large language model to analyse patients' description of their symptoms and classify them

Tools:
1. MLFLow
2. LLM serving stack
3. PostgreSQL backend
4. Django app framework
5. SAM2 object detection
6. FastAPI to build endpoints
7. Docker
8. kubeflow (TBD)

Unsloth.ai (for fine tuning)

AdalFlow (for pre-production and optimizations)

vLLM (for model serving

sqlalchemy put CSV into sql

# install git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
# clone the LLM
git lfs install
git clone https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
