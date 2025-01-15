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