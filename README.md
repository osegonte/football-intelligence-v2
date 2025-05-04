# Football Data Pipeline

A robust data pipeline for collecting and managing football match statistics from SofaScore and FBref.

## Features

- **Automated Fixture Collection**: Hourly updates of upcoming matches from SofaScore
- **Match Statistics Scraping**: Detailed match stats from FBref after games complete
- **Kickoff Monitoring**: Automated detection of completed matches for timely data collection
- **Data Reconciliation**: 3-day reconciliation pass to ensure data completeness
- **Robust Error Handling**: Retries, error recovery, and comprehensive logging
- **Task Queue**: Redis-based task queue for reliable background processing

## Architecture

The pipeline consists of four main components:

1. **Fixtures Loader**: Fetches upcoming fixtures from SofaScore API
2. **Kickoff Watchdog**: Monitors fixtures and schedules stat collection
3. **Stats Scraper**: Collects match statistics from FBref
4. **Reconciliation Service**: Ensures data completeness and accuracy

## Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis 6+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/football-data-pipeline.git
cd football-data-pipeline
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials and settings
```

5. Initialize the database:
```bash
python database/migrate.py
```

## Usage

### Running the Pipeline

Start the task worker:
```bash
python scripts/run_worker.py
```

Start the scheduler:
```bash
python scripts/run_scheduler.py
```

### Manual Operations

Fetch fixtures for a specific date:
```bash
python scripts/fetch_fixtures.py --date 2025-05-04
```

Fetch match statistics:
```bash
python scripts/fetch_match_stats.py --fixture-id 12345
```

## Database Schema

The pipeline uses the following main tables:

- `teams`: Team information
- `competitions`: Competition/league details
- `seasons`: Season information
- `venues`: Stadium information
- `fixtures`: Upcoming matches
- `matches`: Completed match statistics

## Configuration

Key configuration options in `.env`:

- `DB_*`: Database connection settings
- `REDIS_URL`: Redis connection for task queue
- `SCRAPING_DELAY_*`: Rate limiting for scrapers
- `*_INTERVAL`: Timing for various tasks

## Testing

Run tests with:
```bash
pytest tests/
```

With coverage:
```bash
pytest tests/ --cov=football_data_pipeline
```

## Docker Deployment

Build and run with Docker:
```bash
docker-compose up -d
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.