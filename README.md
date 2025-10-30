```markdown
# Safe Flask username echo (prevents XSS)

This small Flask app accepts a username and displays "Wlcome <username>" while escaping the input to prevent XSS.

## Files added

- app.py
- templates/index.html
- templates/result.html
- requirements.txt

## Setup and run locally

1. Create a virtual environment and install requirements:
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt

2. Run the app:
   python app.py

3. Open http://127.0.0.1:5000 in your browser.

## Security notes

- The app uses server-side escaping (`flask.escape` and Jinja2 auto-escaping) to avoid reflected XSS.
- Do not set `debug=True` on a production server.
- If you want an environment to *safely learn* about XSS and web vulnerabilities, use purpose-built, isolated lab projects such as:
  - OWASP Juice Shop
  - OWASP WebGoat
  - Damn Vulnerable Web Application (DVWA)

Always run intentionally-vulnerable apps in an isolated environment (e.g., a local VM or Docker) and never expose them to the public internet.
```
