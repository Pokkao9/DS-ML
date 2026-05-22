import subprocess

# Install localtunnel
!npm install localtunnel

# Run the Streamlit app in the background, suppressing its output
command = "streamlit run clean_app.py"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Expose the Streamlit app via localtunnel
# The Streamlit app runs on port 8501 by default
!npx localtunnel --port 8501
