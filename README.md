# SHORTEN

A simple and functional URL shortening service built using **Python (Flask)**. It allows users to enter a long URL and generates a unique, shortened version that can be used to redirect to the original URL.

## Features

- Generate short URLs for long links
- Redirect short URLs to the original address
- Stores URL mappings using a lightweight sqlitedb
- Basic web interface for input and redirection
- Timestamp-based short code generation

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (basic styling)
- **Storage**: sqlitedb

## How It Works

1. User enters a long URL on the web interface.
2. The app generates a unique short code based on timestamp and stores the mapping.
3. When the user visits the short URL, it redirects them to the original URL.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask

### Installation

```bash
git clone https://github.com/praveen-01/System-design.git
cd System-design/url-shortner
docker build -t url-shortener .
```

### Further Implementations

- Use a standalone database like postgres
- Add in-memory cache for scaling
- Deploy the application to public domains
- Integrate CI after deploying
- Add analytics for link clicks for logged-in users
