# How can I run this project?

For this project, you must install Ollama to handle the API interactions required for generating responses. Follow the steps below to set up Ollama and integrate it into your project.

---
Step 1: What is Ollama?

Ollama is an AI platform that allows you to interact with various AI models via a local API endpoint. For this project, we use it to process dynamic prompts and return concise English descriptions.
---
## Step 2: Installing Ollama
  1. Check System Requirements

      Operating System: Ensure your system supports Ollama (macOS, Linux, or Windows with WSL).
      Hardware: A machine with sufficient resources to run AI models locally.

  2. Install Ollama

      Visit the official Ollama website to download and install the software.
      Follow platform-specific instructions:
          macOS: Install using the provided .dmg installer.
          Linux: Follow the terminal installation steps.
          Windows (via WSL): Install WSL and set up Ollama using the Linux instructions.

  3. Verify Installation

      Open your terminal and run:

      ```ollama --version```

      You should see the version of Ollama installed. If not, revisit the installation steps.
---
## Step 3: Set Up Ollama for This Project
  1. Start Ollama

      Start the Ollama service in your terminal:
      ```
      ollama start
      ```
      This launches Ollama and sets up a local API endpoint, typically at http://localhost:11434/api/chat.

  2. Test the API

    Use curl or a REST client like Postman to ensure the API is running:

    ```curl -X POST http://localhost:11434/api/chat \
    -H "Content-Type: application/json" \
    -d '{
        "model": "llama3.2",
        "messages": [{"role": "user", "content": "Hello, Ollama!"}]
    }'
    ```

    You should receive a response confirming the API is active.

  3. Install a Model

      This project uses the llama3.2 model. Ensure it’s installed in Ollama:

      ```ollama install llama3.2```
---
# How to Build and Use a Configuration File for This Project
## Step 1: Create the Configuration File

    Name the file config.json.
    Structure the file with keys for each configurable parameter.

Example File:
```{
  "api_url": "http://localhost:11111/api/chat",
  "headers": {
    "Content-Type": "application/json"
  },
  "payload_defaults": {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": ""}]
  }
}

```
---
## Step 2: Understanding the Format

    JSON Format:
        Each key represents a configuration parameter.
        Keys can hold strings, objects, or arrays depending on the requirement.

### Key Breakdown:

    api_url:
        The URL for the API endpoint.
        Replace with your server's URL if different.

    prompt_template:
        A template string with a placeholder ({word}) for dynamic input.
        This allows you to customize the prompt by replacing {word} with an actual word.

    headers:
        HTTP headers required for the API request.
        Example: Content-Type specifies the type of data being sent (JSON in this case).

    payload_defaults:
        A dictionary containing the default structure of the request payload.
        The model key specifies the model to use.
        The messages key holds the default message structure.