# Webscrape

A Python-based web scraping tool for collecting airport information from various sources.

## Overview

This project provides web scraping utilities to gather data about major airports, currently supporting:
- **JFK** (John F. Kennedy International Airport)
- **LHR** (London Heathrow Airport)

The scraped data is stored in JSON format for easy processing and analysis.

## Project Structure

```
Webscrape/
├── main.py          # Main entry point for the application
├── jfk.py          # Web scraper for JFK Airport data
├── lhr.py          # Web scraper for LHR Airport data
├── jfk.json        # Scraped data for JFK Airport
├── lhr.json        # Scraped data for LHR Airport
└── .gitignore      # Git ignore configuration
```

## Features

- 🌐 Automated web scraping for airport information
- 📊 Data export to JSON format
- 🔄 Modular design for easy extension to additional airports
- 🐍 Built with Python

## Requirements

- Python 3.x
- Required Python packages (install via pip):
  ```bash
  pip install requests beautifulsoup4
  ```

## Usage

Run the main script to start scraping:

```bash
python main.py
```

Individual airport scrapers can also be run separately:

```bash
# Scrape JFK Airport data
python jfk.py

# Scrape LHR Airport data
python lhr.py
```

## Output

The scraped data is saved in JSON files:
- `jfk.json` - Contains scraped data from JFK Airport
- `lhr.json` - Contains scraped data from LHR Airport

## Contributing

Contributions are welcome! To add support for additional airports:

1. Create a new Python file named after the airport code (e.g., `lax.py`)
2. Implement the scraping logic following the existing patterns
3. Update `main.py` to include the new scraper
4. Submit a pull request

## License

This project is available for educational and research purposes.

## Disclaimer

⚠️ **Important**: When scraping websites, always:
- Check the website's `robots.txt` file
- Review and comply with the Terms of Service
- Implement rate limiting to avoid overloading servers
- Respect copyright and data usage policies

---

**Note**: This tool is for educational purposes. Always ensure you have permission to scrape data from websites and comply with their terms of service.
