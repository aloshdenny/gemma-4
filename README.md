# 🤖 AI Agent Development Toolkit

This repository is a collection of examples and implementations designed to help developers build advanced, multimodal AI agents. It covers foundational concepts from basic input processing (text, vision, audio) up to complex agentic workflows using external tools and local/cloud LLMs.

## ✨ Features Overview

*   **Multimodal Input:** Basic handling for Chat, Vision (Image), and Audio inputs.
*   **Tool Use:** Implementing structured tool calling mechanisms for LLMs.
*   **Agent Framework:** A dedicated structure for building autonomous agents that can reason and execute multi-step tasks.
*   **Model Flexibility:** Supports both commercial APIs (OpenAI) and local models (Ollama).

## 🚀 Getting Started

### Prerequisites

Before running any code, ensure you have Python installed and set up your environment.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/aloshdenny/gemma-4
    cd gemma-4
    ```

2.  **Install Dependencies:**
    The required libraries are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Ollama (if you haven't):**
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
    ```bash
    ollama serve
    ```

## 📂 Usage Guide

The repository is structured into modules based on complexity and functionality.

### 1. `1_basics/` - Foundational Inputs

This directory contains basic examples demonstrating how to handle different types of multimodal inputs:

*   **`chat/`**: Examples for standard conversational AI interactions.
*   **`vision/`**: Code snippets for processing and understanding images (e.g., describing an image, reading text from it).
*   **`audio/`**: Implementation using `faster-whisper` or similar tools for speech-to-text transcription.

### 2. `2_tools/` - Tool Integration

This section focuses on giving LLMs the ability to interact with external functions (Tools).

*   **`main.py`**: The primary entry point for testing tool usage.
*   **`tools/`**: Contains definitions and implementations of the tools that the AI agent can call (e.g., a calculator, a database lookup function).
*   **Goal:** Learn how to structure prompts and model calls so the LLM knows *when* and *how* to use available functions.

### 3. `3_agent/` - Autonomous Agents

This is the core agentic logic of the repository. It demonstrates building agents that can plan, execute, and iterate on tasks without constant human prompting.

*   **`agent.py`**: Contains the main agent loop or class responsible for reasoning (e.g., using a ReAct pattern).
*   **`tools.py`**: Defines the specific tools available to this advanced agent instance.
*   **`prompt.py`**: Holds sophisticated system prompts that guide the agent's behavior, memory, and decision-making process.

## 💡 Quick Start Example (Conceptual)

To run a basic tool-using agent:

1.  Navigate to `3_agent/`.
2.  Modify `agent.py` or `main.py` to load your desired tools from `tools.py`.
3.  Execute the script, providing an initial prompt that requires tool usage (e.g., "What is 50 times 12?").

---
*Happy Coding!*