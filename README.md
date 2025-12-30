# Agentic Chat Bot Application

Overview
--------
Agentic Chat Bot built with Streamlit, LangChain (Groq), and LangGraph. Two use-cases are provided:
1. Basic chat
2. Chat with web search using Tavily

Requirements
------------
- Python 3.8+
- See `requirements.txt` for runtime dependencies. Install with:

```bash
python -m pip install -r requirements.txt
```

Run
---
Preferred (recommended): start the app with Streamlit so session state and UI behave correctly:

```bash
streamlit run app.py
```

Alternate: the repository includes a small wrapper so you can also run:

```bash
python app.py
```

The wrapper will attempt to launch `streamlit run app.py` automatically. Running `python app.py` directly still launches Streamlit, but using `streamlit run` is recommended for development and debugging.

Environment variables
---------------------
- `GROQ_API_KEY`: API key for Groq LLM (if using Groq models)
- `TAVILY_API_KEY`: API key for Tavily search (if using web search tools)

You can set these in your environment or enter them in the UI when prompted.

Troubleshooting
---------------
- If you see warnings about "missing ScriptRunContext" or "Session state does not function when running a script without `streamlit run`", start the app with `streamlit run app.py` instead of `python app.py`.
- If the `streamlit` command is not found after installing, add your Python `Scripts` directory to `PATH`. Example (PowerShell):

```powershell
$env:Path += ";$env:USERPROFILE\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts"
```

Notes
-----
- The small wrapper in `app.py` will set an internal environment flag to avoid relaunch loops. You can safely use either startup method, but `streamlit run` gives the best developer experience.

If you want a dedicated RUNNING.md or additional deployment instructions, tell me which target (local, Docker, or cloud) and I will add it.

