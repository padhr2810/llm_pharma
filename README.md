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

# NDC code
The NDC, or National Drug Code, is a unique 10-digit, 3-segment number.

In the package NDC file it is 10 digits. Column = ndcpackagecode ... e.g. 0002-0800-01

For the product NDC file it is only 8 digits. Column = productndc ... e.g. 0002-0800


# install git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash

sudo apt-get install git-lfs
# clone the LLM
git lfs install

git clone https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct

# favicon.ico 
https://www.favicon-generator.org/

It isn't required. It stands for "favourite icon" and is the icon the browser will use when displaying the page. You know the logos in each tab of a web browser? Those are favicons.

A favicon is an icon that appears at the top of a browser tab. Although they are not required, favicons are important because they help the user identify your site. If you would like to generate a favicon, use this link abvoe. Add this code to the section of your website<link rel='icon' href='favicon.ico' type='image/x-icon'/ >

# Questionnaire
1. Age
2. sex
3. Diagnoses
4. Medication

