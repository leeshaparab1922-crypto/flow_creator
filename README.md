# 📘 Guide Creator Flow

A **CrewAI Flow** that transforms raw learning resources into a **publication-ready, beginner-friendly Markdown guide**. Simply provide sources such as **YouTube videos, documentation pages, arXiv research papers, or local PDF files**, and the system automatically researches, enriches, and writes a structured learning guide.

Once the guide is generated, an **AI-powered student chatbot** can answer questions using **only the generated guide and the original source material**, ensuring reliable and grounded responses.

---

## ✨ Features

* 📺 Extracts information from YouTube videos
* 🌐 Processes documentation websites and web articles
* 📄 Reads arXiv research papers
* 📁 Supports local PDFs, Markdown, and text files
* 🤖 Automatically activates only the agents required for the provided source types
* 🔍 Performs additional web research when information gaps are detected
* ✍️ Generates a publication-ready Markdown guide
* 👨‍🎓 Creates beginner-friendly explanations
* 💬 Student chatbot answers questions using only the generated guide and source material
* 📚 Provides grounded responses with section and source references
* 🚫 Clearly states when requested information is not present in the provided material

---

# 🏗️ Architecture

```text
                Input Sources
                       │
      ┌────────────────┼────────────────┐
      │                │                │
 YouTube          Documentation      arXiv Papers
      │                │                │
      └────────────────┼────────────────┘
                       │
                Local PDFs / Files
                       │
                       ▼
               Research Crew
                       │
                       ▼
          Research Quality Evaluation
                       │
         ┌─────────────┴─────────────┐
         │                           │
     Score ≥ Threshold         Score < Threshold
         │                           │
         ▼                           ▼
      Skip                     Enrichment Crew
                                    │
                                    ▼
                             Additional Research
                                    │
                                    ▼
                             Writing Crew
                                    │
      ┌──────────────┬──────────────┬──────────────┐
      │              │              │              │
   Outline      Full Draft     Review      Final Guide
                                    │
                                    ▼
                          Student Chatbot
                                    │
                                    ▼
                        Grounded Question Answering
```

---

# 🔄 Workflow

The project consists of **three sequential CrewAI crews**.

## 1. Research Crew

The Research Crew gathers information from every source provided.

Supported source types include:

* YouTube videos
* Documentation websites
* Web articles
* arXiv papers
* Local PDF files
* Markdown documents
* Text documents

Instead of running every specialist, the workflow dynamically activates **only the agents required** for the supplied sources, making execution faster and more efficient.

---

## 2. Enrichment Crew

After research is completed, the collected information is evaluated.

If the research quality score is below a predefined threshold, the Enrichment Crew performs additional targeted web searches to fill missing information.

If the research is already sufficient, this stage is skipped automatically.

---

## 3. Writing Crew

The Writing Crew converts the research into a polished guide using a four-stage pipeline:

1. Create a structured outline
2. Generate a complete draft
3. Review for beginner friendliness and clarity
4. Produce the final edited Markdown guide

The resulting guide is organized, easy to read, and suitable for self-learning.

---

# 💬 Student Chatbot

After the guide is generated, an AI student assistant can be launched.

The chatbot:

* Answers questions using only the generated guide and original sources
* Never invents information outside the provided material
* References the guide section or original source used for each answer
* Clearly indicates when a topic is not covered by the available material

This helps ensure trustworthy and explainable responses.

---

# 📂 Project Workflow

```text
Input Sources
      │
      ▼
Research Crew
      │
      ▼
Quality Evaluation
      │
      ├── High Quality ──────────────► Writing Crew
      │
      └── Needs Improvement
                  │
                  ▼
          Enrichment Crew
                  │
                  ▼
            Writing Crew
                  │
                  ▼
      Beginner-Friendly Guide
                  │
                  ▼
         Student AI Chatbot
```

---

# 🛠️ Technology Stack

* Python
* CrewAI
* Large Language Models (LLMs)
* Markdown
* arXiv Integration
* YouTube Content Extraction
* Web Scraping
* PDF Processing

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/leeshaparab1922-crypto/flow_creator.git
```

## Navigate to the project

```bash
cd flow_creator
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

Create a `.env` file and add the required API keys and configuration values.

Example:

```env
OPENAI_API_KEY=your_api_key
SERPER_API_KEY=your_api_key
```

*(Add any additional environment variables required by your project.)*

---

## Run the project

```bash
python main.py
```

or use the appropriate entry point for your CrewAI flow.

---

# 📖 Example Use Cases

* Generate study guides from YouTube playlists
* Summarize technical documentation
* Create beginner-friendly tutorials from research papers
* Build educational content from mixed learning resources
* Create an AI tutor for custom course material

---

# 📌 Future Enhancements

* Multi-language guide generation
* Interactive diagrams
* Support for additional document formats
* Export to PDF and HTML
* Multiple chatbot personas
* Incremental guide updates
* Citation generation in APA/IEEE formats

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Leesha Parab**

GitHub: https://github.com/leeshaparab1922-crypto
