"""Launcher wrapper for the Agentic Chatbot Streamlit app.

This file supports two invocation patterns:

- Direct Streamlit run (recommended):
    `streamlit run app.py` — runs the app under Streamlit's runner with full
    session support.

- Wrapper convenience: `python app.py` — this wrapper will invoke
    `python -m streamlit run app.py` automatically. The wrapper sets an
    internal `LAUNCHED_BY_APP_PY` environment flag to avoid re-launch loops.

Notes:
- Prefer `streamlit run app.py` for development.
- Ensure `GROQ_API_KEY` and `TAVILY_API_KEY` are set or provided via the UI
    when using those features.
"""

import os
import subprocess
import sys

from src.langgraphagentic_ai.main import load_langgraph_agenticai_app


def _is_streamlit_run() -> bool:
    """Return True when the script is running under Streamlit."""
    # Detect common Streamlit environment indicators and a wrapper-launched flag
    return bool(
        os.getenv("STREAMLIT_SERVER_PORT")
        or os.getenv("STREAMLIT_RUN_MAIN")
        or os.getenv("LAUNCHED_BY_APP_PY")
        or "streamlit" in " ".join(sys.argv)
    )


if __name__ == "__main__":
    if not _is_streamlit_run():
        print("This application must be run with Streamlit.")
        print("Launching Streamlit now...")
        script_path = os.path.abspath(__file__)
        try:
            # Pass an env flag so the re-executed script doesn't re-launch Streamlit again
            env = os.environ.copy()
            env["LAUNCHED_BY_APP_PY"] = "1"
            subprocess.check_call([sys.executable, "-m", "streamlit", "run", script_path], env=env)
        except subprocess.CalledProcessError as exc:
            print(f"Failed to launch Streamlit: {exc}")
            sys.exit(exc.returncode if exc.returncode is not None else 1)
        except FileNotFoundError:
            print("Streamlit is not installed or not available in this Python environment.")
            print("Install it with: python -m pip install streamlit")
            sys.exit(1)
        sys.exit(0)

    load_langgraph_agenticai_app()
